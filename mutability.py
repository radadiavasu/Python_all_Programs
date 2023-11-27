friends_last_seen = {
    'Jay': 90,
    'Vasu': 5,
    'Kunj':20
}
print(id(friends_last_seen))

# 
friends_last_seen = {
    'Jay': 90,
    'Vasu': 5,
    'Kunj':20
}
print(id(friends_last_seen))

# 
friends_last_seen['Jay'] = 0  # friends_last_seen.__setitem__(self, 'Jay')
print(id(friends_last_seen))

# 
my_int = 1
print(id(my_int))

# 
my_int = my_int + 1
print(id(my_int))  # my_int.__iadd__(self, 1).  "__iadd__" method create new object every time while we add.
                   # after that my_int is immutable that you can not change.


# these are the immutable types in python.
# 1. integers -> all functions new int objects. you can not change int object.
# 2. floats
# 3. strings
# 4. tuple