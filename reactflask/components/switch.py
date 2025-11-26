import hashlib
from .base import BaseComponent

class Switch(BaseComponent):
    """A generic switch component with toggle logic."""
    def __init__(self, parent, initial=False, width=None, height=None, color="#007bff", background=None, on_toggle=None):
        super().__init__(parent, width=width, height=height)
        self.state = initial
        self.color = color
        self.background = background
        self.on_toggle = on_toggle
        self.name = f"switch_{id(self)}"
        hash_id = hashlib.md5((self.name + str(id(self))).encode()).hexdigest()[:8]
        self.route = f"/switch_{hash_id}"
        self._route_parent.add_switch_route(self.route, self)

    def toggle(self, new_state=None):
        if new_state is not None:
            self.state = new_state
        else:
            self.state = not self.state
        if self.on_toggle:
            self.on_toggle(self.state)

    def render(self):
        if not self.visible:
            return ""
        js = f"""
        <script>
        function switch_{self.name}_change(el) {{
            var checked = el.checked;
            fetch('{self.route}', {{
                method: 'PUT',
                headers: {{ 'Content-Type': 'application/json' }},
                body: JSON.stringify({{ state: checked }})
            }});
        }}
        </script>
        """
        extra = ""
        if self.background:
            extra += f'background-color: {self.background}; '
        if self.color:
            extra += f'color: {self.color}; '
        style = self.get_style(extra)
        checked = "checked" if self.state else ""
        label_html = f'<label class="rf-switch-label">{self.label}</label>' if self.label else ''
        return (
            js +
            f'<input type="checkbox" class="rf-switch" style="{style}" {checked} onchange="switch_{self.name}_change(this)">' +
            label_html
        )
