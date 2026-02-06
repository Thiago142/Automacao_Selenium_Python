from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
browser = webdriver.Chrome()

browser.get('https://www.google.com/')
time.sleep(5)

