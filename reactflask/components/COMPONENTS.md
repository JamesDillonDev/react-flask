# React-Flask Components Documentation

This document explains each component in the `reactflask/components` directory and their purpose within the framework.

---

## BaseComponent (`base.py`)
**Purpose:**
- Serves as the foundation for all UI components.
- Manages layout (pack/grid), visibility, and provides a `render()` method to be implemented by subclasses.

---

## Button (`button.py`)
**Purpose:**
- Represents a clickable button UI element.
- Supports custom labels, colors, and click event routing.
- Can trigger Python functions via Flask routes when clicked.

---

## Entry (`entry.py`)
**Purpose:**
- Provides a text input field for user data entry.
- Supports live updates using JavaScript and Flask routes.
- Allows retrieval of the current value entered by the user.

---

## Header (`header.py`)
**Purpose:**
- Displays text as HTML headers (`<h1>` to `<h6>`).
- Allows specification of header level and text content.

---

## Paragraph (`paragraph.py`)
**Purpose:**
- Displays text as an HTML paragraph (`<p>`).
- Used for general text content in the UI.

---

## Usage
Each component inherits from `BaseComponent` and is designed to be used within a parent container. They provide methods for layout management and rendering HTML for integration with Flask web applications.

For more details, see the docstrings in each component's source file.
