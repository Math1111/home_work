from optparse import make_option
from tkinter import *

from DM import canvas


def menu_up():
    global menu_current_index
    menu_current_index-=1
    if menu_current_index<0:
        menu_current_index = 0
    menu_update()

def menu_down():
    global menu_current_index
    menu_current_index += 1
    if menu_current_index > len(menu_options) - 1:
        menu_current_index = len(menu_options) - 1
    menu_update()

def menu_create(canvas):
    offest = 0
    for menu_option in menu_options:
        option_id = canvas.create_text(400, 200+offest, anchor=CENTER, font=('Arial', '25'), text=menu_option, fill='black')
        menu_options_id.append(option_id)
        offest += 50
    menu_update()

def menu_hide():
    global menu_mode
    menu_mode = False
    menu_update()

def menu_show():
    global menu_mode
    menu_mode = True
    menu_update()

def menu_update():
    for menu_index in range(len(menu_options_id)):
        element_id = menu_options_id[menu_index]
        if menu_mode:
            canvas.itemconfig(element_id,state='normal')
            if menu_index == menu_current_index:
                canvas.itemconfig(element_id, fill='blue')
            else:
                canvas.itemconfig(element_id, fill='black')
        else:
            canvas.itemconfig(element_id, state='hidden')

def menu_enter():
    if menu_current_index == 0:
        game_resume()
    elif menu_current_index == 1:
        game_new()
    elif menu_current_index == 2:
        game_save()
    elif menu_current_index == 3:
        game_load()
    elif menu_current_index == 4:
        game_exit()
    menu_hide()

def game_new():
    print('Начинаем новую игру')
def game_resume():
    print('Возобновляем старую игру')
def game_save():
    print('Сохраняем игру')
def game_load():
    print('Загружаем игру')
def game_exit():
    print('Выходим из игры')
    exit()

def game_controller(event):
    if event.keycode == KEY_ESC:
        menu_show()
    else:
        print('Управляем персонажами игры')

def menu_controller(event):
    if event.keycode == KEY_UP:
        menu_up()
    elif event.keycode == KEY_DOWN:
        menu_down()
    elif event.keycode == KEY_ESC:
        menu_hide()
    elif event.keycode == KEY_ENTER:
        menu_enter()

def key_press(event):
    if menu_mode:
        menu_controller(event)
    else:
        game_controller(event)

menu_mode = True
menu_options = ['Возврат в игру', "Новая игра", "Сохранить", "Загрузить", "Выход"]
menu_options_id = []
menu_current_index = 3

KEY_UP = 87
KEY_DOWN = 83
KEY_ESC = 27
KEY_ENTER = 13

window_width = 800
window_height = 800
window = Tk()
window.title('Меню игры')

canvas = Canvas(window, width=window_width, height=window_height, bg='white')
window.bind('<Key>', key_press)
menu_create(canvas)
canvas.pack()
window.mainloop()