from abc import ABCMeta, abstractmethod

class Animal(metaclass=ABCMeta): # "abc means abstract base class."
    def walk(self):
        print('Walking...')
    
    @abstractmethod
    def num_legs(self):
        pass
      
class Dog(Animal):
    def __init__(self, name):
        self.name = name
        
    def num_legs(self):
        return 4
    
class Monkey(Animal):
    def __init__(self, name):
        self.name = name
        
    def num_legs(self):
        return 2
    

d = Dog('rolf')
print(d.num_legs())