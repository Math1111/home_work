from units import Missile
_missiles=[]
_canvas=None

def initialize(canvas):
    global _canvas
    _canvas = canvas

def fire(owner):
    m = Missile(_canvas, owner)
    _missiles.append(m)

def update():
    for missile in _missiles:
        missile.update()
