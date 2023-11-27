from bs4 import BeautifulSoup

SIMPLE_HTML = '''<html>
<head></head> 
<body>
    <h1>This is title</h1>
    <p class="subtitle">Hi my name is Vasu.</p>
    <p>Here's another p without a class</p>
<ul>
    <li>Vasu</li>
    <li>Kunj</li>
    <li>Jay</li>
    <li>Parth</li>
</ul>
</body>
</html>'''

simple_soup = BeautifulSoup(SIMPLE_HTML, 'html.parser')

# print(simple_soup.find('h1').string)

def find_title():
    h1_tag = simple_soup.find('h1')
    print(h1_tag.string)
    
def find_li():
    li_tag = simple_soup.find_all('li')
    li_contants = [e.string for e in li_tag]
    print(li_contants)
    
def find_subtitle():
    paragraph = simple_soup.find('p', {'class': 'subtitle'})
    print(paragraph.string)
    
def find_other_paragraph():
    paragraphs = simple_soup.find_all('p')
    other_paragraph = [p for p in paragraphs if 'subtitle' not in p.attrs.get('class', [])]
    print(other_paragraph[0].string)
    
find_title()
find_li()
find_subtitle()
find_other_paragraph()