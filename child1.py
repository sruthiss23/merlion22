from parent1 import rectangle
class parallelepiped(rectangle):
    def __init__(self, h):
        self.h = h

    def volume(self):
        print('volume', (self.h * rect.area))


rect = rectangle(2, 4)
rect.area()
rect.perimeter()
r1 = parallelepiped(2)
r1.volume()

