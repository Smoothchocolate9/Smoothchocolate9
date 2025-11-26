from tkinter import *
from tkinter import filedialog
root = Tk()
root.title("Text Editor")
root.geometry("600x400")
text = Text(root, wrap="word")
text.pack(fill="both", expand=True)
def new_file():
    text.delete(1.0, END)
def open_file():
    file = filedialog.askopenfilename()
    if file:
        text.delete(1.0, END)
        f = open(file, "r")
        text.insert(END, f.read())
        f.close()
def save_file():
    file = filedialog.asksaveasfilename(defalutextentions=".txt")
    if file:
        f = open(file, "W")
        f.write(text.get(1.0, END))
        f.close
menu = Menu(root)
root.config(menu=menu)
file_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=new_file)
file_menu.add_command(label="Save", command=new_file)
file_menu.add_command(label="Exit", command=new_file)
root.mainloop
