import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.ttk import *

window = Tk()
window.geometry("400x600")
window.title("Рогов Роман Николаевич")


def calculate():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    operator = operator_var.get()

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2

    messagebox.showinfo("Результат", f"Результат: {result}")


def show_selected_options():
    selected_options = []
    if checkbox1_var.get():
        selected_options.append("Первый")
    if checkbox2_var.get():
        selected_options.append("Второй")
    if checkbox3_var.get():
        selected_options.append("Третий")

    messagebox.showinfo("Выбранные опции", f"Вы выбрали: {', '.join(selected_options)}")


def open_file():
    filename = askopenfilename()


notebook = tk.ttk.Notebook(window)
notebook.pack(pady=10, padx=10)

tab1 = tk.Frame(notebook)
tab1.pack()

entry1 = tk.Entry(tab1)
entry1.pack()

operator_var = tk.StringVar(tab1)
operator_var.set("+")
operator_dropdown = tk.OptionMenu(tab1, operator_var, "+", "-", "*", "/")
operator_dropdown.pack()

entry2 = tk.Entry(tab1)
entry2.pack()

calculate_button = tk.Button(tab1, text="Вычислить", command=calculate)
calculate_button.pack()

tab2 = tk.Frame(notebook)
tab2.pack()

checkbox1_var = tk.BooleanVar()
checkbox2_var = tk.BooleanVar()
checkbox3_var = tk.BooleanVar()

checkbox1 = tk.Checkbutton(tab2, text="Первый", variable=checkbox1_var)
checkbox1.pack()

checkbox2 = tk.Checkbutton(tab2, text="Второй", variable=checkbox2_var)
checkbox2.pack()

checkbox3 = tk.Checkbutton(tab2, text="Третий", variable=checkbox3_var)
checkbox3.pack()

show_options_button = tk.Button(tab2, text="Показать выбранные опции", command=show_selected_options)
show_options_button.pack()

tab3 = tk.Frame(notebook)
tab3.pack()

open_file_button = tk.Button(tab3, text="Загрузить файл", command=open_file)
open_file_button.pack()

notebook.add(tab1, text="Калькулятор")
notebook.add(tab2, text="Чекбоксы")
notebook.add(tab3, text="Работа с текстом")

window.mainloop()