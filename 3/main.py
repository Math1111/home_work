
import missiles_collection
from tank import Tank
from tkinter import*
import world
import tanks_collection
import texture

def key_press(event):
    print(f'ажата клавиша {event.keysym}, код {event.keycode}')

KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN = 37,39,38,40

KEY_W=87
KEY_S=83
KEY_A=65
KEY_D=68

FPS=60
KEY_E = 69


def update():
    tanks_collection.update()#####
    missiles_collection.update()
    player=tanks_collection.get_player()
    world.set_camera_xy(player.get_x()-world.SCREEN_WIDTH//2+player.get_size()//2,
                        player.get_y()-world.SCREEN_HEIGHT//2+player.get_size()//2)
    world.update_map()
    w.after(1000//FPS,update)  




def key_press(event):
    player=tanks_collection.get_player()

    if player.is_destroyed():
        return

    elif event.keycode == KEY_W:
        player.forward()
    elif event.keycode == KEY_S:
        player.backward()
    elif event.keycode == KEY_A:
        player.left()
    elif event.keycode == KEY_D:
        player.right()
    elif event.keycode == KEY_F:
        tanks_collection.spawn()

    #if event.keycode == KEY_UP:
        #world.move_camera(0,-5)
    #if event.keycode == KEY_DOWN:
        #world.move_camera(0,5)
    #if event.keycode == KEY_LEFT:
        #world.move_camera(-5,0)
    #if event.keycode == KEY_RIGHT:
        #world.move_camera(5,0)
    elif event.keycode == 32:
        player.fire()

def load_textures():
    texture.load('tank_up',
                 '../img/tankT34_up.png')
    texture.load("tank_down",
                 '../img/tankT34_down.png')
    texture.load("tank_left",
                 '../img/tankT34_left.png')
    texture.load("tank_right",
                 '../img/tankT34_right.png')

    texture.load('tank_down_player', '../img/tank_down_player.png')
    texture.load("tank_up_player", '../img/tank_up_player.png')
    texture.load("tank_left_player", '../img/tank_left_player.png')
    texture.load("tank_right_player", '../img/tank_right_player.png')

    texture.load('missile_up', '../img/missile_up.png')
    texture.load("missile_down", '../img/missile_down.png')
    texture.load("missile_left", '../img/missile_left.png')
    texture.load("missile_right", '../img/missile_right.png')

    texture.load('xp_0', '../img/0.png')
    texture.load('xp_25', '../img/25.png')
    texture.load('xp_50', '../img/50.png')
    texture.load('xp_75', '../img/75.png')
    texture.load('xp_100', '../img/100.png')


    texture.load(world.BRICK, "../img/brick.png")
    texture.load(world.WATER, "../img/water.png")
    texture.load(world.CONCRETE, "../img/wall.png")
    texture.load(world.MISSLE, "../img/bonus.png")

    texture.load('tank_lose','../img/tank_destroy.png')

w=Tk()
load_textures()
w.title('Танки на минималках 2.0')
canv=Canvas(w, width=world.SCREEN_WIDTH, height=world.SCREEN_HEIGHT, bg='#8ccb5e')
canv.pack()
world.initialaze(canv)
tanks_collection.initialize(canv)
missiles_collection.initialize(canv)
w.bind('<KeyPress>', key_press)
update()
w.mainloop()