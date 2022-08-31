from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def gethtml(url):
    ser = Service("./chromedriver.exe")
    op = webdriver.ChromeOptions()
    op.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=ser, options=op)
    driver.get(url)
    page = driver.page_source
    driver.close()
    return page