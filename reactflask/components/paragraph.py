
from .base import BaseComponent

class Paragraph(BaseComponent):
    """A paragraph component."""
    def __init__(self, parent, text):
        super().__init__(parent)
        self.text = text

    def render(self):
        """Render the paragraph as HTML."""
        if not self.visible:
            return ""
        return f'<p>{self.text}</p>'
