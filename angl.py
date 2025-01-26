def set_blacklist(self, black_list):
    self.__black_list = black_list

self._hitbox.set_blacklist([world.CONCRETE, world.BRICK])

def _on_map_collision(self, details):
    if world.BRICK in details:
        row = details[world.BRICK]['row']
        col = details[world.BRICK]['col']
        world.destroy(row, col)

self._destroyed = False###

def is_destroyed(self):###
    return self._destroyed

def destroy(self):###
    self._destroyed = True
    self.stop()
    self._speed = 0

def _on_map_collision(self, details):
    if world.BRICK in details:
        row = details[world.BRICK]['row']
        col = details[world.BRICK]['col']
        world.destroy(row, col)
        self.destroy()

    if world.CONCRETE in details:
        self.destroy()

def update():####
    start=len(_missiles)-1
    for i in range(start, -1, -1):
        if _missiles[i].is_destroyed():
            del _missiles[i]
        else:
            _missiles[i].update()