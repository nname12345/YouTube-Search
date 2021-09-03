# Графическая часть
from tkinter import *
from selenium import webdriver
driver = webdriver.Chrome('C:/Users/Family/Desktop/YouTube Search/DriverChrome/chromedriver.exe')

root = Tk()
root.title("YouTube Search")
root.geometry("400x300+300+250")


def show_message():
    driver.get('https://www.youtube.com/')  # ссылка сайта, на котором будет выполняться действие
    search = driver.find_element_by_xpath('//*[@id="search"]')  # строка ввода
    search.send_keys(detect.get())  # ввод содержания
    button = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]/yt-icon')  # поиск > наведение
    button.click()  # поиск > клик


def watch_filtr2():
    icon = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[1]/div[2]/ytd-search-sub-menu-renderer/div[1]/div/ytd-toggle-button-renderer/a/tp-yt-paper-button/yt-formatted-string')
    icon.click()
    filtr2 = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[1]/div[2]/ytd-search-sub-menu-renderer/div[1]/iron-collapse/div/ytd-search-filter-group-renderer[5]/ytd-search-filter-renderer[2]/a/div/yt-formatted-string')
    filtr2.click()


def watch_filtr3():
    icon = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[1]/div[2]/ytd-search-sub-menu-renderer/div[1]/div/ytd-toggle-button-renderer/a/tp-yt-paper-button/yt-icon')
    icon.click()
    filtr3 = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[1]/div[2]/ytd-search-sub-menu-renderer/div[1]/iron-collapse/div/ytd-search-filter-group-renderer[5]/ytd-search-filter-renderer[3]/a/div/yt-formatted-string')
    filtr3.click()


def watch_filtr4():
    icon = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[1]/div[2]/ytd-search-sub-menu-renderer/div[1]/div/ytd-toggle-button-renderer/a/tp-yt-paper-button/yt-icon')
    icon.click()
    filtr4 = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[1]/div[2]/ytd-search-sub-menu-renderer/div[1]/iron-collapse/div/ytd-search-filter-group-renderer[5]/ytd-search-filter-renderer[4]/a/div/yt-formatted-string')
    filtr4.click()


# Комментарий для пользователя
label = Label(root, text="↓ Ввод запроса ↓", fg='white', bg="#DC143C", pady=10, padx=1920, cursor="sb_down_arrow")
label.pack()

# Ввод запроса
detect = Entry(root, width=1920, bg='#A9A9A9', justify='center', font=('Arial', 12))
detect.pack()


filtr_var = IntVar()
Radiobutton(text='По релевантности', variable=filtr_var, value=1, activebackground='Gold', command='start').pack(anchor=W)
Radiobutton(text='По дате загрузки', variable=filtr_var, value=2, activebackground='Gold', command=watch_filtr2).pack(anchor=W)
Radiobutton(text='По числу просмотров', variable=filtr_var, value=3, activebackground='Gold', command=watch_filtr3).pack(anchor=W)
Radiobutton(text='По рейтингу', variable=filtr_var, value=4, activebackground='Gold', command=watch_filtr4).pack(anchor=W)


# Кнопка
button = Button(root, text="Поиск", fg="white", bg="#DC143C", activebackground='pink',
                command=show_message, pady=10, padx=1920)
button.pack()

root.mainloop()
