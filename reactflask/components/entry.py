
import hashlib
from .base import BaseComponent

class Entry(BaseComponent):
    """A text entry field component."""
    def __init__(self, parent, placeholder="", value="", width=None, height=None, color=None, background=None):
        super().__init__(parent, width=width, height=height)
        self.placeholder = placeholder
        self.value = value
        self.color = color
        self.background = background
        self.name = f"entry_{id(self)}"
        hash_id = hashlib.md5((self.name + str(id(self))).encode()).hexdigest()[:8]
        self.route = f"/entry_{hash_id}"
        self._route_parent.add_entry_route(self.route, self)

    def setValue(self, new_value):
        self.value = new_value
        # Emit SocketIO event to update the UI
        if hasattr(self._route_parent, 'socketio'):
            self._route_parent.socketio.emit(f'entry_update_{self.name}', {'value': new_value})

    def render(self):
        """Render the entry field as HTML with JS for live update and SocketIO sync."""
        if not self.visible:
            return ""
        js = f"""
        <script src="https://cdn.socket.io/4.5.4/socket.io.min.js"></script>
        <script>
        var socket = window.reactflask_socketio || io();
        window.reactflask_socketio = socket;
        function updateEntry_{self.name}(el) {{
            fetch('{self.route}', {{
                method: 'PUT',
                headers: {{ 'Content-Type': 'application/json' }},
                body: JSON.stringify({{ value: el.value }})
            }});
        }}
        socket.on('entry_update_{self.name}', function(data) {{
            var entry = document.getElementsByName('{self.name}')[0];
            if (entry) {{ entry.value = data.value; }}
        }});
        </script>
        """
        extra = ""
        if self.background:
            extra += f'background-color: {self.background}; '
        if self.color:
            extra += f'color: {self.color}; '
        style = self.get_style(extra)
        return js + f'<input type="text" class="rf-entry" name="{self.name}" value="{self.value}" placeholder="{self.placeholder}" style="{style}" oninput="updateEntry_{self.name}(this)">'

    def getValue(self):
        """Return the current value of the entry field."""
        return self.value
