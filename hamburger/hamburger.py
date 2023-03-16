import tkinter
from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image

window = Tk()


# Funkce na vyčištění celého okna
def clear_window():
    for widgets in window.winfo_children():
        widgets.destroy()


# Widgety
# Uvítací hláška
welcome = Label(window, text="Vítejte v restauraci.", font=("Times New Roman", 30))
welcome.place(x=155, y=10)

# Jméno burgeru, label a entry
burger_name_label = Label(window, text="Jméno burgeru:", font=("Times New Roman", 15))
burger_name_label.place(x=168, y=80)
burger_name_entry = Entry(window, width=23)
burger_name_entry.place(x=300, y=80)

# Výběr masa, label a combobox (drop down menu)
meat_options_label = Label(window, text="Vyberte maso:", font=("Times New Roman", 15))
meat_options_label.place(x=174, y=120)
meat_options = ("Hovezí", "Kuřecí", "Krůtí", "Ryba")
meat_options_combobox = Combobox(window, values=meat_options)
meat_options_combobox.place(x=300, y=120)

# Výběr žemle, labely a combobox (drop down menu)
buns_options_label = Label(window, text="Vyberte žemli:", font=("Times New Roman", 15))
buns_options_label.place(x=174, y=160)
buns_options = ("Domácí houska", "Bulka", "Brioška na burger")
buns_options_combobox = Combobox(window, values=buns_options)
buns_options_combobox.place(x=300, y=160)

# Výběr zeleniny, labely a listbox (menu)
vegetable_options_label = Label(window, text="Vyberte zeleninu:", font=("Times New Roman", 15))
vegetable_options_label.place(x=153, y=200)
tomato = IntVar()
salad = IntVar()
pickle = IntVar()
vegetable_options_checkbox_tomato = Checkbutton(window, text="Rajče", variable=tomato)
vegetable_options_checkbox_tomato.place(x=300, y=200)
vegetable_options_checkbox_salad = Checkbutton(window, text="Salát", variable=salad)
vegetable_options_checkbox_salad.place(x=300, y=220)
vegetable_options_checkbox_pickle = Checkbutton(window, text="Okurka", variable=pickle)
vegetable_options_checkbox_pickle.place(x=300, y=240)

# Výběr omáčky, labely a combobox (drop down menu)
sauce_options_label = Label(window, text="Vyberte omáčku:", font=("Times New Roman", 15))
sauce_options_label.place(x=157, y=270)
sauce_options = ("Kečup", "Majonéza", "BBQ omáčka")
sauce_options_combobox = Combobox(window, values=sauce_options)
sauce_options_combobox.place(x=300, y=270)


def button_clicked():
    err = ""
    burger_name_get = burger_name_entry.get()
    meat_options_get = meat_options_combobox.get()
    buns_options_get = buns_options_combobox.get()
<<<<<<< HEAD
    vegetable_tomato = tomato.get()
    vegetable_salad = salad.get()
    vegetable_pickle = pickle.get()
=======
>>>>>>> origin/master
    sauce_options_get = sauce_options_combobox.get()
    if burger_name_get == "":
        err_screen = Toplevel(window)
        err_screen.geometry("150x50")
        Label(err_screen, text="Vypňte jméno prosím").pack()
    elif meat_options_get == "":
        err_screen = Toplevel(window)
        err_screen.geometry("150x50")
        Label(err_screen, text="Vyberte maso prosím.").pack()
    elif buns_options_get == "":
        err_screen = Toplevel(window)
        err_screen.geometry("150x50")
        Label(err_screen, text="Vyberte žemli prosím.").pack()
    elif sauce_options_get == "":
        err_screen = Toplevel(window)
        err_screen.geometry("170x50")
        Label(err_screen, text="Vyberte si omáčku prosím.").pack()
<<<<<<< HEAD
    elif vegetable_tomato == 0 and vegetable_salad == 0 and vegetable_pickle == 0:
        err_screen = Toplevel(window)
        err_screen.geometry("170x50")
        Label(err_screen, text="Vyberte si zeleninu.").pack()
    elif err == "":
        clear_window()
        print(buns_options_get)
        # img = ImageTk.PhotoImage(Image.open("img/cute_rat.jpg"))
        # img_print = tkinter.Label(window, image=img)
        # img_print.PhotoImage = img
        # img_print.pack()
        if buns_options_get == "Domácí houska":
            img_top_domaci = ImageTk.PhotoImage(Image.open("img/top_domaci.png"))
            img_print = tkinter.Label(window, image=img_top_domaci)
            img_print.PhotoImage = img_top_domaci
            img_print.place(x=155, y=0)
            img_buttom_domaci = ImageTk.PhotoImage(Image.open("img/buttom_domaci.png"))
            img_print = tkinter.Label(window, image=img_buttom_domaci)
            img_print.PhotoImage = img_buttom_domaci
            img_print.place(x=155, y=340)
        elif buns_options_get == "Bulka":
            img_top_bulka = ImageTk.PhotoImage(Image.open("img/top_bulka.png"))
            img_print = tkinter.Label(window, image=img_top_bulka)
            img_print.PhotoImage = img_top_bulka
            img_print.place(x=155, y=0)
            img_buttom_bulka = ImageTk.PhotoImage(Image.open("img/buttom_bulka.png"))
            img_print = tkinter.Label(window, image=img_buttom_bulka)
            img_print.PhotoImage = img_buttom_bulka
            img_print.place(x=155, y=340)
        elif buns_options_get == "Brioška na burger":
            img_top_brioska = ImageTk.PhotoImage(Image.open("img/top_brioska.png"))
            img_print = tkinter.Label(window, image=img_top_brioska)
            img_print.PhotoImage = img_top_brioska
            img_print.place(x=155, y=0)
            img_buttom_brioska = ImageTk.PhotoImage(Image.open("img/buttom_brioska.png"))
            img_print = tkinter.Label(window, image=img_buttom_brioska)
            img_print.PhotoImage = img_buttom_brioska
            img_print.place(x=155, y=340)
=======
    elif err == "":
        clear_window()
        img = ImageTk.PhotoImage(Image.open("img/cute_rat.jpeg"))
        img_print = tkinter.Label(window, image=img)
        img_print.PhotoImage = img
        img_print.pack()
>>>>>>> origin/master

        if meat_options_get == "Hovezí":
            print(meat_options_get)
            img_meat_hovezi = ImageTk.PhotoImage(Image.open("img/meat_hovezi.png"))
            img_print = tkinter.Label(window, image=img_meat_hovezi)
            img_print.PhotoImage = img_meat_hovezi
            img_print.place(x=155, y=150)
        elif meat_options_get == "Kuřecí":
            print(meat_options_get)
            img_meat_kureci = ImageTk.PhotoImage(Image.open("img/meat_kureci.png"))
            img_print = tkinter.Label(window, image=img_meat_kureci)
            img_print.PhotoImage = img_meat_kureci
            img_print.place(x=155, y=150)
        elif meat_options_get == "Krůtí":
            print(meat_options_get)
            img_meat_kruti = ImageTk.PhotoImage(Image.open("img/meat_kruti.png"))
            img_print = tkinter.Label(window, image=img_meat_kruti)
            img_print.PhotoImage = img_meat_kruti
            img_print.place(x=155, y=150)
        elif meat_options_get == "Ryba":
            print(meat_options_get)
            img_meat_ryba = ImageTk.PhotoImage(Image.open("img/meat_ryba.png"))
            img_print = tkinter.Label(window, image=img_meat_ryba)
            img_print.PhotoImage = img_meat_ryba
            img_print.place(x=155, y=150)

        if vegetable_tomato == 1:
            img_vegetable_tomato = ImageTk.PhotoImage(Image.open("img/vegetable_rajce.png"))
            img_print = tkinter.Label(window, image=img_vegetable_tomato)
            img_print.PhotoImage = img_vegetable_tomato
            img_print.place(x=155, y=184)
        if vegetable_salad == 1:
            img_vegetable_salad = ImageTk.PhotoImage(Image.open("img/vegetable_salat.png"))
            img_print = tkinter.Label(window, image=img_vegetable_salad)
            img_print.PhotoImage = img_vegetable_salad
            if vegetable_tomato == 1:
                img_print.place(x=155, y=224)
            else:
                img_print.place(x=155, y=184)
        if vegetable_pickle == 1:
            img_vegetable_pickle = ImageTk.PhotoImage(Image.open("img/vegetable_okurka.png"))
            img_print = tkinter.Label(window, image=img_vegetable_pickle)
            img_print.PhotoImage = img_vegetable_pickle
            if vegetable_tomato == 1:
                if vegetable_salad == 1:
                    img_print.place(x=155, y=264)
                else:
                    img_print.place(x=155, y=224)
            elif vegetable_salad == 1:
                img_print.place(x=155, y=224)
            else:
                img_print.place(x=155, y=184)

        if sauce_options_get == "Kečup":
            print(sauce_options_get)
            img_sauce_ketchup = ImageTk.PhotoImage(Image.open("img/sauce_kecup.png"))
            img_print = tkinter.Label(window, image=img_sauce_ketchup)
            img_print.PhotoImage = img_sauce_ketchup
            img_print.place(x=155, y=304)
        if sauce_options_get == "Majonéza":
            print(sauce_options_get)
            img_sauce_majonese = ImageTk.PhotoImage(Image.open("img/sauce_majoneza.png"))
            img_print = tkinter.Label(window, image=img_sauce_majonese)
            img_print.PhotoImage = img_sauce_majonese
            img_print.place(x=155, y=304)
        if sauce_options_get == "BBQ omáčka":
            print(sauce_options_get)
            img_sauce_bbq = ImageTk.PhotoImage(Image.open("img/sauce_BBQ.png"))
            img_print = tkinter.Label(window, image=img_sauce_bbq)
            img_print.PhotoImage = img_sauce_bbq
            img_print.place(x=155, y=304)

# Tlačítko na potvrzení
Button(window, text="Hotovo", command=button_clicked).place(x=250, y=310)

window.title('Hello Python')
window.geometry("600x600")
window.mainloop()
