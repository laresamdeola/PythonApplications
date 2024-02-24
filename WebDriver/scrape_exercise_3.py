from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
url = 'https://secure-retreat-92358.herokuapp.com/'

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

first_name = driver.find_element(By.NAME, value='fName')
first_name.send_keys('Lare', Keys.ENTER)
last_name = driver.find_element(By.NAME, value='lName')
last_name.send_keys('Adeola', Keys.ENTER)
email = driver.find_element(By.NAME, value='email')
email.send_keys('l.adeola@gmail.com', Keys.ENTER)

submit_button = driver.find_element(By.XPATH, value='/html/body/form/button')
submit_button.click()

driver.quit()
