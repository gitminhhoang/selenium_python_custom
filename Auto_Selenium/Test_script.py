import time
from api_automation import *
from Connect_selenium import *

def TestSCript():
    remote_port = OpenProfile("999e918d-4882-4b33-9a40-f24782bcce95")
    print("Remote port --->  ",remote_port)
    time.sleep(5)
    driver = connect_to_debug_port(remote_port)

    url = "https://whois.inet.vn/ip-location"
    
    driver = GotoUrl(driver,url)
    
    # #get requets
    # GetRequest(driver) 

    inputIp = '//*[@id="ip-location-check"]/div/div/form/div/input'
    if(HasElementXpath(driver,inputIp)):
        findElement = FindElementXpath(driver,inputIp)
        if(SendTextElement(findElement,"38.170.114.231") == False):
            print("--- send text false ---")
            
    else:
        print("Check has xpath -->  false")

    time.sleep(5)
    submitButton = '//*[@id="ip-location-check"]/div/div/form/div/div/button'
    if(HasElementXpath(driver,submitButton)):
        findElement = FindElementXpath(driver,submitButton)
        ClickElement(findElement)
    else:
        print("Check has xpath 1 -->  false ")  

    time.sleep(5)
    xp_Tittle = '//*[@id="ip-location-check"]/div/div/h1'
    val = GetTextHTML(FindElementXpath(driver,xp_Tittle));
    print("===>  ",val)


TestSCript()