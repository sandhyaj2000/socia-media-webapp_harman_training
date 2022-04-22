from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class Test2:
    def testmethod(self, dropdown=None):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("http://127.0.0.1:5000/signup")

        text = driver.find_element(By.NAME, "fname")
        text.send_keys("Sandhya")
        print("value is " + text.get_attribute("value"))
        assert text.get_attribute("value") == "Sandhya"
        time.sleep(5)

        text = driver.find_element(By.NAME, "lname")
        text.send_keys("j")
        print("value is " + text.get_attribute("value"))
        assert text.get_attribute("value") == "j"
        time.sleep(5)

        text = driver.find_element(By.NAME, "uname")
        text.send_keys("sandhyaj2000")
        print("value is " + text.get_attribute("value"))
        assert text.get_attribute("value") == "sandhyaj2000"
        time.sleep(5)

        text = driver.find_element(By.NAME, "email")
        text.send_keys("sandhyajagan2000@gmail.com")
        print("value is" + text.get_attribute("value"))
        assert text.get_attribute("value") == "sandhyajagan2000@gmail.com"
        time.sleep(5)

        text = driver.find_element(By.NAME, "phone")
        text.send_keys("9686531897")
        print("value is" + text.get_attribute("value"))
        assert text.get_attribute("value") == "9686531897"
        time.sleep(5)

        text = driver.find_element(By.NAME, "dob")
        text.send_keys("2000-03-08")
        print("value is" + text.get_attribute("value"))
        assert text.get_attribute("value") == "2000-03-08"
        time.sleep(5)

        text = driver.find_element(By.NAME, "addr")
        text.send_keys("Kr puram,bengaluru")
        print("value is" + text.get_attribute("value"))
        assert text.get_attribute("value") == "Kr puram,bengaluru"
        time.sleep(5)

        text = driver.find_element(By.NAME, "pass")
        text.send_keys("123456")
        print("value is" + text.get_attribute("value"))
        assert text.get_attribute("value") == "123456"
        time.sleep(5)

        text = driver.find_element(By.NAME, "cnfpass")
        text.send_keys("123456")
        print("value is" + text.get_attribute("value"))
        assert text.get_attribute("value") == "123456"
        time.sleep(5)

        text = driver.find_element(By.NAME, "bio")
        text.send_keys("As a man thinks in his heart so is he.What you think you become!!!!!!!")
        print("value is" + text.get_attribute("value"))
        assert text.get_attribute("value") == "As a man thinks in his heart so is he.What you think you become!!!!!!!"
        time.sleep(5)

        res = driver.find_element(By.XPATH, "//label[@for='dot-2']").is_selected()

        print(res)





