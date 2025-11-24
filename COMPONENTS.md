
# React-Flask Components Documentation

This document explains each component in the `reactflask/components` directory, their flags (arguments/properties), and layout options.

---

## Layout Types
- **pack**: Adds the component in sequence (vertical stack). Use `component.pack()`.
- **grid**: Places the component in a table-like grid. Use `component.grid(row, column, padx=0, pady=0)`.

---

## Component Flags

### BaseComponent (`base.py`)
**Flags:**
- `parent`: Parent container (required)
- `width`: Width (e.g., `"300px"` or `300`)
- `height`: Height (e.g., `"40px"` or `40`)
- Methods: `.pack()`, `.grid(row, column, padx=0, pady=0)`, `.show()`, `.hide()`

---

### Button (`button.py`)
**Flags:**
- `parent`: Parent container (required)
- `label`: Button text
- `onClick`: Python function to call on click
- `color`: Button background color (default: `"#007bff"`)
- `width`: Width
- `height`: Height

---

### Entry (`entry.py`)
**Flags:**
- `parent`: Parent container (required)
- `placeholder`: Placeholder text
- `value`: Initial value
- `width`: Width
- `height`: Height

---

### Header (`header.py`)
**Flags:**
- `parent`: Parent container (required)
- `text`: Header text
- `level`: Header level (`1` to `6`, default: `1`)
- `width`: Width
- `height`: Height

---

### Paragraph (`paragraph.py`)
**Flags:**
- `parent`: Parent container (required)
- `text`: Paragraph text
- `width`: Width
- `height`: Height

---

## Usage
Each component inherits from `BaseComponent` and is designed to be used within a parent container. They provide methods for layout management and rendering HTML for integration with Flask web applications.

For more details, see the docstrings in each component's source file.
