from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
url = 'https://www.asos.com/pullbear/pullbear-classic-sunglasses-in-black/prd/206207012#colourWayId-206207013'

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

price_pounds = driver.find_element(By.CLASS_NAME, value="MwTOW")

# Searching with Selenium
# search_bar = driver.find_element(By.NAME, value='q')
# print(search_bar.get_attribute('placeholder'))
# button = driver.find_element(By.ID, value='submit')
# print(button.size)

documentation_link = driver.find_element(By.CSS_SELECTOR, value='documentation_widget p')
print(documentation_link.text)

bug_link = driver.find_element(By.XPATH, value='XPATH LINK')
print(bug_link.text)


print(f'The price is {price_pounds.text}')

# driver.close()
#driver.quit()
