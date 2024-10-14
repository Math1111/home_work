from hitbox import Hitbox
hb1=Hitbox(0,100,100,100)
hb2=Hitbox(50,80,100,100)
hb3=Hitbox(140,100,100,100)

print(f"верхняя граница hb1: {hb1.top}, верхняя граница hb2: {hb2.top}")
print(f"нижняя граница hb1: {hb1.bottom}, нижняя граница hb2: {hb2.bottom}")
print(f"левая граница hb1: {hb1.left}, левая граница hb2: {hb2.left}")
print(f"равая граница hb1: {hb1.right}, правая граница hb2: {hb2.right}")

intersection1 = hb1.intersects(hb2)
intersection2 = hb1.intersects(hb3)
intersection3 = hb2.intersects(hb3)

print(f'Первый и второй: {intersection1}, первый и третий: {intersection2}, '
      f'второй и третий: {intersection3}.')