class Animal:
    def __init__(self, name):
        self.name = name
    def printName(self):
        print("Fish Name: " + self.name)

class Fish(Animal):
    def __init__(self, name, size):
        Animal.name = name
        self.size = size
    def printName(self):
        print("Animal Name: " + self.name)
    def printSize(self):
        print("size: " + str(self.size))


a = Animal("tom")
a.printName()

b = Fish("jack", 12)
b.printName()
b.printSize()

if isinstance(a, Animal):
    print("a is Animal")
else:
    print("a isn't Animal")
    
if isinstance(b, Animal):
    print("b is Animal")
else:
    print("b isn't Animal")
    
if isinstance(a, Fish):
    print("a is Fish")
else:
    print("a isn't a Fish")
    
if issubclass(Animal, Fish):
    print("Animal is subclass of Fish")
elif issubclass(Fish, Animal):
    print("Fish is subclass of Animal")
else:
    print("oh!")
