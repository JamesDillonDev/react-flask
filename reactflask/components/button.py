
import hashlib
from .base import BaseComponent

class Button(BaseComponent):
    """A clickable button component."""
    def __init__(self, parent, label, onClick=None, color="#007bff"):
        super().__init__(parent)
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
        if self.route:
            return f'<form action="{self.route}" method="get" style="display:inline;"><button type="submit" style="{style}">{self.label}</button></form>'
        return f'<button style="{style}">{self.label}</button>'
