from tkinter import *
from math import *

def calculate():
    a = float(entry_a.get())
    b = float(entry_b.get())
    c = float(entry_c.get())
    if a + b <= c or a + c <= b or b + c <= a:
        result.config(text="Треугольника не существует")
        return
    P = (a + b + c) / 2
    S = sqrt(P * (P - a) * (P - b) * (P - c))
    result.config(text=f"Площадь: {S:.2f}")

window = Tk()
window.title("Калькулятор площади треугольника")
window.geometry("350x350")
Label(
    window,
    text="Калькулятор площади треугольника",
    font=("Arial", 16)).pack(pady=15)
Label(window, text="Сторона A:").pack()
entry_a = Entry(window)
entry_a.pack(pady=5)
Label(window, text="Сторона B:").pack()
entry_b = Entry(window)
entry_b.pack(pady=5)
Label(window, text="Сторона C:").pack()
entry_c = Entry(window)
entry_c.pack(pady=5)
Button(
    window,
    text="Рассчитать",
    command=calculate).pack(pady=15)
result = Label(
    window,
    text="Площадь: ",
    font=("Arial", 12))
result.pack()
window.mainloop()