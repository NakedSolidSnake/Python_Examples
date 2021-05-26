#!/usr/bin/python3

class Parent:

    __parentAttr = 100

    def __init__(self):
        print("Constructor")

    def parentMethod(self):
        print("Parent Method")

    def setAttr(self, attr):
        Parent.__parentAttr = attr 
    
    def getAttr(self):
        return self.__parentAttr


class Child(Parent):
    def __init__(self):
        print("Child Constructor")

    def childMethod(self):
        print("Child Method")


c = Child()
c.childMethod()
c.parentMethod()
c.setAttr(200)
# print(c.__parentAttr)

print(c.getAttr())