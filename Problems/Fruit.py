class Fruit:
    def __init__(self,color,weight):
        self.color = color
        self.weight = weight
    def eat(self):
        print "Eaten"
f = Fruit("red",1)
f.eat()