from selenium import webdriver
from selenium.webdriver.common.by import By
import time



class Rushi:
    driver = webdriver.Chrome("C:\\Users\\DELL\\PycharmProjects\\pythonProject2\\selenium driver\\chromedriver")

    def login(self):
        username = "rushi_javalkar"
        password = "12345678"

        username_xpath = "input[name='username']"
        password_xpath = "input[name='password']"
        login_button_xpath ="body > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > section:nth-child(1) > main:nth-child(2) > article:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(1) > div:nth-child(3)"

        try:
            self.driver.get(url)
            self.driver.maximize_window()
            self.driver.implicitly_wait(5)
            username_xpath = self.driver.find_element(By.CSS_SELECTOR, value=username_xpath)
            password_xpath = self.driver.find_element(By.CSS_SELECTOR, value=password_xpath)
            login_button_xpath = self.driver.find_element(By.CSS_SELECTOR, value=login_button_xpath)

            username_xpath.send_keys("rushi_javalkar")
            password_xpath.send_keys("12345678")
            login_button_xpath.click()
            self.driver.quit()


        except:
            print("ERROR : Xpath Not  Found !")



r = Rushi()
url = 'https://www.instagram.com/'
r.login()

