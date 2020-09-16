from selenium import webdriver 
from getpass import getpass
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import datetime
import time
from selenium.webdriver.common.by import By
#get current date time
current_time = datetime.datetime.now()
#create filename
filename = str("cart_" + str(current_time.month) + "-" + str(current_time.day) + "-" + str(current_time.year) + ".csv")
#open file and specify write 
f = open(filename,"w")
headers = "product_name, product_price\n" #headers of the file
f.write(headers)
#credentials
username = "tuenguyen12329@gmail.com"
password = "Phuonganh#1107"
#get driver from 
driver = webdriver.Chrome("C:\\webdriver\\chromedriver.exe")
driver.get("https://www.amazon.ca/")
#enter credentials
cart = driver.find_element_by_id("nav-cart")
cart.click()

signin_account = driver.find_element_by_id("a-autoid-0-announce")
signin_account.click()

username_textbox = driver.find_element_by_id("ap_email")
username_textbox.send_keys(username)

continue_button = driver.find_element_by_id("continue")
continue_button.submit()

password_textbox = driver.find_element_by_id("ap_password")
password_textbox.send_keys(password)

signin_button = driver.find_element_by_id("signInSubmit")
signin_button.submit()
#put program to sleep for 30 secs to validate login from phone
time.sleep(30)
#find names and prices 
names = driver.find_elements(By.XPATH,"//span[contains(@class,'a-size-medium') and contains(@class, 'sc-product-title') and contains(@class, 'a-text-bold')]")
prices = driver.find_elements(By.XPATH,"//span[contains(@class, 'a-size-medium') and contains(@class, 'a-color-base') and contains(@class, 'sc-price') and contains(@class, 'sc-white-space-nowrap') and contains(@class, 'sc-product-price') and contains(@class, 'a-text-bold')]")
i = 0
for name in names:
    print(name.text.replace(",", "|"))
    print(prices[i].text)
    f.write(name.text.replace(",","|") + "," + prices[i].text + "\n")
    i = i + 1
    
