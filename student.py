class Student(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.__person= [self.name,self.age]

    def printName(self):
        print(self.name)

    def printAge(self):
        print(self.age)

    def printPerson(self):
        for name in self.__person:
            print(name)
            pass
    