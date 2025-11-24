class BaseComponent:
    """Base class for all UI components."""
    def __init__(self, parent):
        self.parent = parent
        self.layout = None
        self.grid_info = None
        self.visible = True

    def pack(self):
        """Add component to packed layout."""
        self.layout = 'pack'
        self.parent.add_packed(self)
        return self

    def grid(self, row, column):
        """Add component to grid layout."""
        self.layout = 'grid'
        self.grid_info = {'row': row, 'column': column}
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