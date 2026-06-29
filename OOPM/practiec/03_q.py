'''create a base class Animal with a method sound() that prints "Some sound" .
Create a derived class Dog that overrides sound() to print "Bark!" .
Create an object of Dog and call sound() .'''
class animal:
    def sound(self):
        print("soooo")

class dog(animal):
    def sound(self):
        print("bark")

d2=dog()
d2.sound()
