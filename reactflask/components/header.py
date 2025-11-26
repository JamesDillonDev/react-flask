from .base import BaseComponent

class Header(BaseComponent):
    """A header component (h1-h6)."""
    def __init__(self, parent, text, level=1, width=None, height=None, color=None, background=None):
        super().__init__(parent, width=width, height=height)
        self.text = text
        self.level = level
        self.color = color
        self.background = background

    def render(self):
        """Render the header as HTML with styling."""
        if not self.visible:
            return ""
        extra = ""
        if self.background:
            extra += f'background-color: {self.background}; '
        if self.color:
            extra += f'color: {self.color}; '
        style = self.get_style(extra)
        return f'<h{self.level} class="rf-header" style="{style}">{self.text}</h{self.level}>'