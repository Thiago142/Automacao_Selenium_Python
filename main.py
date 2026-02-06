from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
browser = webdriver.Chrome()

browser.get('http://www.google.com/')
time.sleep(5)

