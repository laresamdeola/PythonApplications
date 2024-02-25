from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
url = 'https://secure-retreat-92358.herokuapp.com/'
ip_speed_url = 'https://www.speedtest.net/result/15932161620'

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = 'laresamdeola@gmail.com'
TWITTER_PASSWORD = 'Dhlawrence27#'


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.down = PROMISED_DOWN
        self.up = PROMISED_UP

    def get_internet_speed(self):
        self.driver.get(ip_speed_url)
        self.click_modal()
        current_down = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[1]/div/div[2]/span')
        current_up = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[2]/span')
        return [current_down.text, current_up.text]

    def tweet_at_provider(self):
        pass

    def click_modal(self):
        base_window = self.driver.window_handles[0]
        #current_window = self.driver.window_handles[1]
        self.driver.switch_to.window(base_window)
        time.sleep(10)
        accept_button = self.driver.find_element(By.ID, value='onetrust-accept-btn-handler')
        accept_button.click()
        time.sleep(5)
        # self.driver.switch_to.window(base_window)


speed_one = InternetSpeedTwitterBot()
print(speed_one.get_internet_speed())
# driver = webdriver.Chrome(options=chrome_options)
# driver.get(url)