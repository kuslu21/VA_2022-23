from tkinter import *
from tkinter.ttk import *
window = Tk()
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
vegetable_options = ("Rajče", "Salát", "Okurka")
vegetable_options_listbox = Listbox(window, height=3, width=23, selectmode='multiple')
for num in vegetable_options:
    vegetable_options_listbox.insert(END, num)
vegetable_options_listbox.place(x=300, y=200)

# Výběr omáčky, labely a combobox (drop down menu)
sauce_options_label = Label(window, text="Vyberte omáčku:", font=("Times New Roman", 15))
sauce_options_label.place(x=157, y=270)
sauce_options = ("Kečup", "Majonéza", "BBQ omáčka")
sauce_options_combobox = Combobox(window, values=sauce_options)
sauce_options_combobox.place(x=300, y=270)

# Tlačítko na potvrzení
submit_button=Button(window, text="Hotovo")
submit_button.place(x=250, y=310)

window.title('Hello Python')
window.geometry("600x600")
window.mainloop()
