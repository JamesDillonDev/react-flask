from .base import BaseComponent

class Header(BaseComponent):
    """A header component (h1-h6)."""
    def __init__(self, parent, text, level=1, width=None, height=None):
        super().__init__(parent, width=width, height=height)
        self.text = text
        self.level = level

    def render(self):
        """Render the header as HTML with styling."""
        if not self.visible:
            return ""
        style = (
            'margin: 16px 0; '
            'font-family: Arial, Helvetica, sans-serif; '
            'font-weight: bold; '
            'color: #2c3e50; '
        )
        if self.width:
            style += f'width: {self.width}; '
        if self.height:
            style += f'height: {self.height}; '
        return f'<h{self.level} style="{style}">{self.text}</h{self.level}>'