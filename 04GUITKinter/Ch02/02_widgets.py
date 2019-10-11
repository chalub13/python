
# widgets.py by Marco Chalub
# This is an exercise file from Python GUI Development with Tkinter

from tkinter import *
from tkinter import ttk

root = Tk()

button = ttk.Button(root, text = 'Click Me')
button.pack()

print(button['text'])
button['text'] = 'Press Me'
button.config(text = 'Push Me')
print(button.config())

print(str(button))
print(str(root))

ttk.Label(root, text ='Hello, Tkinter!').pack()

# mainloop() add
root.mainloop()
