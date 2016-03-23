class Father:
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


person = Father("lisper", 12)
print(person.__getName__())
person.printAge()
person.printInfo()

print("\/" * 30);
class Child(Father):
    def __init__(self, name, age):
        #Father.__init__(self,name,age)
        super().__init__(name, age)

person1 = Child('tom', 10)
person1.printInfo()

