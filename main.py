# this program is to grab a text from a web page
# reference: Automate Everything with Python Course (Udemy)
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from webdriver_manager.chrome import ChromeDriverManager


def get_driver():
    # add options to the webdriver object to make it more effective.
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument("no-sandbox")
    options.add_argument("disable-blink-features=AutomationControlled")

    # options and service are positional arguments, service is used to install chrome compatible chromedriver
    chrome_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    chrome_driver.get("https://automated.pythonanywhere.com/")
    return chrome_driver


def get_element(chrome_driver):
    element = chrome_driver.find_elements(by="xpath", value="/html/body/div[1]/div/h1[1]")
    print(element[0].text)


if __name__ == "__main__":
    driver = get_driver()
    get_element(driver)
    # Close the webpage after text parsing is done.
    time.sleep(2)
    driver.close()
