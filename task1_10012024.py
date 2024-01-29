# PANCHAL BHOOMI
# TASK-1 10/01/24 MODIFIED

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class SubmissionAutomation:
    def __init__(self):
        self.driver = self.initialize_driver()
        self.postcode_text = "N1 0AA"
        self.email_address_text = "testemail@gmail.com"

    def initialize_driver(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument(r"C:\Users\bhoom\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
        chrome_options.add_argument('--ignore-certificate-errors')
        return webdriver.Chrome(options=chrome_options)

    def navigate_to_website(self, website_url):
        self.driver.get(website_url)

    def click_element(self, by, value):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((by, value)))
        element.click()

    def scroll_into_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def enter_text(self, by, value, text):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((by, value)))
        element.clear()
        element.send_keys(text)

    def process_all_addresses(self):
        i = 1
        while True:
            try:
                address_xpath = f'/html/body/div[2]/div[3]/div/div/div[3]/div/button[{i}]'
                address = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, address_xpath)))

                self.scroll_into_view(address)
                address_text = address.text
                address.click()
                time.sleep(2)

                self.driver.execute_script("window.scrollBy(0, 100);")

                email_bar_xpath = '/html/body/div[2]/div[1]/main/section[3]/div/section[2]/form/div[3]/div/input'
                self.enter_text(By.XPATH, email_bar_xpath, self.email_address_text)

                checkbox = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/main/section[3]/div/section[2]/form/div[4]/div/input')
                checkbox.click()

                submit_button_xpath = '/html/body/div[2]/div[1]/main/section[3]/div/section[2]/form/button/span'
                self.click_element(By.XPATH, submit_button_xpath)

                thank_you_message_xpath = '/html/body/div[2]/div[3]/div/div/div/h5'
                thank_you_message = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, thank_you_message_xpath)))

                print("Iteration:", i)
                print("Email successfully entered for address:", address_text)
                print("Email:", self.email_address_text)

                close_button_xpath = '/html/body/div[2]/div[3]/div/div/div/button[2]/span'
                self.click_element(By.XPATH, close_button_xpath)

                self.driver.execute_script("window.scrollBy(0, -100);")

                address_button_xpath = '/html/body/div[2]/div[1]/main/section[3]/div/section[1]/div[1]/button[1]'
                self.click_element(By.XPATH, address_button_xpath)

                search_bar_xpath = "/html/body/div[2]/div[1]/main/section[3]/div/section[2]/form/div[2]/div/input"
                self.click_element(By.XPATH, search_bar_xpath)

                postcode_input_xpath = "/html/body/div[2]/div[3]/div/div/div[2]/input"
                self.enter_text(By.XPATH, postcode_input_xpath, self.postcode_text)

                i += 1  

            except Exception as e:
                print(f"No more addresses found. {e}")
                break

    def run(self):
        website_url = 'https://www.ukpowernetworks.co.uk/who-is-my-electricity-supplier-and-what-is-my-mpan'
        self.navigate_to_website(website_url)

        address_button_xpath = '/html/body/div[2]/div[1]/main/section[3]/div/section[1]/div[1]/button[1]'
        self.click_element(By.XPATH, address_button_xpath)

        search_bar_xpath = "/html/body/div[2]/div[1]/main/section[3]/div/section[2]/form/div[2]/div/input"
        self.click_element(By.XPATH, search_bar_xpath)

        postcode_input_xpath = "/html/body/div[2]/div[3]/div/div/div[2]/input"
        self.enter_text(By.XPATH, postcode_input_xpath, self.postcode_text)

        self.process_all_addresses()

        self.driver.quit()

if __name__ == "__main__":
    automation = SubmissionAutomation()
    automation.run()
