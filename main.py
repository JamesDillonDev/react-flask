from reactflask import FlaskNative, Header, Paragraph, Button, Entry, Toggle, Checkbox, Body, Footer, Nav, HeaderBar, Image, Redirect

# --- App Setup ---
native = FlaskNative(__name__)
native.setTitle("React Flask Full Demo")
native.background("#f0f4f8")

# --- Layout Areas ---
headerbar = HeaderBar(native)
body_home = Body(native, route="/")
body_about = Body(native, route="/about")
body_all = Body(native, route="/all-components")
footer = Footer(native)
nav = Nav(native)

# --- Area Backgrounds ---
headerbar._background = "#1976d2"   # Blue header
body_home._background = "#fff"      # White home body
body_about._background = "#f9f9f9"  # Light about body
footer._background = "#263238"      # Dark footer
nav._background = "#e3eaf2"         # Light nav


# --- Shared Components ---
Header(headerbar, text='React Flask Demo', level=1, width=400, height=60, color="#fff", background="#1976d2").grid(row=0, column=0, padx=8, pady=8)
Button(nav, label='Home', color="#fff", background="#34495e", width=120, height=30, onClick=Redirect("/")).grid(row=0, column=0, padx=15, pady=8)
Button(nav, label='About', color="#fff", background="#34495e", width=120, height=30, onClick=Redirect("/about")).grid(row=0, column=1, padx=15, pady=8)
Button(nav, label='All Components', color="#fff", background="#34495e", width=300, height=30, onClick=Redirect("/all-components")).grid(row=0, column=2, padx=15, pady=8)

Paragraph(footer, text='© 2025 React Flask Demo', width=380, height=30, color="#fff", background="#263238").grid(row=0, column=0, padx=8, pady=8)
Button(footer, label='Contact', color="#263238", background="#f0f4f8", width=120, height=30).grid(row=0, column=1, padx=8, pady=8)

# --- Home Body Components ---
Image(body_home, src="https://upload.wikimedia.org/wikipedia/commons/a/a7/React-icon.svg", alt="React Logo", width=100, height=100).grid(row=2, column=0, columnspan=2, padx=8, pady=8)
entry_obj = Entry(body_home, placeholder="Type something...", width=300, height=30, color="#263238", background="#e3eaf2")
entry_obj.grid(row=3, column=0, padx=8, pady=16)

def set_entry_value():
    entry_obj.setValue("Hello from button!")

Button(body_home, label='Set Entry Value', onClick=set_entry_value, color="#fff", background="#34495e", width=200, height=40).grid(row=3, column=1, padx=8, pady=16)

toggle = Toggle(body_home, label_on="Enabled", label_off="Disabled", show_state=True, color="#fff", background="#43a047", initial=False)
toggle.grid(row=4, column=0, padx=8, pady=8)

def on_checkbox_toggle(state):
    print("Checkbox toggled. State:", state)

Checkbox(body_home, label="Accept Terms", on_toggle=on_checkbox_toggle, initial=False, color="#fff", background="#43a047").grid(row=4, column=1, padx=8, pady=8)

def on_button_click():
    print("Button was clicked!")
    print("Entry value:", entry_obj.getValue())
    print(f"Toggle is {'ON' if toggle.state else 'OFF'}")

Button(body_home, label='Submit', onClick=on_button_click, color="#fff", background="#43a047", width=200, height=40).grid(row=5, column=0, columnspan=2, padx=8, pady=8)
Header(body_home, text='Features', level=3, width=200, color="#1976d2").grid(row=6, column=0, columnspan=2, padx=8, pady=8)

Paragraph(body_home, text='- Layout areas: header, nav, body, footer', width=320, color="#1976d2").grid(row=7, column=0, columnspan=2, padx=8, pady=4)
Paragraph(body_home, text='- Interactive buttons, toggles, checkboxes, entries', width=320, color="#1976d2").grid(row=8, column=0, columnspan=2, padx=8, pady=4)
Paragraph(body_home, text='- Custom backgrounds and tab title', width=320, color="#1976d2").grid(row=9, column=0, columnspan=2, padx=8, pady=4)


# --- About Body Components ---
Header(body_about, text='About Page', level=2, width=300, color="#263238").grid(row=0, column=0, columnspan=2, padx=8, pady=8)
Paragraph(body_about, text='This is the about page. You can add more components here.', width=380, height=30, color="#263238").grid(row=1, column=0, columnspan=2, padx=8, pady=8)
Image(body_about, src="https://upload.wikimedia.org/wikipedia/commons/4/4a/Logo_2013_Google.png", alt="Google Logo", width=100, height=100).grid(row=2, column=0, columnspan=2, padx=8, pady=8)

# --- All Components Example Page ---
from reactflask import Hyperlink, Redirect
Header(body_all, text='All Components Example', level=2, width=400, color="#34495e").grid(row=0, column=0, columnspan=2, padx=8, pady=12)
Paragraph(body_all, text='This page demonstrates every available component in React Flask.', width=400, color="#263238").grid(row=1, column=0, columnspan=2, padx=8, pady=8)
Button(body_all, label='Button Example', color="#fff", background="#34495e", width=200, height=40, onClick=lambda: print('Button clicked!')).grid(row=2, column=0, columnspan=2, padx=8, pady=8)
Entry(body_all, placeholder="Entry Example", width=300, height=30, color="#263238", background="#e3eaf2").grid(row=3, column=0, columnspan=2, padx=8, pady=8)
Toggle(body_all, label_on="On", label_off="Off", show_state=True, color="#fff", background="#43a047", initial=True).grid(row=4, column=0, columnspan=2, padx=8, pady=8)
Checkbox(body_all, label="Checkbox Example", initial=True, color="#fff", background="#43a047").grid(row=5, column=0, columnspan=2, padx=8, pady=8)
Image(body_all, src="https://upload.wikimedia.org/wikipedia/commons/a/a7/React-icon.svg", alt="Image Example", width=100, height=100).grid(row=6, column=0, columnspan=2, padx=8, pady=8)
Hyperlink(body_all, text="Hyperlink Example", href="https://www.example.com", color="#1976d2").grid(row=7, column=0, columnspan=2, padx=8, pady=8)

# --- Run the app ---
native.run(host='0.0.0.0', port=5000)