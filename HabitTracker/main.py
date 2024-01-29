import requests
from datetime import datetime
from RainAlert import config

pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
    'token': config.TRACKER_TOKEN,
    'username': config.TRACKER_USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

graph_endpoint = f'{pixela_endpoint}/{user_params['username']}/graphs'

graph_config = {
    'id': 'graph1',
    'name': 'Days I code',
    'unit': 'day',
    'type': 'int',
    'color': 'kuro'
}

headers = {
    'X-USER-TOKEN': user_params['token']
}

#response = requests.post(pixela_endpoint, json=user_params, headers=headers)
#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(response.text)

pixel_creation_endpoint = f'{pixela_endpoint}/{user_params['username']}/graphs/{graph_config['id']}'

today = datetime.now()
yesterday = datetime(year=2024, month=1, day=28)

pixel_data = {
    'date': today.strftime('%Y%m%d'),
    'quantity': '6'
}

#response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
#print(response.text)

#UPDATE

update_endpoint = f'{pixela_endpoint}/{user_params['username']}/graphs/{graph_config['id']}/{pixel_data['date']}'

update_pixel = {
    'quantity': '10'
}

#response = requests.put(url=update_endpoint, json=update_pixel, headers=headers)
#print(response.text)

# DELETE

delete_endpoint = f'{pixela_endpoint}/{user_params['username']}/graphs/{graph_config['id']}/{pixel_data['date']}'
#response = requests.delete(url=update_endpoint, headers=headers)
#print(response.text)

