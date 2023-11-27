import requests
from bs4 import BeautifulSoup

page = requests.get('http://www.example.com')
# print(page.content)
soup = BeautifulSoup(page.content, 'html.parser')

print(soup.find('title').string)
print(soup.select_one('p a').attrs['href'])