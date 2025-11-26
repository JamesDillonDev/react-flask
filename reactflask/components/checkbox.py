from .switch import Switch

class Checkbox(Switch):
    """A checkbox that syncs its state with Python, using Switch logic."""
    def __init__(self, parent, label="", initial=False, width=None, height=None, color="#007bff", background=None, on_toggle=None):
        super().__init__(parent, initial=initial, width=width, height=height, color=color, on_toggle=on_toggle)
        self.label = label
        self.background = background

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
        extra = ""
        if self.background:
            extra += f'background-color: {self.background}; '
        if self.color:
            extra += f'color: {self.color}; '
        style = self.get_style(extra)
        checked = "checked" if self.state else ""
        label_html = f'<label class="rf-checkbox-label">{self.label}</label>' if self.label else ''
        return (
            js +
            f'<input type="checkbox" class="rf-checkbox" style="{style}" {checked} onchange="checkbox_{self.name}_change(this)">' +
            label_html
        )
