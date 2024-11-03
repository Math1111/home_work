from tank import Tank
from tkinter import*
import world

def key_press(event):
    print(f'ажата клавиша {event.keysym}, код {event.keycode}')

KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN = 37,39,38,40

KEY_W=87
KEY_S=83
KEY_A=65
KEY_D=68
FPS=60

def update():
    world.set_camera_xy(player.get_x()-world.SCREEN_WIDTH//2+player.get_size()//2,
                        player.get_y()-world.SCREEN_HEIGHT//2+player.get_size()//2)
    player.update()
    enemy.update()
    check_collision()
    neutral.update()
    w.after(1000//FPS,update)  

def check_collision():
    player.inersects(enemy)
    enemy.inersects(player)


def key_press(event):
    if event.keycode == KEY_W:
        player.forvard()
    if event.keycode == KEY_S:
        player.backward()
    if event.keycode == KEY_A:
        player.left()
    if event.keycode == KEY_D:
        player.right()
    check_collision()

    if event.keycode == KEY_UP:
        world.move_camera(0,-5)
    if event.keycode == KEY_DOWN:
        world.move_camera(0,5)
    if event.keycode == KEY_LEFT:
        world.move_camera(-5,0)
    if event.keycode == KEY_RIGHT:
        world.move_camera(5,0)

w=Tk()
w.title('Танки на минималках 2.0')
canv=Canvas(w, width=world.SCREEN_WIDTH, height=world.SCREEN_HEIGHT, bg='alice blue')

player=Tank(canvas=canv,x=100,y=50,ammo=100,speed = 2, bot=False)

enemy=Tank(canvas = canv, x = 300, y=300, ammo = 100,speed = 2, bot=True)
neutral=Tank(canvas = canv, x = 300, y=300, ammo = 100, speed = 1, bot=False)
neutral.stop()
canv.pack()
enemy.set_target(player)
w.bind('<KeyPress>', key_press)
update()
w.mainloop()