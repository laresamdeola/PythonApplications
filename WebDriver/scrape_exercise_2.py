from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
url = 'https://en.wikipedia.org/wiki/Main_Page'

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

article_count = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]')
print(article_count.text)

driver.close()