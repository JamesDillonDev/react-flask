
from .base import BaseComponent

class Paragraph(BaseComponent):
    """A paragraph component."""
    def __init__(self, parent, text, width=None, height=None):
        super().__init__(parent, width=width, height=height)
        self.text = text

    def render(self):
        """Render the paragraph as HTML with styling."""
        if not self.visible:
            return ""
        style = (
            'margin: 12px 0; '
            'font-family: Arial, Helvetica, sans-serif; '
            'font-size: 17px; '
            'color: #34495e; '
            'line-height: 1.6; '
        )
        if self.width:
            style += f'width: {self.width}; '
        if self.height:
            style += f'height: {self.height}; '
        return f'<p style="{style}">{self.text}</p>'
