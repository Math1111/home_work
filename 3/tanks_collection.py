from tkinter import NW
import time
from random import randint
from missiles_collection import check_missiles_collision
#from tank import Tank
import world
from units import Tank

_tanks = []
_canvas = None

id_screen_text = 0
remaining_tanks = 0

def initialize(canv):
    global _canvas, id_screen_text
    _canvas = canv

    #spawn(False)
    #for i in range(2):
        #spawn(True).set_target(get_player())
    #print(_tanks)
    player=spawn(False)
    enemy=spawn(True).set_target(player)
    spawn(True).set_target(player)




    id_screen_text = _canvas.create_text(10,10,text=_get_screen_text(),font=('TkDefaultFont',20),fill='white',anchor=NW)
    return id_screen_text

def _get_screen_text():
    global remaining_tanks
    if remaining_tanks == 0:
        return 'Вы проиграли!'
    elif remaining_tanks == 1:
        return 'Вы победили!'
    else:
        return f'Осталось {remaining_tanks}'


def update_screen_text(canv, id_screen_text):
    canv.itemconfig(id_screen_text, text=_get_screen_text())

def get_player():
    return _tanks[0]


def _update_screen_text():
    _canvas.itemconfig(id_screen_text,text=_get_screen_text())

def get_player():
    return _tanks[0]




def update():
    _update_screen_text()
    start=len(_tanks)-1
    for i in range(start,-1,-1):
        if _tanks[i].is_destroyed() and i!=0:
            del _tanks[i]
            print(5)
        else:
            _tanks[i].update()
            check_collision(_tanks[i])
            check_missiles_collision(_tanks[i])


def check_collision(tank):
    for other_tank in _tanks:
        if tank == other_tank:
            continue
        if tank.intersects(other_tank):
            return True
    return False

def spawn(is_bot=True):
    global remaining_tanks
    cols = world.get_cols()
    rows = world.get_rows()

    while True:
        col = randint(1, cols-1)
        row = randint(1, rows-1)

        if world.get_block(row, col) != world.GROUND:
            continue

        t = Tank(_canvas, row, col,bot=is_bot)
        if not check_collision(t):
            _tanks.append(t)
            remaining_tanks +=1
            return t