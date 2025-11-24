from reactflask import FlaskNative, Header, Paragraph, Button, Entry

# Example usage
native = FlaskNative(__name__)


# Example usage with grid layout and custom padx/pady
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