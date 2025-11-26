
class LayoutArea:
    def __init__(self, app, name):
        self.app = app  # Reference to FlaskNative
        self.name = name
        self.components = []
    def add_component(self, component):
        self.components.append(component)

    def add_packed(self, component):
        # For now, treat packed as just adding to components
        self.components.append(component)

    def add_grid(self, component, row, column, columnspan=1, rowspan=1):
        # Store grid info in component for layout rendering
        if not hasattr(component, 'grid_info') or component.grid_info is None:
            component.grid_info = {}
        component.grid_info.update({
            'row': row,
            'column': column,
            'columnspan': columnspan,
            'rowspan': rowspan
        })
        self.components.append(component)
    def render(self):
        style = f' style="background:{self._background};"' if hasattr(self, '_background') and self._background else ''
        html = f'<div{style}>'
        # Basic grid rendering: wrap each row in a div, use inline-block for columns
        grid_map = {}
        for comp in self.components:
            info = getattr(comp, 'grid_info', None)
            if info:
                row = info.get('row', 0)
                grid_map.setdefault(row, []).append((info.get('column', 0), info.get('columnspan', 1), comp))
            else:
                html += comp.render()
        for row in sorted(grid_map.keys()):
            html += '<div style="display:flex;">'
            for col, colsp, comp in sorted(grid_map[row], key=lambda x: x[0]):
                flex = f'flex:{colsp};' if colsp > 1 else ''
                html += f'<div style="display:inline-block;{flex}">{comp.render()}</div>'
            html += '</div>'
        html += '</div>'
        return html
    # Forward route-related calls to app
    def add_entry_route(self, *args, **kwargs):
        return self.app.add_entry_route(*args, **kwargs)
    def add_switch_route(self, *args, **kwargs):
        return self.app.add_switch_route(*args, **kwargs)
    def add_button_route(self, *args, **kwargs):
        return self.app.add_button_route(*args, **kwargs)


class Body(LayoutArea):
    def __init__(self, app, route='/'):
        super().__init__(app, f'body_{route}')
        self.route = route
        app.register_body(self, route)

    def render_page(self):
        # Render a full page with headerbar, nav, body, and footer
        style = f' style="background:{self._background};"' if hasattr(self, '_background') and self._background else ''
        html = f'''<html><head><title>{self.app.title}</title>
        <link rel="stylesheet" href="/static/css/button.css">
        <link rel="stylesheet" href="/static/css/header.css">
        <link rel="stylesheet" href="/static/css/paragraph.css">
        <link rel="stylesheet" href="/static/css/entry.css">
        <link rel="stylesheet" href="/static/css/toggle.css">
        <link rel="stylesheet" href="/static/css/checkbox.css">
        <link rel="stylesheet" href="/static/css/layout.css">
        </head><body{style}>'''
        if self.app.headerbar:
            html += f'<div id="headerbar">{self.app.headerbar.render()}</div>'
        if self.app.nav:
            html += f'<nav id="nav">{self.app.nav.render()}</nav>'
        html += f'<main id="body">{self.render()}</main>'
        if self.app.footer:
            html += f'<footer id="footer">{self.app.footer.render()}</footer>'
        html += '</body></html>'
        return html

class Footer(LayoutArea):
    def __init__(self, app):
        super().__init__(app, 'footer')
        app.footer = self

class Nav(LayoutArea):
    def __init__(self, app):
        super().__init__(app, 'nav')
        app.nav = self

class HeaderBar(LayoutArea):
    def __init__(self, app):
        super().__init__(app, 'headerbar')
        app.headerbar = self
