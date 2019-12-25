from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.by import By
import time
import csv
l=[]
with open('Samples/people.csv','rt')as f:
  data = csv.reader(f)
  for row in data:
      l.append(row[1])
driver = webdriver.Firefox()
s=time.time()
r=driver.get('https://web.whatsapp.com/')
time.sleep(20)
driver.find_element_by_xpath('//*[@title="DH j.g g"]').click()# name of the group
time.sleep(15)
driver.find_elements_by_class_name("_3V5x5")[0].click()
time.sleep(15)
driver.find_elements_by_class_name("_3p0T6")[0].click()
for i in l:
    driver.find_element_by_xpath('//*[@title="Search…"]').send_keys(i)
    time.sleep(5)
    driver.find_element_by_xpath('//*[@title="{}"]'.format(i)).click()
    #time.sleep(5)

driver.find_element_by_xpath('//*[@data-icon="checkmark-light"]').click()
time.sleep(5)

