from .switch import Switch

class Checkbox(Switch):
    """A checkbox that syncs its state with Python, using Switch logic."""
    def __init__(self, parent, label="", initial=False, width=None, height=None, color="#007bff", on_toggle=None):
        super().__init__(parent, initial=initial, width=width, height=height, color=color, on_toggle=on_toggle)
        self.label = label

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
