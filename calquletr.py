import tkinter as tk
import math

root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("320x520")
root.configure(bg="#1e1e1e")

expression = ""
equation = tk.StringVar()

# Display
entry = tk.Entry(root, textvariable=equation, font=('Arial', 22),
                 bg="#2d2d2d", fg="white", bd=10,
                 justify='right')
entry.grid(row=0, column=0, columnspan=4, pady=10)
entry.focus_set()  # focus for keyboard

# Functions
def press(value):
    global expression
    expression += str(value)
    equation.set(expression)

def clear():
    global expression
    expression = ""
    equation.set("")

def equal():
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

# Scientific
def sin():
    global expression
    try:
        result = math.sin(math.radians(float(expression)))
        equation.set(result)
        expression = str(result)
    except:
        equation.set("Error")
        expression = ""

def cos():
    global expression
    try:
        result = math.cos(math.radians(float(expression)))
        equation.set(result)
        expression = str(result)
    except:
        equation.set("Error")
        expression = ""

def sqrt():
    global expression
    try:
        result = math.sqrt(float(expression))
        equation.set(result)
        expression = str(result)
    except:
        equation.set("Error")
        expression = ""

# Keyboard support
def key_input(event):
    global expression
    key = event.char

    if key in "0123456789+-*/.":
        press(key)

    elif event.keysym == "Return":  # Enter
        equal()

    elif event.keysym == "BackSpace":
        expression = expression[:-1]
        equation.set(expression)

    elif event.keysym == "Escape":
        clear()

# Bind keyboard
root.bind("<Key>", key_input)

# Button style
def create_btn(text, row, col, cmd):
    tk.Button(root, text=text, command=cmd,
              width=5, height=2,
              bg="#3a3a3a", fg="white",
              font=('Arial', 14), bd=0)\
        .grid(row=row, column=col, padx=5, pady=5)

# Buttons
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('+',4,2), ('=',4,3),
]

for (text, r, c) in buttons:
    if text == "=":
        create_btn(text, r, c, equal)
    else:
        create_btn(text, r, c, lambda t=text: press(t))

# Scientific buttons
create_btn("sin", 5, 0, sin)
create_btn("cos", 5, 1, cos)
create_btn("√",   5, 2, sqrt)
create_btn("C",   5, 3, clear)

root.mainloop()