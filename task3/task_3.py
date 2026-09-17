from tkinter import *

def vis_year():
    year = int(entry.get())
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        result.config(text="високосный год")
    else:
        result.config(text="не високосный год")

window = Tk()
window.title("Определение високосного года")
window.geometry("350x270")
Label(
    window,
    text="Определение високосного года",
    font=("Arial", 16, "bold")).pack(pady=20)
Label(
    window,
    text="Введите год:",
    font=("Arial", 16)).pack()
entry = Entry(window)
entry.pack(pady=10)
Button(
    window,
    text="Определить",
    command=vis_year,
    width=15,
    height=2,
    bg='Orange',).pack(pady=10)
Label(
    window,
    text="Результат:",
    font=("Arial", 16, "bold")).pack(pady=5)
result = Label(
    window,
    text="",
    font=("Arial", 14))
result.pack()
window.mainloop()