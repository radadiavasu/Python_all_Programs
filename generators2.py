class FirstHundredGenerator():
    def __init__(self):
        self.number = 0

    def __next__(self):  # next(my_obj) all objectes dunder next method are called iterators
        if self.number < 100:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration
        
    def __iter__(self):
        return self


print(sum(FirstHundredGenerator()))

for i in FirstHundredGenerator():
    print(i)
# my_generator = FirstHundredGenerator()
# print(next(my_generator))
# print(next(my_generator))


