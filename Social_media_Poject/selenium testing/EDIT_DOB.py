from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class Test6:
    def testmethod(self, dropdown=None):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("http://127.0.0.1:5000/editdob")

        text = driver.find_element(By.NAME, "ndob")
        text.send_keys("2001-08-24")
        print("value is" + text.get_attribute("value"))
        assert text.get_attribute("value") == "2001-08-24"
        time.sleep(5)
