friends = [
    {
        'username': 'vasu',
        'location': 'Ahmedabad'
     },
    {
        'username': 'kshitij',
        'location': 'Thunder Bay, Canada'
     },
    {
        'username': 'kunj',
        'location': 'Ahmedabad'
     },
    {
        'username': 'jay',
        'location': 'Ahmedabad'
     },
]

your_location = input('Where are you right now? ')
friends_nearby = [
    friend for friend in friends if friend['location'] == your_location]

if any(friends_nearby) > 0:
    print('You are not alone!')
else:
    print("I couldn't found your location!!!")
