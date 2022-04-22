from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class Test5:
    def testmethod(self, dropdown=None):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("http://127.0.0.1:5000/editbio")

        text = driver.find_element(By.NAME, "nbio")
        text.send_keys("YOU BE YOURSELF!!! AND SHINE MORE")
        print("value is" + text.get_attribute("value"))
        assert text.get_attribute("value") == "YOU BE YOURSELF!!! AND SHINE MORE"
        time.sleep(5)


