class BaseComponent:
    """
    Base class for all UI components.
    Handles layout, visibility, and style logic.
    """

    def __init__(self, parent, width=None, height=None):
        self.parent = parent
        self.layout = None
        self.grid_info = None
        self.visible = True
        self.width = self._format_px(width)
        self.height = self._format_px(height)
        # If parent is a LayoutArea, use its app for route registration
        self._route_parent = getattr(parent, 'app', parent)

    def _format_px(self, value):
        """
        Format a value as px if int/float, else return as string.
        """
        if value is None:
            return None
        if isinstance(value, (int, float)):
            return f"{value}px"
        return str(value)

    def get_style(self, extra=None):
        """
        Return inline style string for width/height and any extra styles.
        """
        style = ""
        if self.width:
            style += f'width: {self.width}; '
        if self.height:
            style += f'height: {self.height}; '
        if extra:
            style += extra
        return style

    def pack(self):
        """
        Add component to packed layout.
        """
        self.layout = 'pack'
        self.parent.add_packed(self)
        return self

    def grid(self, row, column, padx=0, pady=0):
        """
        Add component to grid layout with optional padding.
        """
        self.layout = 'grid'
        self.grid_info = {'row': row, 'column': column, 'padx': padx, 'pady': pady}
        self.parent.add_grid(self, row, column)
        return self

    def show(self):
        """
        Show the component.
        """
        self.visible = True

    def hide(self):
        """
        Hide the component.
        """
        self.visible = False

    def render(self):
        """
        Render HTML for the component. Must be implemented by subclasses.
        Always return a string, never None.
        """
        return ""  # Default: subclasses should override