import texture
from tkinter import NW
from random import randint, choice

GROUND='g'
WATER='w'
CONCRETE='c'
BRICK='b'

_canvas = None
BLOCK_SIZE = 64

_camera_x=0
_camera_y=0
SCREEN_WIDTH=800
SCREEN_HEIGHT=800
WIDTH=SCREEN_WIDTH*6
HEIGHT=SCREEN_HEIGHT*4

_map=None

def initialaze(canv):
    global _canvas, _map
    _canvas = canv
    _map=_Cell(_canvas,WATER,0,0)
    #create_map(20,20)

def set_camera_xy(x,y):
    global _camera_x, _camera_y
    if x<0:
        x=0
    if y<0:
        y=0

    if x>WIDTH - SCREEN_WIDTH:
        x=WIDTH-SCREEN_WIDTH
    if y>HEIGHT-SCREEN_HEIGHT:
        y=HEIGHT-SCREEN_HEIGHT

    _camera_x=x
    _camera_y=y

def move_camera(delta_x, delta_y):
    set_camera_xy(_camera_x + delta_x, _camera_y + delta_y)

def get_screen_x(world_X):
    return world_X - _camera_x

def get_screen_y(world_Y):
    return world_Y - _camera_y

class _Cell:
    def __init__(self, canvas, block, x, y):
        self.__canvas = canvas
        self.__block = block
        self.__x = x
        self.__y = y
        self.__create_element(block)

    def __create_element(self, block):
        if block != GROUND:
            self.__id = self.__canvas.create_image(self.__x, self.__y, image=texture.get(block),anchor=NW)

    def __del__(self):
        try:
            self.__canvas.delete(self.__id)
        except:
            pass

    def get_block(self):
        return self.__block