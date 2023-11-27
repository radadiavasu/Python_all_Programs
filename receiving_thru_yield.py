from collections import deque

friends = deque(('Jay', 'Vasu', 'Kunj', 'Priyanka', 'Rose'))


def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield
        print(f'{greeting} {friend}')


def greet(g):
    yield from g


greeter = greet(friend_upper())
greeter.send(None)
greeter.send('Hello')
print('Hello, world! Multitasking...')
greeter.send('How are you,')


#############################################
# def greet():
#     friend = yield
#     print(f'Hello, {friend}')
    
# g = greet()
# g.send(None)
# g.send('Vasu')