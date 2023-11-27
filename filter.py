# def starts_with_r(friend):
#     return friend.startswith('R')

# friends = ['Rose', 'Jay', 'Ruhani', 'Rohan', 'Vasu']
# starts_with_r = filter(starts_with_r, friends)

# print(next(starts_with_r))
# print(next(starts_with_r))
# print(next(starts_with_r))


# friends = ['Rose', 'Jay', 'Ruhani', 'Rohan', 'Vasu']
# starts_with_r = my_custom_filter(lambda friend: friend.startswith('R'), friends)

# another_starts_with_r = (f for f in friends if f.startswith('R'))

# def my_custom_filter(func, iterable):
#     for i in iterable:
#         if func(i):
#             yield i


friends = ['Rose', 'Jay', 'Ruhani', 'Rohan', 'Vasu']
starts_with_r = filter(lambda friend: friend.startswith('R'), friends)

another_starts_with_r = (f for f in friends if f.startswith('R'))

friends_lower = map(lambda x: x.lower(), friends)

friends_lower = [friend.lower() for friend in friends]
friends_lower = (friend.lower() for friend in friends)

print(next(friends_lower))

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
@classmethod
def from_dict(cls, data):
    return cls(data['username'], data['password'])

users = [
    {'username': 'vasu', 'password': 'vasu123'},
    {'username': 'vasuradadia', 'password': 'vasu'}
]

users = [User.from_dict(user) for user in users]
users = map(User.form_dict(users))