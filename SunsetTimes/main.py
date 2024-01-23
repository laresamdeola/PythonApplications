import requests
from datetime import datetime

URL = 'https://api.sunrise-sunset.org/json'
LATITUDE = 36.7201600
LONGITUDE = -4.4203400
parameters = {
    "lat": LATITUDE,
    "lng": LONGITUDE,
    "formatted": 0
}

response = requests.get(url=URL, params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data['results']['sunrise'].split("T")[1].split(":")[0]
sunset = data['results']['sunset'].split("T")[0].split(":")[0]


time = datetime.now()
print(time.hour)