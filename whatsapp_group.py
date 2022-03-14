import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def group_add(name):
    l=[]
    with open('Samples/people.csv','rt')as f:
      data = csv.reader(f)
      for row in data:
          if row[1] != "Given Name":
              if row[1]:
                  l.append(row[1])
    print(l)
    open('geckodriver.exe','rt')
    driver = webdriver.Firefox()
    driver.maximize_window()
    r=driver.get('https://web.whatsapp.com/')
    time.sleep(20)
    try:
        driver.find_element_by_xpath('//*[@title="{}"]'.format(name)).click()# name of the group
    except:
        print("WhatsApp group doesn't exist")
        print("Please Try again")
        return
    f = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,'//*[@class="_2rlF7"]')))
    f.click()
    f = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,'//*[@class="_3vPI2"]')))
    f.click()
    """
    driver.find_elements_by_class_name("_2rlF7")[0].click()
    time.sleep(25)
    driver.find_elements_by_class_name("_3vPI2")[0].click()
    """
    for i in l :
        driver.find_element_by_xpath('//*[@class="_13NKt copyable-text selectable-text"]').send_keys(i)
        time.sleep(5)
        driver.find_element_by_xpath('//*[@title="{}"]'.format(i)).click()

    driver.find_element_by_xpath('//*[@data-icon="checkmark-medium"]').click()
    time.sleep(5)
    f = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,'//*[@class="_20C5O _2Zdgs"]')))
    f.click()
    return

name=input("Enter the name of the WhatsApp group you want to add people to")
group_add(name)
