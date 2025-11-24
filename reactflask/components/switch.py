import hashlib
from .base import BaseComponent

class Switch(BaseComponent):
    """A generic switch component with toggle logic."""
    def __init__(self, parent, initial=False, width=None, height=None, color="#007bff", on_toggle=None):
        super().__init__(parent, width=width, height=height)
        self.state = initial
        self.color = color
        self.on_toggle = on_toggle
        self.name = f"switch_{id(self)}"
        self.parent.add_component(self)
        hash_id = hashlib.md5((self.name + str(id(self))).encode()).hexdigest()[:8]
        self.route = f"/switch_{hash_id}"
        parent.add_switch_route(self.route, self)

    def toggle(self, new_state=None):
        if new_state is not None:
            self.state = new_state
        else:
            self.state = not self.state
        if self.on_toggle:
            self.on_toggle(self.state)

    def vstate(self):
        """Return the current switch state."""
        return self.state

    def render(self):
        raise NotImplementedError("Subclasses must implement render() for styling.")
