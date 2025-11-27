
from flask import Flask, redirect, request, send_from_directory
import os
from flask_socketio import SocketIO


class FlaskNative(Flask):
    """A Flask app with simple component-based layout (pack/grid) and routes for UI events."""

    def add_select_route(self, route, dropdown):
        """Add a route to update dropdown value via PUT."""
        def handler():
            data = request.get_json(force=True)
            dropdown.selected = data.get('value', dropdown.selected)
            if hasattr(dropdown, 'onChange') and dropdown.onChange:
                dropdown.onChange(dropdown.selected)
            return '', 204
        self.add_url_rule(route, route, handler, methods=['PUT'])

    def add_static_routes(self):
        static_dir = os.path.join(os.path.dirname(__file__), 'static')
        @self.route('/static/css/<path:filename>')
        def static_css(filename):
            return send_from_directory(os.path.join(static_dir, 'css'), filename)

    def setTitle(self, title):
        """Set the browser tab title."""
        self.title = title
        return self
    
    def __init__(self, import_name, title="React Flask App"):
        super().__init__(import_name)
        self.title = title
        self._background = None
        self.components = []
        self.packed = []
        self.grid = {}
        self.bodies = {}  # route -> Body
        self.footer = None
        self.nav = None
        self.headerbar = None
        self.add_static_routes()
        self.socketio = SocketIO(self)

    def register_body(self, body, route):
        self.bodies[route] = body
        self.add_url_rule(route, f'body_{route}', lambda: body.render_page())

    def title(self, value):
        """Set the browser tab title."""
        self.title = value
        return self

    def background(self, color):
        """Set the background color of the site."""
        self._background = color
        return self

    def add_component(self, component, area=None):
        """Register a component for value updates, optionally to a layout area."""
        if area is None:
            self.components.append(component)
        else:
            # Support multiple bodies by area name
            if area.startswith('body_') and area in self.bodies:
                self.bodies[area].add_component(component)
            elif hasattr(self, area) and getattr(self, area):
                getattr(self, area).add_component(component)
            else:
                self.components.append(component)

    def add_packed(self, component):
        """Add a component to packed layout."""
        if self.grid:
            raise Exception("Cannot use pack when grid layout is already in use.")
        self.packed.append(component)

    def add_grid(self, component, row, column, columnspan=1, rowspan=1):
        """Add a component to grid layout, supporting columnspan and rowspan."""
        if self.packed:
            raise Exception("Cannot use grid when pack layout is already in use.")
        if not hasattr(component, 'grid_info') or component.grid_info is None:
            component.grid_info = {}
        component.grid_info.update({
            'row': row,
            'column': column,
            'columnspan': columnspan,
            'rowspan': rowspan
        })
        self.grid.setdefault(row, {})[column] = component

    def add_entry_route(self, route, entry):
        """Add a route to update entry value via PUT."""
        def handler():
            data = request.get_json(force=True)
            entry.value = data.get('value', '')
            return '', 204
        self.add_url_rule(route, route, handler, methods=['PUT'])
        

    def add_switch_route(self, route, switch):
        """Add a route to update switch state via PUT (for Switch, Checkbox, Toggle)."""
        def handler():
            data = request.get_json(force=True)
            switch.state = bool(data.get('state', False))
            if hasattr(switch, 'on_toggle') and switch.on_toggle:
                switch.on_toggle(switch.state)
            return '', 204
        self.add_url_rule(route, route, handler, methods=['PUT'])
    
    def add_button_route(self, route, func):
        """Add a route for button click (PUT)."""
        def handler():
            if request.method == 'PUT':
                func()
                return '', 204
            # fallback for GET (optional, can remove if not needed)
            for comp in self.components:
                if hasattr(comp, 'name') and comp.name.startswith('entry_'):
                    entry_value = request.args.get(comp.name) or request.form.get(comp.name, "")
                    if entry_value:
                        comp.value = entry_value
            func()
            return redirect('/')
        self.add_url_rule(route, route, handler, methods=['PUT', 'GET'])
        
    def home(self):
        """Render the home page with layout areas if present, using sticky header/nav/footer."""
        style = f' style="background:{self._background};"' if self._background else ''
        html = f'''<html><head><title>{self.title}</title>
        <link rel="stylesheet" href="/static/css/button.css">
        <link rel="stylesheet" href="/static/css/header.css">
        <link rel="stylesheet" href="/static/css/paragraph.css">
        <link rel="stylesheet" href="/static/css/entry.css">
        <link rel="stylesheet" href="/static/css/toggle.css">
        <link rel="stylesheet" href="/static/css/checkbox.css">
        <link rel="stylesheet" href="/static/css/layout.css">
        <link rel="stylesheet" href="/static/css/dropdown.css">
        </head><body{style}>'''
        if self.headerbar:
            html += f'<div id="headerbar">{self.headerbar.render()}</div>'
        if self.nav:
            html += f'<nav id="nav">{self.nav.render()}</nav>'
        if self.body:
            html += f'<main id="body">{self.body.render()}</main>'
        else:
            if self.grid and self.packed:
                html += '<p style="color:red;">Error: Cannot use both pack and grid layouts at the same time.</p>'
            elif self.grid:
                html += '<table style="border-collapse:collapse;">'
                max_row = max(self.grid.keys()) if self.grid else -1
                for r in range(max_row+1):
                    html += '<tr>'
                    row_dict = self.grid.get(r, {})
                    max_col = max(row_dict.keys()) if row_dict else -1
                    for c in range(max_col+1):
                        cell = row_dict.get(c)
                        style = ''
                        if cell and getattr(cell, 'grid_info', None):
                            padx = cell.grid_info.get('padx', 0)
                            pady = cell.grid_info.get('pady', 0)
                            if padx or pady:
                                style = f'padding-left:{padx}px;padding-right:{padx}px;padding-top:{pady}px;padding-bottom:{pady}px;'
                        html += f'<td{f' style="{style}"' if style else ''}>'
                        if cell:
                            html += cell.render()
                        html += '</td>'
                    html += '</tr>'
                html += '</table>'
            else:
                for comp in self.packed:
                    html += comp.render()
        if self.footer:
            html += f'<footer id="footer">{self.footer.render()}</footer>'
        html += '</body></html>'
        return html