from tkinter import *


def button_press(num):
    global equation_text

    equation_text = equation_text + str(num)
    equation_label.set(equation_text)


def equals():
    global equation_text

    try:
        total = str(eval(equation_text))

        equation_label.set(total)
        equation_text = total
    except SyntaxError:
        equation_label.set("syntax error")
        equation_text = ""
    except ZeroDivisionError:
        equation_label.set("arithmetic error")
        equation_text = ""


def clear():
    global equation_text
    equation_text = ""
    equation_label.set("")


window = Tk()
window.title("Simple Calculator")
window.geometry("500x500")

equation_text = ""

equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=('consolas', 20), bg="white", width=24, height=2)
label.pack()

frame = Frame(window)
frame.pack()

# NUMBERS -------------------------------------------------------
# BUTTON 1
btn_1 = Button(frame, text=1, height=4, width=9, font=35,
               command=lambda: button_press(1))
btn_1.grid(row=0, column=0)

# BUTTON 2
btn_2 = Button(frame, text=2, height=4, width=9, font=35,
               command=lambda: button_press(2))
btn_2.grid(row=0, column=1)

# BUTTON 3
btn_3 = Button(frame, text=3, height=4, width=9, font=35,
               command=lambda: button_press(3))
btn_3.grid(row=0, column=2)

# BUTTON 4
btn_4 = Button(frame, text=4, height=4, width=9, font=35,
               command=lambda: button_press(4))
btn_4.grid(row=1, column=0)

# BUTTON 5
btn_5 = Button(frame, text=5, height=4, width=9, font=35,
               command=lambda: button_press(5))
btn_5.grid(row=1, column=1)

# BUTTON 6
btn_6 = Button(frame, text=6, height=4, width=9, font=35,
               command=lambda: button_press(6))
btn_6.grid(row=1, column=2)

# BUTTON 7
btn_7 = Button(frame, text=7, height=4, width=9, font=35,
               command=lambda: button_press(7))
btn_7.grid(row=2, column=0)

# BUTTON 8
btn_8 = Button(frame, text=8, height=4, width=9, font=35,
               command=lambda: button_press(8))
btn_8.grid(row=2, column=1)

# BUTTON 9
btn_9 = Button(frame, text=9, height=4, width=9, font=35,
               command=lambda: button_press(9))
btn_9.grid(row=2, column=2)

# BUTTON 0
btn_0 = Button(frame, text=0, height=4, width=9, font=35,
               command=lambda: button_press(0))
btn_0.grid(row=3, column=1)

# SIGNS -----------------------------------------------------------------
# BUTTON +
btn_add = Button(frame, text='+', height=4, width=9, font=35,
                 command=lambda: button_press('+'))
btn_add.grid(row=0, column=3)

# BUTTON -
btn_subtract = Button(frame, text='-', height=4, width=9, font=35,
                      command=lambda: button_press('-'))
btn_subtract.grid(row=1, column=3)

# BUTTON *
btn_multiply = Button(frame, text='*', height=4, width=9, font=35,
                      command=lambda: button_press('*'))
btn_multiply.grid(row=2, column=3)

# BUTTON /
btn_divide = Button(frame, text='/', height=4, width=9, font=35,
                    command=lambda: button_press('/'))
btn_divide.grid(row=3, column=2)

# BUTTON .
btn_decimal = Button(frame, text='.', height=4, width=9, font=35,
                     command=lambda: button_press('.'))
btn_decimal.grid(row=3, column=0)

# BUTTON =
btn_equal = Button(frame, text='=', height=4, width=9, font=35,
                   command=equals)
btn_equal.grid(row=3, column=3)

# BUTTON Clear
btn_clear = Button(frame, text='Clear', height=4, width=16, font=35,
                   command=clear)
btn_clear.grid(row=4, columnspan=4)

window.mainloop()
