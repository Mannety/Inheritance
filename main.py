'''
main.py
'''
from animal import Dog, Cat

fufu = Dog(name='fufu', age=3)
baxter = Cat(name='baxter', age=5)

print(fufu.speak())
print(baxter.speak())

'''
animal.py
'''
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def speak(self):
        return f"My name is {self.name}"
    
class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
    
    def speak(self):
        return "whoof whoof!"

class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)