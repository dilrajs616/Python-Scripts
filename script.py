from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os
import time

class WebScraper():

    def __init__(self) -> None:
        self.get_variables()
        self.get_driver()
        self.login()
        self.call_scraper()

    def get_variables(self):
        load_dotenv()
        self.link = os.getenv('LINK')
        self.driver_path = os.getenv("DRIVER_PATH")
        self.username = os.getenv("USERNAME")
        self.password = os.getenv("PASSWORD")

    def get_driver(self):
        self.service = Service(executable_path=self.driver_path)
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.get(self.link)
        self.driver.implicitly_wait(10)
    
    def login(self):
        username_field = self.driver.find_element(By.ID, "userName")
        password_field = self.driver.find_element(By.ID, "txtpassword")

        username_field.send_keys(self.username)
        password_field.send_keys(self.password)

        password_field.send_keys(Keys.RETURN)

    def call_scraper(self):
        while True:
            self.scraper()
            time.sleep(5)

    def scraper(self):
        print("working")

if __name__ == "__main__":
    scraper = WebScraper()