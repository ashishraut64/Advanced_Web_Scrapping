from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

Options = Options()
Options.add_experimental_option("detach", True)
s = Service('C:/Users/ASHISH SANJAY RAUT/Desktop/chromedriver_win32/chromedriver.exe')
driver = webdriver.Chrome(service=s, options=Options)
driver.get("https://www.fundsindia.com/a/all-mutual-funds")
driver.find_element(by=By.XPATH,value='//*[@id="searchsummary"]/div/div/ul/li[3]/div').click()
time.sleep(5)
driver.find_element(by=By.XPATH, value='//*[@id="cate"]/option[1]').click()
time.sleep(1)

old_height = driver.execute_script('return document.body.scrollHeight')
time.sleep(3)
while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(3)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height==old_height:
        break
    old_height=new_height
time.sleep(15)

html = driver.page_source
with open('Mutual_Funds1.html','w',encoding='utf-8') as f:
    f.write(html)









