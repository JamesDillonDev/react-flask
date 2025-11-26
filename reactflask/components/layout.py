
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

    def add_grid(self, component, row, column):
        # For now, treat grid as just adding to components
        self.components.append(component)
    def render(self):
        style = f' style="background:{self._background};"' if hasattr(self, '_background') and self._background else ''
        html = f'<div{style}>'
        for comp in self.components:
            html += comp.render()
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
    def __init__(self, app):
        super().__init__(app, 'body')
        app.body = self

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
