
import hashlib
from .base import BaseComponent

class Button(BaseComponent):
    """A clickable button component."""
    def __init__(self, parent, label, onClick=None, color="#007bff", width=None, height=None):
        super().__init__(parent, width=width, height=height)
        self.label = label
        self.onClick = onClick
        self.color = color
        self.route = None
        if onClick:
            hash_id = hashlib.md5((label + str(id(onClick))).encode()).hexdigest()[:8]
            self.route = f'/button_{hash_id}'
            parent.add_button_route(self.route, onClick)

    def render(self):
        """Render the button as HTML."""
        if not self.visible:
            return ""
        style = (
            f'background-color: {self.color}; '
            'color: white; '
            'border: none; '
            'padding: 10px 20px; '
            'border-radius: 5px; '
            'font-size: 16px; '
            'cursor: pointer; '
            'transition: background 0.3s; '
        )
        if self.width:
            style += f'width: {self.width}; '
        if self.height:
            style += f'height: {self.height}; '
        active_css = '<style>.rf-btn:active{filter:brightness(85%);}</style>'
        btn_class = 'rf-btn'
        if self.route:
            return f'''{active_css}<button class="{btn_class}" style="{style}" onclick="fetch('{self.route}', {{method: 'PUT'}}).then(r => r.ok && console.log('Button clicked!'))">{self.label}</button>'''
        return f'{active_css}<button class="{btn_class}" style="{style}">{self.label}</button>'
