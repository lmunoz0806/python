from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import xlrd
import pandas as pd
 
 
# You need Python, pip (selenium, xlrd, and panda) install on your computer
# Need to download your browser driver (https://chromedriver.chromium.org/downloads)
 
# Params
username = 'Your Username'
password = 'Your Password'
xlfile = "C:\\Users\\luis.munoz\\Downloads\\airwatch-data-list-3.xlsx"
chromeDriver="C:\\Users\\luis.munoz\\Downloads\\chromedriver_90\\chromedriver.exe"
url = 'https://cn274.awmdm.com/AirWatch/Login?ReturnUrl=%2FAirWatch%2F'
delay = 40
 
# Functions
def logintoAirwatch(username,password):
    #Login in to Airwatch
    #username
    usernameBox = driver.find_element_by_xpath('//*[@id="UserName"]')
    usernameBox.send_keys(username)
    nextButton = driver.find_element_by_xpath('//*[@id="loginform"]/div[4]')
    nextButton.click()
    time.sleep(1)
    #password
    passwordBox = driver.find_element_by_xpath('//*[@id="Password"]')
    passwordBox.send_keys(password)
    #Click on log in
    loginButton = driver.find_element_by_xpath('//*[@id="loginform"]/div[5]/input')
    loginButton.click()
    time.sleep(1)
    ####End of AUTH box###
 
def updateName(serial, newName):
    #Select List View
    listView = driver.find_element_by_xpath('//*[@id="submenu"]/ul[2]/li[2]/a')
    listView.click()
    time.sleep(7)
    #Search for device
    searchList = driver.find_element_by_xpath('//*[@id="SearchText"]')
    searchList.clear()
    searchList.send_keys(serial)
    searchList.send_keys(Keys.RETURN)
    time.sleep(5)
    #Select Device
    friendlyname = driver.find_element_by_xpath('//*[@id="FriendlyName"]/a')
    friendlyname.click()
    time.sleep(5)
    #Edit device name
    moreAction = driver.find_element_by_xpath('//*[@id="MoreActionsPopup"]')
    moreAction.click()
    time.sleep(1)
    editDevice = driver.find_element_by_xpath('//*[@id="maincolumn"]/hgroup/div[2]/div/section/div[5]/ul/li[2]/a')
    editDevice.click()
    time.sleep(1)
    #New Name
    deviceName= driver.find_element_by_xpath('//*[@id="FriendlyName"]')
    deviceName.clear()
    deviceName.send_keys(newName)
    #Save New Name
    time.sleep(1)
    #save = driver.find_element_by_xpath('//*[@id="airwatchdeviceseditdevice2208114"]/section/form/section/div/button[1]')
    save = driver.find_elements_by_css_selector('button.clr-button.button.large.emphasis.branded-highlight-bg.branded-highlight-item.js-ignore-settings-inheritance')[0]
    save.click()
 
# Step 1: Store CSV data
df = pd.read_excel(xlfile, dtype = {"serial": str, "newname": str})
 
# Step 2: Open Browser
driver = webdriver.Chrome(executable_path=chromeDriver)
driver.get(url)
 
# Step 3: Login
logintoAirwatch(username, password)
 
# Step 3: Loop through rows and update
for index, row in df.iterrows():
    if index == 0:
        updateName(row['serial'], row['newName'])
    else:
        time.sleep(delay)
        updateName(row['serial'], row['newName'])