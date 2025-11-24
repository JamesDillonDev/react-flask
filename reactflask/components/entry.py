
import hashlib
from .base import BaseComponent

class Entry(BaseComponent):
    """A text entry field component."""
    def __init__(self, parent, placeholder="", value="", width=None, height=None):
        super().__init__(parent, width=width, height=height)
        self.placeholder = placeholder
        self.value = value
        self.name = f"entry_{id(self)}"
        self.parent.add_component(self)
        hash_id = hashlib.md5((self.name + str(id(self))).encode()).hexdigest()[:8]
        self.route = f"/entry_{hash_id}"
        parent.add_entry_route(self.route, self)

    def render(self):
        """Render the entry field as HTML with JS for live update."""
        if not self.visible:
            return ""
        js = f"""
        <script>
        function updateEntry_{self.name}(el) {{
            fetch('{self.route}', {{
                method: 'PUT',
                headers: {{ 'Content-Type': 'application/json' }},
                body: JSON.stringify({{ value: el.value }})
            }});
        }}
        </script>
        """
        style = 'padding:8px;font-size:16px;border-radius:4px;border:1px solid #ccc;'
        if self.width:
            style += f'width: {self.width}; '
        if self.height:
            style += f'height: {self.height}; '
        return js + f'<input type="text" name="{self.name}" value="{self.value}" placeholder="{self.placeholder}" style="{style}" oninput="updateEntry_{self.name}(this)">' 

    def vvalue(self):
        """Return the current value of the entry field."""
        return self.value
