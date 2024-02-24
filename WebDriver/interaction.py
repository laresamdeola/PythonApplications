from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
url = 'https://en.wikipedia.org/wiki/Main_Page'

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

# Click Buttons
all_portals = driver.find_element(By.LINK_TEXT, value='Content portals')
all_portals.click()

# Finding the 'Search' <input> by Name
search = driver.find_element(By.NAME, value='search')

# Sending keyboard input to Selenium
search.send_keys('Python', Keys.ENTER)
