class MyClass:
    'MyClass, just for test'
    name = ''
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printAge(self):
        print('age:'+str(self.age))
    def __getName__(self):
        return self.name
    def printInfo(self):
        print("name="+self.__getName__())
        self.printAge()


class1 = MyClass("lisper", 12)
print(class1.__getName__())
class1.printAge()
class1.printInfo()

print("\/" * 30);
class MyClassChild(MyClass):
    def __init__(self, name, age):
        super().__init__(name, age)

class2 = MyClassChild('tom', 10)
class2.printInfo()

print("\/" * 30, end='\\\n')

class MyClassChild2(MyClassChild):
    def __init__(self, name):
        super(MyClassChild2, self).__init__(name, 2)
    def printInfo(self):
        print("printInfo:")
        super(MyClassChild2, self).printInfo()

class3 = MyClassChild2('child2')
class3.printInfo()
print("\/" * 30, end='\\\n')
