from bs4 import BeautifulSoup as bs
import lxml
import requests
import pandas as pd

response = requests.get('https://news.ycombinator.com/news')
yc_webpage = response.text
soup = bs(yc_webpage, features='lxml')

#yc_news = soup.find_all(name='td', class_='title')
article_tag = soup.find_all('span', class_='titleline', limit=100)
#article_text = article_tag.get_text()
article_link = soup.find_all('a', limit=100)
article_score = soup.find_all('span', class_='score', limit=100)

yc_news_titles = []
yc_news_links = []
yc_news_scores = []
yc_news = []

for title in article_tag:
    titles = title.get_text()
    yc_news_titles.append(titles)

for link in article_link[0:30]:
    links = link.get('href')
    yc_news_links.append(links)

for score in article_score:
    scores = score.get_text()
    yc_news_scores.append(int(scores.split()[0]))

yc = pd.DataFrame({
    'title': yc_news_titles,
    'links': yc_news_links,
    'scores': yc_news_scores
})

print(yc.sort_values('scores'))

