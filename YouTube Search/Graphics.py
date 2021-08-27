# Графическая часть
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("YouTube Search")
root.geometry("500x500")


def show_message():
    messagebox.showinfo("Ютуб", detect.get())


# Комментарий для пользователя
label = Label(root, text="↓ Ввод запроса ↓", fg='white', bg="#DC143C", pady=10, padx=1920, cursor="sb_down_arrow")
label.pack()

# Ввод запроса
detect = Entry(root, width=1920, bg='#A9A9A9', justify='center', font=('Arial', 12))
detect.pack()


filtr_var = IntVar()
Radiobutton(text='По релевантности', variable=filtr_var, value=1, activebackground='Gold', command='start').pack(anchor=W)
Radiobutton(text='По дате загрузки', variable=filtr_var, value=2, activebackground='Gold').pack(anchor=W)
Radiobutton(text='По числу просмотров', variable=filtr_var, value=3, activebackground='Gold').pack(anchor=W)
Radiobutton(text='По рейтингу', variable=filtr_var, value=4, activebackground='Gold').pack(anchor=W)


# Кнопка
button = Button(root, text="Поиск", fg="white", bg="#DC143C", activebackground='pink',
                command=show_message, pady=10, padx=1920)
button.pack()

root.mainloop()
