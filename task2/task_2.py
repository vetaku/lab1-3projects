from tkinter import *

def converter():
    a = float(entry.get())
    if a_from.get() == "км":
        metr = a * 1000
    elif a_from.get() == "м":
        metr = a
    elif a_from.get() == "см":
        metr = a / 100
    elif a_from.get() == "мм":
        metr = a / 1000
    elif a_from.get() == "mi":
        metr = a * 1609.34
    elif a_from.get() == "yd":
        metr = a * 0.9144

    if a_to.get() == "км":
        result_a = metr / 1000
    elif a_to.get() == "м":
        result_a = metr
    elif a_to.get() == "см":
        result_a = metr * 100
    elif a_to.get() == "мм":
        result_a = metr * 1000
    elif a_to.get() == "mi":
        result_a = metr / 1609.34
    elif a_to.get() == "yd":
        result_a = metr / 0.9144
    result.config(text=f"Результат: {result_a:.2f} {a_to.get()}")

window = Tk()
window.title("Конвертер единиц измерения расстояния")
window.geometry("400x400")
Label(
    window,
    text="Конвертер единиц измерения расстояния",
    font=("Arial", 18, "bold")).pack(pady=30)
Label(window, text="Из какой единицы:").pack()
a_from = StringVar()
a_from.set("м")
OptionMenu(
    window,
    a_from,
    "км", "м", "см", "мм", "mi", "yd").pack(pady=5)
Label(window, text="В какую единицу:").pack()
a_to = StringVar()
a_to.set("км")
OptionMenu(
    window,
    a_to,
    "км", "м", "см", "мм", "mi", "yd").pack(pady=5)
Label(window, text="Введите расстояние:").pack()
entry = Entry(window)
entry.pack(pady=5)
Button(
    window,
    text="Конвертировать",
    command=converter).pack(pady=15)
result = Label(
    window,
    text="Результат: ",
    font=("Arial", 12))
result.pack()
window.mainloop()