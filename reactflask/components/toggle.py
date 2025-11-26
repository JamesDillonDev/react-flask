from .switch import Switch

class Toggle(Switch):
    """A switch that toggles its state and sends updates to Python, using Switch logic."""
    def __init__(self, parent, label_on="ON", label_off="OFF", initial=False, width=None, height=None, show_state=False, color="#007bff", background=None, on_toggle=None):
        super().__init__(parent, initial=initial, width=width, height=height, color=color, on_toggle=on_toggle)
        self.label_on = label_on
        self.label_off = label_off
        self.show_state = show_state
        self.background = background
        self.label_on = label_on
        self.label_off = label_off
        self.show_state = show_state
        self.background = background

    def render(self):
        if not self.visible:
            return ""
        js = f"""
        <script>
        function toggle_{self.name}_change(el) {{
            var checked = el.checked;
            fetch('{self.route}', {{
                method: 'PUT',
                headers: {{ 'Content-Type': 'application/json' }},
                body: JSON.stringify({{ state: checked }})
            }});
        }}
        </script>
        """
        checked = "checked" if self.state else ""
        label_text = self.label_on if self.state else self.label_off if self.show_state else ""
        label_html = f'<span class="rf-toggle-label">{label_text}</span>' if label_text else ''
        # Use the new toggle-switch structure, with label text outside
        return (
            js +
            f'<label class="toggle-switch">' +
            f'<input type="checkbox" {checked} onchange="toggle_{self.name}_change(this)">' +
            '<span class="slider"></span>' +
            '</label>' +
            label_html
        )
