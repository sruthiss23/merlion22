class rectangle:
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def perimeter(self):
        self.perimeter = 2 * (self.l + self.b)
        print ('perimeter = ', self.perimeter)

    def area(self):
        self.area = self.l * self.b
        print ('area =', self.area)