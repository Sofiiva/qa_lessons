import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s=Service('./chromedriver/chromedriver.exe')
driver=webdriver.Chrome(service=s)

driver.get("https://guru.qahacking.ru/")
driver.execute_script("window.scrollTo(0, 5000)")
driver.find_element(By.ID, "mod-rscontact-email-91").send_keys("november@yopmail.com")
driver.find_element(By.ID, "mod-rscontact-submit-btn-91").click()
if driver.find_element(By.ID, "mod-rscontact-submit-btn-91"):print("\033[31m{}\033[0m".format("FAIL"))
time.sleep(1)
driver.save_screenshot("TC-3.2.png")