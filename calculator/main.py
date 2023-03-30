import tkinter as tk
root = tk.Tk()

# display_text je proměnná, která se bude měnit podle toho, co uživatel zadává
display_text = ""
def displaying_text(input):
    global display_text
    display_text = display_text + str(input)
    display.delete("1.0", "end")
    display.insert("1.0", display_text)

# funkce pro výpočet výsledku podle toho, co uživatel zadává
def calculating_display_text():
    global display_text
    result = str(eval(display_text))
    display.delete("1.0", "end")
    display.insert("1.0", result)

# funkce pro smazání display_text (vyčistí display)
def delete_display_text():
    global display_text
    display_text = ""
    display.delete("1.0", "end")
    
display = tk.Text(root, height=2, width=24, font=("Times New Roman", 20))
display.grid(row=0, column=0, columnspan=4)

AC_button = tk.Button(root, text="AC", width=3, height=2, command=delete_display_text)
AC_button.grid(row=1, column=0, columnspan=1)

squared_button = tk.Button(root, text="x²", width=3, height=2, command=lambda: displaying_text("**2"))
squared_button.grid(row=1, column=1)

square_root_button = tk.Button(root, text="√", width=3, height=2, command=lambda: displaying_text("**0.5"))
square_root_button.grid(row=1, column=2)

divide_button = tk.Button(root, text="/", width=3, height=2, command=lambda: displaying_text("/"))
divide_button.grid(row=1, column=3)

seven_button = tk.Button(root, text="7", width=3, height=2, command=lambda: displaying_text(7))
seven_button.grid(row=2, column=0)

eight_button = tk.Button(root, text="8", width=3, height=2, command=lambda: displaying_text(8))
eight_button.grid(row=2, column=1)

nine_button = tk.Button(root, text="9", width=3, height=2, command=lambda: displaying_text(9))
nine_button.grid(row=2, column=2)

multiply_button = tk.Button(root, text="*", width=3, height=2, command=lambda: displaying_text("*"))
multiply_button.grid(row=2, column=3)

four_button = tk.Button(root, text="4", width=3, height=2, command=lambda: displaying_text(4))
four_button.grid(row=3, column=0)

five_button = tk.Button(root, text="5", width=3, height=2, command=lambda: displaying_text(5))
five_button.grid(row=3, column=1)

six_button = tk.Button(root, text="6", width=3, height=2, command=lambda: displaying_text(6))
six_button.grid(row=3, column=2)

minus_button = tk.Button(root, text="-", width=3, height=2, command=lambda: displaying_text("-"))
minus_button.grid(row=3, column=3)

one_button = tk.Button(root, text="1", width=3, height=2, command=lambda: displaying_text(1))
one_button.grid(row=4, column=0)

two_button = tk.Button(root, text="2", width=3, height=2, command=lambda: displaying_text(2))
two_button.grid(row=4, column=1)

three_button = tk.Button(root, text="3", width=3, height=2, command=lambda: displaying_text(3))
three_button.grid(row=4, column=2)

plus_button = tk.Button(root, text="+", width=3, height=2, command=lambda: displaying_text("+"))
plus_button.grid(row=4, column=3)

zero_button = tk.Button(root, text="0", width=10, height=2, command=lambda: displaying_text(0))
zero_button.grid(row=5, column=0, columnspan=2)

point_button = tk.Button(root, text=".", width=3, height=2, command=lambda: displaying_text("."))
point_button.grid(row=5, column=2)

equal_button = tk.Button(root, text="=", width=3, height=2, command=calculating_display_text)
equal_button.grid(row=5, column=3)


root.title('Calculator')
root.geometry("252x278")
root.resizable(0, 0)
root.mainloop()