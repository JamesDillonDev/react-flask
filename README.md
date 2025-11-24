
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
from reactflask import FlaskNative, Header, Paragraph, Button, Entry

native = FlaskNative(__name__)

heading = Header(native, text='Welcome!', level=1, width=400, height=60)
heading.grid(row=0, column=0)

paragraph = Paragraph(native, text='This is a plain paragraph.', width=380, height=30)
paragraph.grid(row=1, column=0)

entry = Entry(native, placeholder="Type here...", width=300, height=30)
entry.grid(row=2, column=0)

def on_button_click():
	 print("Button was clicked!")
	 print(entry.value)

button1 = Button(native, label='Click Me', onClick=on_button_click, color="#28a745", width=300, height=40)
button1.grid(row=2, column=1)

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
