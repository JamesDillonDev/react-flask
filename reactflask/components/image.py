from .base import BaseComponent



class Image(BaseComponent):
    """A component for displaying an image from any path or URL."""
    def __init__(self, parent, src: str, alt: str = "", width: int = None, height: int = None):
        super().__init__(parent, width=width, height=height)
        self.src = src  # Can be a filename, relative path, absolute path, or URL
        self.alt = alt

    def render(self) -> str:
        style = self.get_style()
        style_attr = f' style="{style}"' if style else ''
        return f'<img src="{self.src}" alt="{self.alt}"{style_attr}/>'
