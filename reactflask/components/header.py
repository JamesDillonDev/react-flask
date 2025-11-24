from .base import BaseComponent

class Header(BaseComponent):
    """A header component (h1-h6)."""
    def __init__(self, parent, text, level=1):
        super().__init__(parent)
        self.text = text
        self.level = level

    def render(self):
        """Render the header as HTML."""
        if not self.visible:
            return ""
        return f'<h{self.level}>{self.text}</h{self.level}>'