import re

email = 'vasu@gmail.com'
expression = '[a-z\.]+'

matches = re.findall(expression, email)
print(matches)

name = matches[0]
domain = f'{matches[1]}'

print(name)
print(domain)

price = 'Price: $689.90'
expression = 'Price: \$([0-9,]*\.[0-9]*)'

matches = re.search(expression, price)

print(matches.group(0)) # entire match
print(matches.group(1)) # first thing in brackets

price_without_comma = matches.group(1).replace(',', '')
price_number = float(price_without_comma)
print(price_number)