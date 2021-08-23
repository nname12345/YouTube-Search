#  Техническая часть
from selenium import webdriver
driver = webdriver.Chrome('C:/Users/Лев/Desktop/YouTube Search/DriverChrome/chromedriver.exe')
# Графическая часть
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('YouTube Search')
root.geometry("500x500")


def show_message():
    messagebox.showinfo('Ютуб', detect.get())


# Комментарий для пользователя
label = Label(root, text='↓ Ввод запроса ↓', fg='white', bg='#DC143C', pady=10, padx=1920, cursor='sb_down_arrow')
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
button = Button(root, text='Поиск', fg='white', bg='#DC143C', activebackground='pink', command='show_message', pady=10, padx=1920)
button.pack()

root.mainloop()

#  Поиск видео
def start():
    driver.get('httpswww.youtube.com') # ссылка сайта, на котором будет выполняться действие
    search = driver.find_element_by_xpath('[@id=search]') # строка ввода
    search.send_keys(detect) # ввод содержания
    button = driver.find_element_by_xpath('[@id=search-icon-legacy]yt-icon') # поиск  наведение
    button.click() # поиск  клик
    filtr0 = driver.find_element_by_xpath('htmlbodyytd-appdivytd-page-managerytd-searchdiv[1]ytd-two-column-search-results-rendererdivytd-section-list-rendererdiv[1]div[2]ytd-search-sub-menu-rendererdiv[1]divytd-toggle-button-rendereratp-yt-paper-buttonyt-icon')
    filtr0.click()
    video1 = driver.find_element_by_xpath('htmlbodyytd-appdivytd-page-managerytd-searchdiv[1]ytd-two-column-search-results-rendererdivytd-section-list-rendererdiv[2]ytd-item-section-rendererdiv[3]ytd-video-renderer[1]div[1]divdiv[1]divh3ayt-formatted-string')
    video1.click()

