# Картинки танков

from hitbox import Hitbox
from tkinter import *
from random import randint
import world

class Tank:
    __count = 0
    # 1 в параметры объекта добавить картинки (путь до картинк)
    def __init__(self, canvas, x, y,model = 'Т-14 Армата', ammo = 100, speed = 5,
                 file_up = '../img/tankT34_up.png',
                 file_down = '../img/tankT34_down.png',
                 file_left = '../img/tankT34_left.png',
                 file_right = '../img/tankT34_right.png',

                 bot=True):
        self.__bot=bot
        self.__target = None
        self.__skin_up = PhotoImage(file = file_up)
        self.__skin_down = PhotoImage(file = file_down)
        self.__skin_left = PhotoImage(file = file_left)
        self.__skin_right = PhotoImage(file = file_right)

        Tank.__count += 1
        self.__hitbox = Hitbox(x, y, self.get_sise(), self.get_sise(), padding=2)
        self.__canvas = canvas
        self.__model = model
        self.__hp = 100
        self.__xp = 0
        self.__ammo = ammo
        self.__fuel = 10000
        self.__speed = speed
        self.__x = x
        self.__y = y
        self.__vx = 0
        self.__vy = 0
        self.__dx = 0
        self.__dy = 0
        if self.__x < 0:
            self.__x = 0
        if self.__y < 0:
            self.__y = 0

        self.__create()
        self.right()

    def fire(self):
        if self.__ammo > 0:
            self.__ammo -= 1
            print('стреляю')

    def forvard(self):
        self.__vx = 0
        self.__vy = -1
        self.__canvas.itemconfig(self.__id, image = self.__skin_up)



    def backward(self):
        self.__vx = 0
        self.__vy = 1
        self.__canvas.itemconfig(self.__id, image = self.__skin_down)



    def left(self):
        self.__vx = -1
        self.__vy = 0
        self.__canvas.itemconfig(self.__id, image = self.__skin_left)



    def right(self):
        self.__vx = 1
        self.__vy = 0
        self.__canvas.itemconfig(self.__id, image = self.__skin_right)

    def set_target(self, target):
        self.__target = target

    def _AI_goto_target(self):
        if randint(1,2) == 1:
            if self.__target.get_x() > self.get_x():
                self.right()
            else:
                self.left()
        else:
            if self.__target.get_y() > self.get_y():
                self.backward()
            else:
                self.forvard()


    def __AI(self):
        if randint(1, 30) == 1:
            if randint(1,10) < 9 and self.__target is not None:
                self._AI_goto_target()
            else:
                self.__AI_change_orientation()

    def __AI_change_orientation(self):
        rand = randint(0, 3)
        if rand == 0:
            self.left()
        if rand == 1:
            self.right()
        if rand == 2:
            self.forvard()
        if rand == 3:
            self.backward()

    def __check_out_of_world(self):
        if self.__hitbox.left < 0 or \
            self.__hitbox.top < 0 or \
            self.__hitbox.right >= world.WIDTH or \
            self.__hitbox.bottom >= world.HEIGHT:
                self.__undo_move()
        if self.__bot:
            self.__AI_change_orientation()

    def __create(self):
        self.__id = self.__canvas.create_image(self.__x, self.__y,
                                               image = self.__skin_up,
                                               anchor ='nw')

    def __repaint(self):
        self.__canvas.moveto(self.__id, x = self.__x, y = self.__y)

    def __update_hitbox(self):
        self.__hitbox.moveto(self.__x, self.__y)

    def __undo_move(self):
        if self.__dx == 0 and self.__dy == 0:
            return
        self.__x -= self.__dx
        self.__y -= self.__dy
        self.__update_hitbox()
        self.__repaint()
        self.__dx = 0
        self.__dy = 0

    def update(self):
        if self.__fuel >= self.__speed:
            if self.__bot:
                self.__AI()
            self.__update_hitbox()
            self.__check_out_of_world()
            self.__dx = self.__vx * self.__speed
            self.__dy = self.__vy * self.__speed
            self.__x += self.__dx
            self.__y += self.__dy
            self.__fuel -= self.__speed
            self.__update_hitbox()
            self.__repaint()

    def inersects(self, other_tank):
        value = self.__hitbox.intersects(other_tank.__hitbox)
        if value:
            self.__undo_move()
            if self.__bot:
                self.__AI_change_orientation()
        return value

    def get_x(self):
        return self.__x
    def get_y(self):
        return self.__y

    def get_ammo(self):
        return self.__ammo

    def get_model(self):
        return self.__model

    def get_hp(self):
        return self.__hp

    def get_xp(self):
        return self.__xp

    def get_fuel(self):
        return self.__fuel

    def get_speed(self):
        return self.__speed

    @staticmethod
    def grt_quantity():
        return Tank.__count

    def get_sise(self):
        return self.__skin_up.width()

    def __str__(self):
        return (f'координаты: x = {self.__x}, y = {self.__y}, модель: {self.__model}, '
                f'здоровье: {self.__hp}, опыт: {self.__xp}, боеприпасы: {self.__ammo}')