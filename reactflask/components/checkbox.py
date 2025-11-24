import hashlib
from .base import BaseComponent

class Checkbox(BaseComponent):
    """A checkbox that syncs its state with Python."""
    def __init__(self, parent, label="", initial=False, width=None, height=None, color="#007bff"):
        super().__init__(parent, width=width, height=height)
        self.state = initial
        self.label = label
        self.color = color
        self.name = f"checkbox_{id(self)}"
        self.parent.add_component(self)
        hash_id = hashlib.md5((self.name + str(id(self))).encode()).hexdigest()[:8]
        self.route = f"/checkbox_{hash_id}"
        parent.add_checkbox_route(self.route, self)

    def render(self):
        if not self.visible:
            return ""
        js = f"""
        <script>
        function checkbox_{self.name}_change(el) {{
            var checked = el.checked;
            fetch('{self.route}', {{
                method: 'PUT',
                headers: {{ 'Content-Type': 'application/json' }},
                body: JSON.stringify({{ state: checked }})
            }});
        }}
        </script>
        """
        style = f'width:18px;height:18px;accent-color:{self.color};vertical-align:middle;'
        checked = "checked" if self.state else ""
        label_html = f'<label style="font-size:17px;font-family:Arial,Helvetica,sans-serif;color:#34495e;line-height:1.6;margin-left:8px;">{self.label}</label>' if self.label else ''
        return (
            js +
            f'<input type="checkbox" style="{style}" {checked} onchange="checkbox_{self.name}_change(this)">' +
            label_html
        )

    def vstate(self):
        """Return the current checkbox state."""
        return self.state
