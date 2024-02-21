from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
url = 'https://www.asos.com/pullbear/pullbear-classic-sunglasses-in-black/prd/206207012#colourWayId-206207013'

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

price_pounds = driver.find_element(By.CLASS_NAME, value="MwTOW")
print(f'The price is {price_pounds.text}')

# driver.close()
#driver.quit()
