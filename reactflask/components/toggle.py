import hashlib
from .base import BaseComponent

class Toggle(BaseComponent):
    """A switch that toggles its state and sends updates to Python."""
    def __init__(self, parent, label_on="ON", label_off="OFF", initial=False, width=None, height=None, show_state=False, color="#007bff"):
        super().__init__(parent, width=width, height=height)
        self.state = initial
        self.label_on = label_on
        self.label_off = label_off
        self.show_state = show_state
        self.color = color
        self.name = f"toggle_{id(self)}"
        self.parent.add_component(self)
        hash_id = hashlib.md5((self.name + str(id(self))).encode()).hexdigest()[:8]
        self.route = f"/toggle_{hash_id}"
        parent.add_toggle_route(self.route, self)

    def render(self):
        if not self.visible:
            return ""
        js = f"""
        <script>
        function toggle_{self.name}(el) {{
            var slider = el.querySelector('.slider');
            var knob = el.querySelector('.slider-knob');
            var label = el.querySelector('.switch-label');
            var state = el.getAttribute('data-state') === 'true';
            var newState = !state;
            el.setAttribute('data-state', newState);
            // Animate knob
            if (newState) {{
                slider.classList.add('active');
                knob.classList.add('active');
                if(label) label.innerText = '{self.label_on}';
            }} else {{
                slider.classList.remove('active');
                knob.classList.remove('active');
                if(label) label.innerText = '{self.label_off}';
            }}
            fetch('{self.route}', {{
                method: 'PUT',
                headers: {{ 'Content-Type': 'application/json' }},
                body: JSON.stringify({{ state: newState }})
            }}).then(() => {{
                // Optionally update Python-side state after confirmation
            }});
        }}
        window.addEventListener('DOMContentLoaded', function() {{
            var el = document.querySelector('[data-toggle-id="{self.name}"]');
            if (el) {{
                var slider = el.querySelector('.slider');
                var knob = el.querySelector('.slider-knob');
                var label = el.querySelector('.switch-label');
                var state = el.getAttribute('data-state') === 'true';
                if (state) {{
                    slider.classList.add('active');
                    knob.classList.add('active');
                    if(label) label.innerText = '{self.label_on}';
                }} else {{
                    slider.classList.remove('active');
                    knob.classList.remove('active');
                    if(label) label.innerText = '{self.label_off}';
                }}
            }}
        }});
        </script>
        """
        switch_css = f'''<style>
        .switch-container {{ display: inline-flex; align-items: center; cursor: pointer; user-select: none; }}
        .slider {{ position: relative; width: 50px; height: 28px; background: #ccc; border-radius: 14px; transition: background 0.3s; }}
        .slider-knob {{ position: absolute; top: 2px; left: 2px; width: 24px; height: 24px; background: #fff; border-radius: 50%; box-shadow: 0 1px 4px rgba(0,0,0,0.2); transition: left 0.3s; }}
        .slider.active {{ background: {self.color}; }}
        .slider-knob.active {{ left: 24px; }}
        .switch-label {{ margin-left: 12px; font-size: 17px; font-family: Arial, Helvetica, sans-serif; color: #34495e; line-height: 1.6; min-width: 32px; text-align: left; }}
        </style>'''
        state = 'true' if self.state else 'false'
        label = self.label_on if self.state else self.label_off
        slider_active = 'active' if self.state else ''
        knob_active = 'active' if self.state else ''
        label_html = f'<span class="switch-label">{label}</span>' if self.show_state else ''
        return (
            switch_css + js +
            f'<span class="switch-container" data-toggle-id="{self.name}" data-state="{state}" onclick="toggle_{self.name}(this)">' +
            f'<span class="slider {slider_active}">' +
            f'<span class="slider-knob {knob_active}"></span>' +
            f'</span>' +
            label_html +
            f'</span>'
        )

    def vstate(self):
        """Return the current toggle state."""
        return self.state
