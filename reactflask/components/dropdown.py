from .base import BaseComponent
from flask import request

class Dropdown(BaseComponent):
    import hashlib

    def __init__(self, parent, options, value=None, onChange=None, width=None, height=None, color=None, background=None, **kwargs):
        super().__init__(parent, width=width, height=height, **kwargs)
        self.options = options
        self.value = value if value is not None else (options[0] if options else None)
        self.onChange = onChange
        self.selected = self.value
        self.color = color
        self.background = background
        self.name = f"select_{id(self)}"
        hash_id = self.hashlib.md5((self.name + str(id(self))).encode()).hexdigest()[:8]
        self.route = f"/select_{hash_id}"
        self._route_parent.add_select_route(self.route, self)

    def render(self):
        options_html = ''.join([
            f'<option value="{opt}"' + (' selected' if opt == self.selected else '') + f'>{opt}</option>'
            for opt in self.options
        ])
        extra = ""
        if self.background:
            extra += f'background-color: {self.background}; '
        if self.color:
            extra += f'color: {self.color}; '
        style = self.get_style(extra)
        js = f"""
        <script>
        function updateSelect_{self.name}(el) {{
            fetch('{self.route}', {{
                method: 'PUT',
                headers: {{ 'Content-Type': 'application/json' }},
                body: JSON.stringify({{ value: el.value }})
            }});
        }}
        </script>
        """
        return js + f'<select class="rf-dropdown" name="{self.name}" style="{style}" onchange="updateSelect_{self.name}(this)">{options_html}</select>'

    def handle_event(self, event):
        self.selected = event.get('value', self.selected)
        if self.onChange:
            self.onChange(self.selected)
