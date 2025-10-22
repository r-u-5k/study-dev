class Circle:
    def __init__(self, radius=1):
        self.radius = radius

myCircle1 = Circle(20)
myCircle2 = Circle(radius=20)
print(myCircle1.radius)
print(myCircle2.radius)