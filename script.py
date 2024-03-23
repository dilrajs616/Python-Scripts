from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
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
        self.auth_link = os.getenv('AUTH_LINK')
        self.driver_path = os.getenv("DRIVER_PATH")
        self.username = os.getenv("USERNAME")
        self.password = os.getenv("PASSWORD")
        self.maker_link = os.getenv("MAKER_LINK")

    def get_driver(self):
        self.service = Service(executable_path=self.driver_path)
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.get(self.auth_link)
        self.driver.implicitly_wait(10)
    
    def login(self):
        username_field = self.driver.find_element(By.ID, "userName")
        password_field = self.driver.find_element(By.ID, "txtpassword")

        username_field.send_keys(self.username)
        password_field.send_keys(self.password)
        password_field.send_keys(Keys.RETURN)

        time.sleep(2)
        self.driver.get(self.maker_link)
        print("Current URL : ", self.driver.current_url)

    def call_scraper(self):
        # old_transactions = self.scraper()
        
        # while True:
        #     new_transactions = self.scraper()
        #     if new_transactions != old_transactions:
        #         old_transactions = new_transactions
        #         self.send_alert()
        #     time.sleep(5)

        self.scraper()

    def scraper(self):
        # time.sleep(5) 
        # pagination_wrapper = self.driver.find_element(By.CLASS_NAME, "paginations-wrapper")
        # pagination_text = pagination_wrapper.text
        # total_items = pagination_text.split()[-3]
        # return total_items

        time.sleep(5)  # Adjust the sleep duration as needed

        # Get the page source
        page_source = self.driver.page_source

        # Create a BeautifulSoup object
        soup = BeautifulSoup(page_source, 'html.parser')

        # Find the div element with class non-table-03
        div_non_table_03 = soup.find('div', class_='non-table-03')

        if div_non_table_03:
            # Print the content of the div
            print("Data from div with class non-table-03:")
            print(div_non_table_03.get_text())
    
    def send_alert(self):
        # Write code to send alerts however you like
        pass


if __name__ == "__main__":
    scraper = WebScraper()