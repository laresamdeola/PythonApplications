import requests
from twilio.rest import Client
from config import TWILIO_AUTH_TOKEN, OWM_API_KEY, account_sid


weather_parameters = {
    'lat': 53.578461,
    'lon': -2.429840,
    'appid': OWM_API_KEY,
    'cnt': 4
}
OWM_endpoint = 'https://api.openweathermap.org/data/2.5/forecast'


response = requests.get(OWM_endpoint, params=weather_parameters)
response.raise_for_status()
weather_data = response.json()
#print(weather_data)

will_rain = False


for hour_data in weather_data['list']:
    condition_code = hour_data['weather'][0]['id']
    if 501 <= int(condition_code) <= 531:
        will_rain = True

if will_rain:
    client = Client(account_sid, TWILIO_AUTH_TOKEN)
    message = client.messages.create(body='It is going to rain today', from_='+447723352157', to='+447828322303')
    print(message.status)
else:
    client = Client(account_sid, TWILIO_AUTH_TOKEN)
    message = client.messages.create(body='It is not going to rain today', from_='+447723352157', to='+447828322303')
    print(message.status)
