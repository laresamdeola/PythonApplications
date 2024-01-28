import requests
from twilio.rest import Client
from RainAlert import config
from config_stock import AV_API_KEY, NEWS_API_KEY


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
AV_API_KEY = AV_API_KEY
NEWS_API_KEY = NEWS_API_KEY
TWILIO_API_KEY = config.TWILIO_AUTH_TOKEN
TWILIO_SID = config.account_sid

news_parameters = {
    'apiKey': NEWS_API_KEY,
    'q': 'Tesla',
    'from': '2024-01-01',
    'to': '2024-01-28',
    'pageSize': 10
}

stock_parameters = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK_NAME,
    'apikey': AV_API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
#print(response.url)
data = response.json()['Time Series (Daily)']

data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data['4. close']
print(yesterday_closing_price)

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data['4. close']

difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = '🔻'
if abs(difference) > 0:
    up_down = '⬆️'

percentage_difference = (difference / float(yesterday_closing_price)) * 100
print(percentage_difference)

news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
news_data = news_response.json()
#print(news_data['articles'][0:3])
#print(news_response.url)
#print(news_response.json())

news_articles = []

if percentage_difference < 5.0:
    for i in range(0, 3):
        news_articles.append(news_data['articles'][i]['title'] + '\n' + news_data['articles'][i]['author'] + '\n' +
                             news_data['articles'][i]['url'] + '\n')
else:
    print('Not relevant news for now')

client = Client(TWILIO_SID, TWILIO_API_KEY)
message = client.messages.create(body=f'{STOCK_NAME}:  {up_down} {round(percentage_difference, 2)}%\n{news_articles[0]}', from_='+447723352157', to='+447828322303')
print(message.status)

