from bs4 import BeautifulSoup as bs
import lxml

with open('website.html', encoding='utf8') as file:
    contents = file.read()

soup = bs(contents, features='lxml')
#print(soup.title.name)
#print(soup.body.p.a)

# Get all contents

all_anchor_tags = soup.find_all(name='a')
#print(all_anchor_tags)

for tag in all_anchor_tags:
    #print(tag.get_text())
    #print(tag.get('href'))
    pass

heading = soup.find(name='h1', id='name')
#print(heading.get_text())
sub_heading = soup.find_all(name='h3', attrs='heading')
#print(sub_heading)

# for sub in sub_heading:
#     print(sub.getText())

# Using select

heading_2 = soup.select_one('.heading')
#print(heading_2.getText())

heading_2_all = soup.select('.heading')
#print(heading_2_all)

for head in heading_2_all:
    print(head.getText())