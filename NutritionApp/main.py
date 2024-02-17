from config import APP_ID, API_KEY
import requests

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
print(f'You have burnt {nutrition_data['exercises'][0]['nf_calories']} calories.')