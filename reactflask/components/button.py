
import hashlib
from .base import BaseComponent




class _Redirect:
    def __init__(self, route):
        self.route = route

def Redirect(route):
    return _Redirect(route)

class Button(BaseComponent):
    """A clickable button component."""
    def __init__(self, parent, label, onClick=None, color=None, background=None, width=None, height=None):
        super().__init__(parent, width=width, height=height)
        self.label = label
        self.onClick = onClick
        self.color = color
        self.background = background
        self.route = None
        self.is_redirect = False
        if onClick:
            if isinstance(onClick, _Redirect):
                self.is_redirect = True
                self.route = onClick.route
            else:
                hash_id = hashlib.md5((label + str(id(onClick))).encode()).hexdigest()[:8]
                self.route = f'/button_{hash_id}'
                self._route_parent.add_button_route(self.route, onClick)

    def render(self):
        """Render the button as HTML."""
        if not self.visible:
            return ""
        extra = ""
        if self.background:
            extra += f'background-color: {self.background}; '
        if self.color:
            extra += f'color: {self.color}; '
        style = self.get_style(extra)
        btn_class = 'rf-btn'
        if self.route:
            if self.is_redirect:
                return f'<button class="{btn_class}" style="{style}" onclick="window.location.href=\'{self.route}\';">{self.label}</button>'
            return f'<button class="{btn_class}" style="{style}" onclick="fetch(\'{self.route}\', {{method: \'PUT\'}}).then(r => r.ok && console.log(\'Button clicked!\'))">{self.label}</button>'
        return f'<button class="{btn_class}" style="{style}">{self.label}</button>'
