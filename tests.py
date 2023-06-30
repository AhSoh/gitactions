import os
import pathlib
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests
import time


def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()

driver = webdriver.Chrome()

####tests on index.html####
uri = file_uri("index.html")
driver.get(uri)

# test: links to Image Search and Advanced Search works
links = driver.find_elements(By.CLASS_NAME, "link")
for i in range(0, len(links)):
    links[i].click()
    print(driver.current_url)
    time.sleep(2)
    driver.back()
    links = driver.find_elements(By.CLASS_NAME, "link")
    time.sleep(2)

# test: type in query in search bar and click "Google Search" and "I'm feeling lucky" button
driver.find_element(By.ID, "searchbar").send_keys("harvard") #+ Keys.ENTER)
driver.find_element(By.ID, "searchbutton").click()
driver.implicitly_wait(3)

####tests on imagesearch.html####
uri = file_uri("imagesearch.html")
driver.get(uri)
driver.find_element(By.CLASS_NAME, "bar").send_keys("cats")
driver.find_element(By.CLASS_NAME, "button").click()
