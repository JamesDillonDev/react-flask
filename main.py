
from reactflask import FlaskNative, Header, Paragraph, Button, Entry, Toggle, Checkbox

# Initialize the app
native = FlaskNative(__name__)

# Header
heading = Header(native, text='Welcome!', level=1, width=400, height=60)
heading.grid(row=0, column=0)

# Paragraph
paragraph = Paragraph(native, text='This is a plain paragraph.', width=380, height=30)
paragraph.grid(row=1, column=0)

# Entry field
entry = Entry(native, placeholder="Type here...", width=300, height=30)
entry.grid(row=2, column=0)

# Toggle switch
toggle = Toggle(native, color="#a72828", initial=True)
toggle.grid(row=3, column=0)

# Checkbox with callback
def on_checkbox_toggle(state):
    print("Checkbox toggled. State:", state)

checkbox = Checkbox(native, label="Accept Terms", on_toggle=on_checkbox_toggle, initial=False)
checkbox.grid(row=4, column=0)

# Button with callback
def on_button_click():
    print("Button was clicked!")
    print("Entry value:", entry.value)
    print(f"Toggle is {'ON' if toggle.state else 'OFF'}")

button1 = Button(native, label='Click Me', onClick=on_button_click, color="#28a745", width=300, height=40)
button1.grid(row=2, column=1)

# Run the app
native.run(host='0.0.0.0', port=5000)