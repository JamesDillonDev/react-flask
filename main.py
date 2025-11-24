from reactflask import FlaskNative, Header, Paragraph, Button, Entry

# Example usage
native = FlaskNative(__name__)

heading = Header(native, text='Welcome!', level=1)
heading.pack()


paragraph = Paragraph(native, text='This is a paragraph.')
paragraph.pack()

# Example Entry usage
entry = Entry(native, placeholder="Type here...")
entry.pack()

def on_button_click():
    print("Button was clicked!")
    print(entry.value)
    
button1 = Button(native, label='Click Me', onClick=on_button_click, color="#28a745")
button1.pack()

native.run(host='0.0.0.0', port=5000)