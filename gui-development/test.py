# List comprehension in Python
numbers = [1, 2, 3, 4, 5, 6]
integrated_list = [x**2 for x in numbers]
print(integrated_list)


# Lambda function in Python
square = lambda x: x**2
print(square(3))


# Filter elements in list using list comrehensions
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)


# Multiple if conditions in list comprehensions
numbers = [1, 2, 3, 4, 5, 6]
filterd_numbers = [x for x in numbers if x % 2 == 0 and x > 2]
print(filterd_numbers)


# Creating dictionaries using list comprehensions
alpha = ['a', 'b', 'c']
numbers = [1, 2, 3]
my_final = {k: v for k, v in zip(alpha, numbers)}
print(my_final)


