
from .base import BaseComponent

class Paragraph(BaseComponent):
    """A paragraph component."""
    def __init__(self, parent, text, width=None, height=None, color=None, background=None):
        super().__init__(parent, width=width, height=height)
        self.text = text
        self.color = color
        self.background = background

    def render(self):
        """
        Render the paragraph as HTML with styling.
        """
        if not self.visible:
            return ""
        extra = ""
        if self.background:
            extra += f'background-color: {self.background}; '
        if self.color:
            extra += f'color: {self.color}; '
        style = self.get_style(extra)
        return f'<p class="rf-paragraph" style="{style}">{self.text}</p>'
