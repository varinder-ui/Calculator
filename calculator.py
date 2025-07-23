from tkinter import *

def press_1():
    print("1")
    entry.insert(END, "1")

def press_2():
    entry.insert(END, "2")

def press_3():
    entry.insert(END, "3")

def press_4():
    entry.insert(END, "4")

def press_5():
    entry.insert(END, "5")

def press_6():
    entry.insert(END, "6")

def press_7():
    entry.insert(END, "7")

def press_8():
    entry.insert(END, "8")

def press_9():
    entry.insert(END, "9")

def press_0():
    entry.insert(END, "0")

def press_dot():
    entry.insert(END, ".")

def press_add():
    entry.insert(END, "+")

def press_subtract():
    entry.insert(END, "-")

def press_multiply():
    entry.insert(END, "*")

def press_divide():
    entry.insert(END, "/")

def press_percent():
    entry.insert(END, "%")

def press_negate():
    content = entry.get()
    if content.startswith('-'):
        entry.delete(0, END)
        entry.insert(END, content[1:])
    else:
        entry.delete(0, END)
        entry.insert(END, '-' + content)


def clear():
    entry.delete(0, END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(END, str(result))
    except:
        entry.delete(0, END)
        entry.insert(END, "Error")

root = Tk()
root.title("SImple Iphone Style Calculator")
root.geometry("500x600")
entry = Entry(root, font=("Arial", 24), bd=10, relief=RIDGE, justify=RIGHT)
entry.grid(row=0, column=0, columnspan=4, pady=10)

btn_ac = Button(root, text="AC" , width=5, height=2, font=("Arial", 14), command=clear)
btn_ac.grid(row=1, column=0)

btn_plus_minus = Button(root, text="+/-", width=5, height=2, font=("Arial", 14), command=press_negate)
btn_plus_minus.grid(row=1, column=1)

btn_percent = Button(root, text='%', width=5, height=2, font=("Arial", 14), command=press_percent)
btn_percent.grid(row=1,column=2)

btn_divide = Button(root, text='/', width=5, height=2, font=("Arial", 14), command=press_divide)
btn_divide.grid(row=1,column=3)

btn_7 = Button(root, text="7", width = 5, height=2, font=("Arial", 14),command=press_7)
btn_7.grid(row=2,column=0)

btn_8 = Button(root, text="8", width=5, height=2, font=("Arial", 14), command=press_8)
btn_8.grid(row=2,column=1)

btn_9 = Button(root, text="9", width=5, height=2, font=("Arial", 14), command=press_9)
btn_9.grid(row=2,column=2)

btn_multiply = Button(root, text="*", width=5, height=2, font=("Arial", 14), command=press_multiply)
btn_multiply.grid(row=2,column=3)

btn_4 = Button(root, text='4', width=5, height=2, font=("Arial", 14), command=press_4)
btn_4.grid(row=3,column=0)

btn_5 = Button(root, text='5', width=5, height=2, font=("Arial", 14), command=press_5)
btn_5.grid(row=3,column=1)

btn_6 = Button(root, text='6', width=5, height=2, font=("Arial", 14), command=press_6)
btn_6.grid(row=3,column=2)

btn_minus = Button(root, text="-", width=5, height=2, font=("Arial", 14), command=press_subtract)
btn_minus.grid(row=3,column=3)

btn_1 = Button(root, text="1", width=5, height=2, font=("Arial", 14), command=press_1)
btn_1.grid(row=4,column=0)

btn_2 = Button(root, text="2", width=5, height=2, font=("Arial", 14), command=press_2)
btn_2.grid(row=4,column=1)

btn_3 = Button(root, text="3", width=5, height=2, font=("Arial", 14), command=press_3)
btn_3.grid(row=4,column=2)

btn_plus = Button(root, text="+", width=5, height=2, font=("Arial", 14), command=press_add)
btn_plus.grid(row=4, column=3)

btn_0 = Button(root, text="0", width=5, height=2, font=("Arial", 14), command=press_0)
btn_0.grid(row=5,column=0,columnspan=2)

btn_dot = Button(root, text=".", width=5, height=2, font=("Arial", 14), command=press_dot)
btn_dot.grid(row=5,column=2)

btn_equal = Button(root, text="=", width=5, height=2, font=("Arial", 14), command=calculate)
btn_equal.grid(row=5,column=3)

root.mainloop()