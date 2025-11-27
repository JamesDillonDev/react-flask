
# react-flask

A lightweight Python + Flask project that provides a simple component-based rendering system for building dynamic HTML pages.

---

## Features
- Component-based UI: Button, Entry, Header, Paragraph
- Dynamic HTML rendering with Python
- Live updates for input fields
- Customizable layout: pack (vertical stack) and grid (table)

---

## Components & Flags

### BaseComponent
- `parent`: Parent container (required)
- `width`: Width (e.g., `"300px"` or `300`)
- `height`: Height (e.g., `"40px"` or `40`)
- Methods: `.pack()`, `.grid(row, column, padx=0, pady=0)`, `.show()`, `.hide()`

### Button
- `parent`: Parent container (required)
- `label`: Button text
- `onClick`: Python function to call on click
- `color`: Button background color (default: `"#007bff"`)
- `width`: Width
- `height`: Height

### Entry
- `parent`: Parent container (required)
- `placeholder`: Placeholder text
- `value`: Initial value
- `width`: Width
- `height`: Height

### Header
- `parent`: Parent container (required)
- `text`: Header text
- `level`: Header level (`1` to `6`, default: `1`)
- `width`: Width
- `height`: Height

### Paragraph
- `parent`: Parent container (required)
- `text`: Paragraph text
- `width`: Width
- `height`: Height

---

## Layout Options
- **pack**: Adds the component in sequence (vertical stack). Use `component.pack()`.
- **grid**: Places the component in a table-like grid. Use `component.grid(row, column, padx=0, pady=0)`.

---

## Example Usage
```python
from reactflask import FlaskNative, Header, Paragraph, Button, Entry, Toggle, Checkbox, Image, Hyperlink

native = FlaskNative(__name__)

headerbar = HeaderBar(native)
nav = Nav(native)
footer = Footer(native)
body_home = Body(native, route="/")

# Shared layout components
demo_header = Header(headerbar, text='Demo', level=1, color="#fff", background="#1976d2")
demo_header.grid(row=0, column=0)

home_button = Button(nav, label='Home', color="#fff", background="#34495e", width=120, height=30, onClick=Redirect("/"))
home_button.grid(row=0, column=0)

about_button = Button(nav, label='About', color="#fff", background="#34495e", width=120, height=30, onClick=Redirect("/about"))
about_button.grid(row=0, column=1)

footer_paragraph = Paragraph(footer, text='© 2025 React Flask Demo', color="#fff", background="#263238")
footer_paragraph.grid(row=0, column=0)

# Home page components
main_header = Header(body_home, text='Main Content', level=2, color="#263238")
main_header.grid(row=0, column=0)

welcome_paragraph = Paragraph(body_home, text='Welcome to the demo app!', color="#263238")
welcome_paragraph.grid(row=1, column=0)

click_me_button = Button(body_home, label='Click Me', onClick=lambda: print('Clicked!'), color="#fff", background="#34495e")
click_me_button.grid(row=2, column=0)

entry_field = Entry(body_home, placeholder="Type here...")
entry_field.grid(row=3, column=0)

toggle_switch = Toggle(body_home, label_on="On", label_off="Off", show_state=True, color="#fff", background="#43a047")
toggle_switch.grid(row=4, column=0)

terms_checkbox = Checkbox(body_home, label="Accept Terms", color="#fff", background="#43a047")
terms_checkbox.grid(row=5, column=0)

logo_image = Image(body_home, src="https://upload.wikimedia.org/wikipedia/commons/a/a7/React-icon.svg", alt="Logo", width=100, height=100)
logo_image.grid(row=6, column=0)

example_link = Hyperlink(body_home, text="Visit Example", href="https://www.example.com", color="#1976d2")
example_link.grid(row=7, column=0)

native.run(host='0.0.0.0', port=5000)
```

---

## Running the App
1. Install dependencies:
	```bash
	pip install flask
	```
2. Run the app:
	```bash
	python main.py
	```
3. Open your browser to `http://localhost:5000`

---

## License
See `LICENSE` for details.
