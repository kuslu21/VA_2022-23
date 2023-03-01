from tkinter import *

error = False

root = Tk()
root.title("Burger konfigurátor")
root.geometry('500x250')
# jmeno ---------------------------------------------------------------------------
lbl = Label(root, text="Jak se má burger jmenovat?")
lbl.grid()

name = Entry(root, width=12)
name.grid(column=1, row=0)
# maso ----------------------------------------------------------------------------
lbl2 = Label(root, text="Jaké maso by jste chtěli? Možnosti -> hovězí, kuřecí, ryba :((")
lbl2.grid()

meat = Entry(root, width=12)
meat.grid(column=1, row=0)
# --------------------------------------------------------------------------------
if name != "" and error is not True:
    # function to display user text when
    # button is clicked
    def clicked():
        res = "Hotovo, Burger se jmenuje:" + name.get()
        lbl.configure(text=res)


    # # button widget with red color text inside
    # btn = Button(root, text="Click me",
    #              fg="red", command=clicked)
    # # Set Button Grid
    # btn.grid(column=2, row=0)
    #
    # # Execute Tkinter
    root.mainloop()
