from tkinter import *

root = Tk()
root.title("Calculator")
entry = Entry(root, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=3, padx=1, pady=1)


def click(number):
    val = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(val) + str(number))


def clear():
    entry.delete(0, END)


def add():
    global operator
    global num_1
    operator = "sum"
    num_1 = float(entry.get())
    entry.delete(0, END)


def subtract():
    global operator
    global num_1
    operator = "diff"
    num_1 = float(entry.get())
    entry.delete(0, END)


def multiply():
    global operator
    global num_1
    operator = "product"
    num_1 = float(entry.get())
    entry.delete(0, END)


def divide():
    global operator
    global num_1
    operator = "div"
    num_1 = float(entry.get())
    entry.delete(0, END)


def equal():
    num_2 = float(entry.get())
    entry.delete(0, END)
    if operator == "sum":
        entry.insert(0, num_1 + num_2)
    elif operator == "diff":
        entry.insert(0, num_1 - num_2)
    elif operator == "product":
        entry.insert(0, num_1 * num_2)
    elif operator == "div":
        entry.insert(0, num_1 / num_2)


# Set buttons
btn_1 = Button(root, text="1", padx=40, pady=20, command=lambda: click(1))
btn_2 = Button(root, text="2", padx=40, pady=20, command=lambda: click(2))
btn_3 = Button(root, text="3", padx=40, pady=20, command=lambda: click(3))
btn_4 = Button(root, text="4", padx=40, pady=20, command=lambda: click(4))
btn_5 = Button(root, text="5", padx=40, pady=20, command=lambda: click(5))
btn_6 = Button(root, text="6", padx=40, pady=20, command=lambda: click(6))
btn_7 = Button(root, text="7", padx=40, pady=20, command=lambda: click(7))
btn_8 = Button(root, text="8", padx=40, pady=20, command=lambda: click(8))
btn_9 = Button(root, text="9", padx=40, pady=20, command=lambda: click(9))
btn_0 = Button(root, text="0", padx=40, pady=20, command=lambda: click(0))

btn_add = Button(root, text="+", padx=38, pady=20, command=add)
btn_sub = Button(root, text="-", padx=38, pady=20, command=subtract)
btn_mul = Button(root, text="*", padx=38, pady=20, command=multiply)
btn_div = Button(root, text="/", padx=38, pady=20, command=divide)
btn_eq = Button(root, text="=", padx=40, pady=20, command=equal)
btn_clr = Button(root, text="Clear", padx=30, pady=20, command=clear)

# Set grid
btn_1.grid(row=3, column=0)
btn_2.grid(row=3, column=1)
btn_3.grid(row=3, column=2)

btn_4.grid(row=2, column=0)
btn_5.grid(row=2, column=1)
btn_6.grid(row=2, column=2)

btn_7.grid(row=1, column=0)
btn_8.grid(row=1, column=1)
btn_9.grid(row=1, column=2)

btn_0.grid(row=4, column=0)
btn_clr.grid(row=4, column=1)
btn_eq.grid(row=4, column=2)
btn_add.grid(row=1, column=3)
btn_sub.grid(row=2, column=3)
btn_mul.grid(row=3, column=3)
btn_div.grid(row=4, column=3)


root.mainloop()
