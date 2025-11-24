class BaseComponent:
    """Base class for all UI components."""
    def __init__(self, parent, width=None, height=None):
        self.parent = parent
        self.layout = None
        self.grid_info = None
        self.visible = True
        self.width = self._format_px(width)
        self.height = self._format_px(height)

    def _format_px(self, value):
        if value is None:
            return None
        if isinstance(value, (int, float)):
            return f"{value}px"
        return str(value)

    def pack(self):
        """Add component to packed layout."""
        self.layout = 'pack'
        self.parent.add_packed(self)
        return self

    def grid(self, row, column, padx=0, pady=0):
        """Add component to grid layout with optional padding."""
        self.layout = 'grid'
        self.grid_info = {'row': row, 'column': column, 'padx': padx, 'pady': pady}
        self.parent.add_grid(self, row, column)
        return self

    def show(self):
        """Show the component."""
        self.visible = True

    def hide(self):
        """Hide the component."""
        self.visible = False

    def render(self):
        """Render HTML for the component. Must be implemented by subclasses."""
        raise NotImplementedError("Subclasses must implement render()")