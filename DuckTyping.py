class Duck:
    def quack(self):
        print("Quack")

class Person:
    def quack(self):
        print("I'm not a duck, but I can still quack like one!")

def do_quack(obj):
    obj.quack()

duck = Duck()
person = Person()

do_quack(duck)
do_quack(person)