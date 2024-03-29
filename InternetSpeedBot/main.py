from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from config import TWITTER_PASSWORD

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
ip_speed_url = 'https://www.speedtest.net/result/15932161620'
twitter_url = 'https://twitter.com/'

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_USERNAME = 'laresamdeola'


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.down = PROMISED_DOWN
        self.up = PROMISED_UP
        self.post = ''

    def get_internet_speed(self):
        self.driver.get(ip_speed_url)
        self.click_modal()
        current_down = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/'
                                                                'div[3]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[1]/'
                                                                'div/div[2]/span')
        current_up = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/'
                                                              'div[3]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/'
                                                              'div/div[2]/span')
        return [current_down.text, current_up.text]

    def click_modal(self):
        base_window = self.driver.window_handles[0]
        self.driver.switch_to.window(base_window)
        time.sleep(10)
        accept_button = self.driver.find_element(By.ID, value='onetrust-accept-btn-handler')
        accept_button.click()
        time.sleep(5)

    def login_twitter(self):
        self.driver.get(twitter_url)
        sign_in_button = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/'
                                                                  'div[1]/div/div/div[3]/div[5]/a/div')
        sign_in_button.click()
        time.sleep(2)
        base_window = self.driver.window_handles[0]
        self.driver.switch_to.window(base_window)
        username = self.driver.find_element(By.NAME, value='text')
        username.send_keys(TWITTER_USERNAME)
        next_button = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/'
                                                               'div[2]/div/div/div[2]/div[2]/div/div/div/div[6]')
        next_button.click()
        time.sleep(5)
        base_window = self.driver.window_handles[0]
        self.driver.switch_to.window(base_window)
        password = self.driver.find_element(By.NAME, value='password')
        password.send_keys(TWITTER_PASSWORD)
        time.sleep(2)
        login_button = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]'
                                                                '/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/'
                                                                'div/div')
        login_button.click()
        time.sleep(5)

    def post_twitter(self):
        post_box = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/'
                                                            'div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/'
                                                            'div[1]/div/div/div/div/div/div/div/div/div/div/label/'
                                                            'div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        post_box.send_keys(f'{self.post}: my download speed are {int(self.get_internet_speed()[0])}, while '
                           f'my upload speed {int(self.get_internet_speed()[1])}')
        post_button = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]'
                                                               '/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/'
                                                               'div[2]/div[2]/div/div/div/div[3]')
        post_button.click()
        time.sleep(5)

    def tweet_at_provider(self):
        self.get_internet_speed()
        time.sleep(5)
        self.login_twitter()
        time.sleep(5)
        self.post_twitter()
        time.sleep(5)
        return 'Successfully posted your internet speed'


speed_one = InternetSpeedTwitterBot()
speed_one.post = 'Here are my Internet Speed'
speed_one.tweet_at_provider()
