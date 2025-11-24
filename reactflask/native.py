from flask import Flask, redirect, request


class FlaskNative(Flask):
    """A Flask app with simple component-based layout (pack/grid) and routes for UI events."""
    def __init__(self, import_name):
        super().__init__(import_name)
        self.components = []
        self.packed = []
        self.grid = {}
        self.add_url_rule('/', 'home', self.home)

    def add_component(self, component):
        """Register a component for value updates."""
        self.components.append(component)

    def add_packed(self, component):
        """Add a component to packed layout."""
        if self.grid:
            raise Exception("Cannot use pack when grid layout is already in use.")
        self.packed.append(component)

    def add_grid(self, component, row, column):
        """Add a component to grid layout."""
        if self.packed:
            raise Exception("Cannot use grid when pack layout is already in use.")
        self.grid.setdefault(row, {})[column] = component

    def add_entry_route(self, route, entry):
        """Add a route to update entry value via PUT."""
        def handler():
            data = request.get_json(force=True)
            entry.value = data.get('value', '')
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
        """Render the home page with either grid or packed layout."""
        html = '<html><body>'
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
        html += '</body></html>'
        return html