from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.devtools import *

from api_automation import *
from Url_Base import *

import requests

import time

# Set up Chrome options
def connect_to_debug_port(port):
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", f"localhost:{port}")  # Specify the debug port

    # Launch Chrome using the configured options 
    # tim driver tuong ung o link https://googlechromelabs.github.io/chrome-for-testing/latest-versions-per-milestone-with-downloads.json
    path_to_chromedriver = 'D:/pythons/selenium_python_custom/chromedriver-win32/chromedriver.exe'
    service = Service(executable_path=path_to_chromedriver)
    # Launch Chrome using the configured options
    driver = webdriver.Chrome(service=service, options=chrome_options)
    print("Conect port success")
    return driver

#driver = connect_to_debug_port(5456)

# _get = GET_Custom(GET_LIST_PROFILE .format(page=1,limit=1))
# print("--->  ",_get)

#driver.quit()

########## go to url 
def GotoUrl(driver,url):
    driver.get(url)
    for req in driver.requests:
        if req.response:
            print("-- METHOD -- ",req.method)
    return driver

########## check xpath is exit
def HasElementXpath(driver,element):
    try:
        driver.find_element(By.XPATH,element)
        return True
    except:
        return False

########## check Selector is exit
def HasElementSelector(driver,element):
    try:
        driver.find_element(By.CSS_SELECTOR,element)
        return True
    except:
        return False


########## find xpath
def FindElementXpath(driver,element):
    findXpath = driver.find_element(By.XPATH,element)
    return findXpath

########## find Selector
def FindElementSelector(driver,element):
    findSelector = driver.find_element(By.CSS_SELECTOR,element)
    return findSelector

########## click element
def ClickElement(findElement):
    try:
        findElement.click()
        return True
    except:
        return False 
    
########## enter element
def EnterElement(findElement):
    try:
        findElement.send_keys(Keys.RETURN)
        return True
    except:
        return False 
    
########## send text element
def SendTextElement(findElement,text):
    try:
        findElement.send_keys(text)
        return True
    except:
        return False 

########## get text element
def GetTextHTML(findElement):
    try:
        getText = findElement.text
        return getText
    except:
        return None 

########## scroll y
def ScrollY(driver,y):
    try:
        driver.execute_script("window.scrollTo(0, {y})" .format(y=y))
        return True
    except:
        return False 

########## scroll x
def ScrollX(driver,x):
    try:
        driver.execute_script("window.scrollTo({x}, 0)" .format(x=x))
        return True
    except:
        return False 

########## new tab
def NewTab(driver,url):
    try:
        driver = driver.execute_script("window.open('{url}');" .format(url=url))
        return driver
    except:
        return None 

########## close tab
def CloseTab(driver):
    try:
        driver = driver.close()
        return driver
    except:
        return None 

########## reload tab
def ReloadTab(driver):
    try:
        driver = driver.refresh()
        return driver
    except:
        return None 

##########  Mouse Element 
def MouseElement(driver,findElement):
    webdriver.ActionChains(driver).move_to_element(findElement).perform()
    return driver

##########  Mouse offset
def MouseOffset(driver,x,y):
    webdriver.ActionChains(driver).move_by_offset(x,y).perform()
    return driver

##########  Get request
def GetRequest(driver):
    # Lấy DevTools từ trình duyệt
    dev_tools = driver.execute_cdp_cmd("DevTools.enable", {})

    # Lắng nghe sự kiện mạng
    dev_tools.on("Network.requestWillBeSent", handle_request)
    dev_tools.on("Network.responseReceived", handle_response)


def handle_request(request):
    print("Request URL:", request["url"])
    print("Request Method:", request["method"])
    print("Request Headers:", request["headers"])

def handle_response(response):
    print("Response URL:", response["url"])
    print("Response Status:", response["status"])
    print("Response Headers:", response["headers"])
