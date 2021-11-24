from geom2d import *

l = list(map(lambda i: Point(i, i*i), range(-5, 6)))

l2 = list(map(lambda p: Point(p.x, -p.y), l))

print(l)
print(l2)