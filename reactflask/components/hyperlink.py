from .base import BaseComponent

class Hyperlink(BaseComponent):
    """A component for rendering a hyperlink."""
    def __init__(self, parent, text, href, color=None, underline=True, width=None, height=None):
        super().__init__(parent, width=width, height=height)
        self.text = text
        self.href = href
        self.color = color
        self.underline = underline

    def render(self):
        style = self.get_style()
        if self.color:
            style += f'color: {self.color};'
        if not self.underline:
            style += 'text-decoration: none;'
        return f'<a href="{self.href}" style="{style}">{self.text}</a>'
