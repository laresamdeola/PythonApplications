from config import APP_ID, API_KEY
import requests
from datetime import datetime


time = datetime.now()

API_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'

query_string = input('Tell me which exercises you did: ')

nutrition_parameters = {
    'query': query_string
}

options = {
    'url': API_ENDPOINT,
    'headers': {
        'Content-Type': 'application/json',
        'x-app-id': APP_ID,
        'x-app-key': API_KEY,
    }
}

response = requests.post(url=options['url'], headers=options['headers'], json=nutrition_parameters)
response.raise_for_status()
nutrition_data = response.json()
# print(nutrition_data)
# print(nutrition_data['exercises'][0]['name'])
# print(nutrition_data['exercises'][0]['duration_min'])
# print(nutrition_data['exercises'][0]['nf_calories'])

sheety_endpoint = 'https://api.sheety.co/d875da4dd9bf749bb9fc338f4efe3afd/myWorkouts2/sheet1'

# 1tyqNcY1K_PYdNIG_B1S4j2OXC1PkmaevmIzY8HdY_Ko

for exercise in nutrition_data['exercises']:
    body = {
        'sheet1': {
            'date': time.strftime('%d/%m/%Y'),
            'time': time.strftime('%T'),
            'exercise': exercise['name'].title(),
            'duration': exercise['duration_min'],
            'calories': exercise['nf_calories']
        }
    }

    sheet_response = requests.post(sheety_endpoint, json=body)
    print(sheet_response.text)

'''
sheety_response = requests.get(sheety_endpoint)
sheety_response.raise_for_status()
sheety_data = sheety_response.json()
print(sheety_data)
'''




