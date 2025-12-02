import tkinter as tk
from tkinter Toplevel
root = tk.Tk()
root.geometry("300x200")
def open_window():
    win = Toplevel(root)
    win.geometry("200x150")
    tk.Label(win, text="This is a new window").pack()
    btn = tk.Button(root, text="Open Window", command=open_window)
btn.pack(pady=40)
root.mainloop()
