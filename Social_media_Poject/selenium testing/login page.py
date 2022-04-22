from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class Test1:from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class Test1:
    def testmethod(self, dropdown=None):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("http://127.0.0.1:5000/")

        text = driver.find_element(By.NAME, "email")
        text.send_keys("sandhyajagan2000@gmail.com")
        print("value is" + text.get_attribute("value"))
        assert text.get_attribute("value") == "sandhyajagan2000@gmail.com"
        time.sleep(5)

        text = driver.find_element(By.NAME, "pass")
        text.send_keys("123456")
        print("value is" + text.get_attribute("value"))
        assert text.get_attribute("value") == "123456"
        time.sleep(5)

    def testmethod(self, dropdown=None):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("http://127.0.0.1:5000/")

        text = driver.find_element(By.NAME, "email")
        text.send_keys("sandhyajagan2000@gmail.com")
        print("value is" + text.get_attribute("value"))
        assert text.get_attribute("value") == "sandhyajagan2000@gmail.com"
        time.sleep(5)

        text = driver.find_element(By.NAME, "pass")
        text.send_keys("123456")
        print("value is" + text.get_attribute("value"))
        assert text.get_attribute("value") == "123456"
        time.sleep(5)
