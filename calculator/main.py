import tkinter
from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image
import tkinter as tk

root = tk.Tk()

display_text = ""
def displaying_text(input):
    global display_text
    display_text = display_text + str(input)
    display.delete("1.0", "end")
    display.insert("1.0", display_text)

def calculating_display_text():
    global display_text
    result = str(eval(display_text))
    display.delete("1.0", "end")
    display.insert("1.0", result)

    
display = tk.Text(root, height=2, width=21, font=("Times New Roman", 20))
display.grid(row=1, column=1, columnspan=4)

root.title('Calculator')
root.geometry("300x300")
# root.resizable(0, 0)
root.mainloop()