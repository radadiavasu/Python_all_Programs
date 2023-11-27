"""
* counter
* defaultdict
* orderdict
* namedtuple
* deque
"""

# counter
from collections import Counter

device_tempratures = [13.5, 14.0, 14.5, 15.0, 15.0, 15.5, 16.0]

temprature_counter = Counter(device_tempratures)
print(temprature_counter[15.0])


# defaultdict
from collections import defaultdict

coworkers = [('Jay', 'IIM'), ('Vasu', 'IIT'), ('Kunj', 'Indus'), ('Priyanka', 'Parul')]

alma_meterss = defaultdict(list)

for coworker, place in coworkers:
    alma_meterss[coworker].append(place)
    
# alma_meterss.default_factory = int  # it gives us default 0 value if we could not defined into a particular list.   
    
print(alma_meterss['Vasu'])
print(alma_meterss['Rolf'])


# orederdict
from collections import OrderedDict

o = OrderedDict()
o['Vasu'] = 10
o['kunj'] = 5
o['Jay'] = 7

print(o)

o.move_to_end('Vasu')
o.move_to_end('Jay', last=False)

print(o)

o.popitem()

print(o)


# namedtuple
from collections import namedtuple

account = ('Checking', 1457.90)

Account = namedtuple('Account', ['name', 'balance'])

accountNamedTuple = Account(*account)

print(accountNamedTuple._asdict())


# deque

from collections import deque

friends = deque(('Vasu', 'Jay', 'Kunj', 'Priyanka'))
friends.appendleft('parth')

print(friends)

friends.pop()
friends.popleft()
print(friends)