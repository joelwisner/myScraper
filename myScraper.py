# Scraping myServices
# This file uses Selinium to scrape 
from selenium import webdriver
import getpass
import time

debugMode = 1  # set to 0 to turn off debug mode, 1 to turn on

# URLs
myServicesHomeURL = "https://myservices.servicenowservices.com/home"
myServicesITReqURL = "https://myservices.servicenowservices.com/home?id=ms_cat_item&sys_id=862141d8db02b2049886fb0e0f96190a"

# user info
userPrompt = "Enter myServices username:"
myServicesUname = input(userPrompt)
passPrompt = "Enter myServices password for user " + myServicesUname + ":"
mfaPrompt = "Enter MFA code from your authenticator app:"
myServicesPword = getpass.getpass(prompt=passPrompt)

# initiate the driver for Chrome and load myServices home page
driver = webdriver.Chrome(executable_path="C:\\Program Files\Google\chromedriver.exe")
driver.get(myServicesHomeURL)

unameFieldElement = driver.find_element_by_id("username")
pwordFieldElement = driver.find_element_by_id("password")
submitButtonElement = driver.find_element_by_name("login")

if(debugMode):
    debugName1 = unameFieldElement.tag_name
    debugName2 = pwordFieldElement.tag_name
    debugName3 = submitButtonElement.tag_name
    print("unameFieldElementID is " + debugName1)
    print("pwordFieldElementID is " + debugName2)
    print("submitButtonElementID is " + debugName3)

# we have the login page elements, now fill and submit

unameFieldElement.send_keys(myServicesUname)
pwordFieldElement.send_keys(myServicesPword)
submitButtonElement.click()
myServicesUname = "" # clear this variable after use
myServicesPword = "" # clear this variable after use

# put in a little 3 sec delay for MFA page load
time.sleep(3)

# now we are on the MFA page, get the field, button, fill and click
mfaFieldElement = driver.find_element_by_id("txtResponse")
mfaButtonElement = driver.find_element_by_id("sysverb_validate_mfa_code")

if(debugMode):
    debugName4 = mfaFieldElement.tag_name
    debugName5 = mfaButtonElement.tag_name
    print("DEBUG mfaFieldElement tag is " + debugName4)
    print("DEBUG mfaButtonElement tag is " + debugName5)


mfaCode = getpass.getpass(prompt=mfaPrompt)

mfaFieldElement.send_keys(mfaCode)
mfaButtonElement.click()
mfaCode = "" # clear this variable after use

# go directly to the IT Services request page
driver.get(myServicesITReqURL)

if(debugMode):
    print("DEBUG the script exited - JHW")


