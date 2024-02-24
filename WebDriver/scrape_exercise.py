from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
url = 'https://www.python.org/'

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

python_events = driver.find_elements(By.CSS_SELECTOR, value='.event-widget .menu li')

python_org_events = {}

for index, event in enumerate(python_events):
    event_details = event.text.split()
    time = ''.join(event_details[0])
    name = ' '.join(event_details[1:])
    python_org_events[index] = {
        'time': time,
        'name': name
    }

print(python_org_events)

driver.close()


