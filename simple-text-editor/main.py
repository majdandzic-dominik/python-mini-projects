import os
from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *


def change_color():
    color = colorchooser.askcolor(title="Pick a color")
    text_area.config(fg=str(color[1]))


def change_font(*args):
    text_area.config(font=(font_name.get(), size_box.get()))


def new_file():
    window.title("Untitled")
    text_area.delete(1.0, END)


def open_file():
    selected_file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])

    try:
        window.title(os.path.basename(selected_file))
        text_area.delete(1.0, END)

        file = open(selected_file, "r")

        text_area.insert(1.0, file.read())
    except Exception:
        print("Couldn't read file")
    finally:
        file.close()


def save_file():
    file_to_save = filedialog.asksaveasfilename(initialfile="untitled.txt",
                                        defaultextension=".txt",
                                        filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file_to_save is None:
        return
    else:
        try:
            window.title(os.path.basename(file_to_save))
            file = open(file_to_save, "w")
            file.write(text_area.get(1.0, END))
        except Exception:
            print("Couldn't save file")
        finally:
            file.close()

def cut():
    text_area.event_generate("<<Cut>>")


def copy():
    text_area.event_generate("<<Copy>>")


def paste():
    text_area.event_generate("<<Paste>>")


def about():
    showinfo("About text editor", "This is where description goes")


def quit():
    window.destroy()


# INTERFACE
window = Tk()
window.title("Simple Text Editor")
file = None

# centering window
window_width = 500
window_height = 500
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))

# initial font
font_name = StringVar()
font_name.set("Arial")

font_size = StringVar()
font_size.set("25")

text_area = Text(window, font=(font_name.get(), font_size.get()))

# text area
scroll_bar = Scrollbar(text_area)
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
text_area.grid(sticky=N + E + S + W)  # north east south west

scroll_bar.pack(side=RIGHT, fill=Y)
text_area.config(yscrollcommand=scroll_bar.set)

# font controls
frame = Frame(window)
frame.grid()

color_btn = Button(frame, text="color", command=change_color)
color_btn.grid(row=0, column=0)

font_box = OptionMenu(frame, font_name, *font.families(), command=change_font)
font_box.grid(row=0, column=1)

size_box = Spinbox(frame, from_=1, to=100, textvariable=font_size, command=change_font)
size_box.grid(row=0, column=2)

# menu
menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit)

edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)

help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about)

window.mainloop()
