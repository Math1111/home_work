_camera_x=0
_camera_y=0
SCREEN_WIDTH=800
SCREEN_HEIGHT=800
WIDTH=SCREEN_WIDTH*6
HEIGHT=SCREEN_HEIGHT*4

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


