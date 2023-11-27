from collections import deque

friends = deque(('Jay', 'Vasu', 'Kunj', 'Priyanka', 'Rose'))

def get_friends():
    yield from friends
 
    
def greet(g):
    while True:
        try:
            friend = next(g)
            yield f'HELLO {friend}'
        except StopIteration:
            pass

friends_generator = get_friends()
g = greet(friends_generator)
print(next(g))
print(next(g))

# #################################################
# c = get_friends()
# print(next(c))
# print(next(c))