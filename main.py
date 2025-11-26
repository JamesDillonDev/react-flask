from reactflask import FlaskNative, Header, Paragraph, Button, Entry, Toggle, Checkbox, Body, Footer, Nav, HeaderBar

# --- App Setup ---
native = FlaskNative(__name__, title="React Flask Full Demo")
native.background("#f0f4f8")

# --- Layout Areas ---
headerbar = HeaderBar(native)
body = Body(native)
footer = Footer(native)
nav = Nav(native)

# --- Area Backgrounds ---
headerbar._background = "#1976d2"   # Blue header
body._background = "#fff"           # White body
footer._background = "#263238"      # Dark footer
nav._background = "#e3eaf2"         # Light nav

Header(headerbar, text='React Flask Demo', level=1, width=400, height=60, color="#fff", background="#1976d2").grid(row=0, column=0, padx=8, pady=8)

Button(nav, label='Dashboard', color="#fff", background="#34495e", width=120, height=30).grid(row=0, column=0, padx=8, pady=8)
Button(nav, label='Settings', color="#fff", background="#34495e", width=120, height=30).grid(row=1, column=0, padx=8, pady=8)
Paragraph(nav, text='Navigation', width=120, color="#34495e").grid(row=2, column=0, padx=8, pady=8)

Header(body, text='Main Content', level=2, width=300, color="#263238").grid(row=0, column=0, padx=8, pady=8)
Paragraph(body, text='Welcome to the React Flask demo app. Try the interactive components below!', width=380, height=30, color="#263238").grid(row=1, column=0, padx=8, pady=8)

entry = Entry(body, placeholder="Type something...", width=300, height=30, color="#263238", background="#e3eaf2").grid(row=2, column=0, padx=8, pady=8)
toggle = Toggle(body, label_on="Enabled", label_off="Disabled", show_state=True, color="#fff", background="#43a047", initial=False).grid(row=3, column=0, padx=8, pady=8)

def on_checkbox_toggle(state):
    print("Checkbox toggled. State:", state)
Checkbox(body, label="Accept Terms", on_toggle=on_checkbox_toggle, initial=False, color="#fff", background="#43a047").grid(row=4, column=0, padx=8, pady=8)

def on_button_click():
    print("Button was clicked!")
    print("Entry value:", entry.getValue())
    print(f"Toggle is {'ON' if toggle.getState() else 'OFF'}")
Button(body, label='Submit', onClick=on_button_click, color="#fff", background="#43a047", width=200, height=40).grid(row=5, column=0, padx=8, pady=8)

# --- More Body Components ---
Header(body, text='Features', level=3, width=200, color="#1976d2").grid(row=6, column=0, padx=8, pady=8)
Paragraph(body, text='- Layout areas: header, nav, body, footer', width=320, color="#1976d2").grid(row=7, column=0, padx=8, pady=4)
Paragraph(body, text='- Interactive buttons, toggles, checkboxes, entries', width=320, color="#1976d2").grid(row=8, column=0, padx=8, pady=4)
Paragraph(body, text='- Custom backgrounds and tab title', width=320, color="#1976d2").grid(row=9, column=0, padx=8, pady=4)

Paragraph(footer, text='© 2025 React Flask Demo', width=380, height=30, color="#fff", background="#263238").grid(row=0, column=0, padx=8, pady=8)
Button(footer, label='Contact', color="#263238", background="#f0f4f8", width=120, height=30).grid(row=0, column=1, padx=8, pady=8)

Header(native, text='Direct Native Component', level=2, width=300, color="#34495e").grid(row=0, column=0, padx=8, pady=8)
Paragraph(native, text='This header is outside any layout area.', width=320, color="#34495e").grid(row=1, column=0, padx=8, pady=8)

# --- Run the app ---
native.run(host='0.0.0.0', port=5000)