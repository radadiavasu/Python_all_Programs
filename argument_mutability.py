friends_last_seen = {
    'Jay': 20,
    'Vasu': 5,
    'Kunj':2
}

def see_friends(friends, name):
    print(friends is friends_last_seen)  # print(id(friends))
    friends[name] = 0
    
# print(id(friends_last_seen))
# print(id(friends_last_seen['Jay']))

see_friends(friends_last_seen, 'Jay')

# print(id(friends_last_seen['Jay']))
# print(id(friends_last_seen))