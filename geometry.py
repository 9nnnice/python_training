from geom2d import *

l = [Point(i, i*i) for i in range(-5, 6)]

l2 = [Point(el.x, -el.y) for el in l]

print(l)
print(l2)