import requests
import json

def OpenProfile(uuid):
    try:
        headers = {
                'Content-Type': 'text/html',
                'Connection': 'keep-alive',
                'Accept': '*/*',
                'Content-Type': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
            }
        x = requests.get('http://127.0.0.1:5555/openProfile?uuid='+uuid,headers=headers)
        
        result =  x.json()
        print(result['data']['remote_port'])
        
        return result['data']['remote_port']
    except Exception as e:
        print("error get data ==>  " ,e)
        return None

def CloseProfile(uuid):
    try:
        headers = {
                'Content-Type': 'text/html',
                'Connection': 'keep-alive',
                'Accept': '*/*',
                'Content-Type': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
            }
        x = requests.get('http://127.0.0.1:5555/closeProfile?uuid='+uuid,headers=headers)
        
        result =  x.json()
        return result['result']
    except Exception as e:
        print("error get data ==>  " ,e)
        return None

def CheckingProfile(uuid):
    try:
        headers = {
                'Content-Type': 'text/html',
                'Connection': 'keep-alive',
                'Accept': '*/*',
                'Content-Type': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
            }
        x = requests.get('http://127.0.0.1:5555/authorize?uuid='+uuid,headers=headers)
        
        result =  x.json()
        return result['status']
    except Exception as e:
        print("error get data ==>  " ,e)
        return None

def ListProfile(page,limit):
    try:
        headers = {
                'Content-Type': 'text/html',
                'Connection': 'keep-alive',
                'Accept': '*/*',
                'Content-Type': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
            }
        x = requests.get('http://127.0.0.1:5555/profileList?page='+str(page)+"&limit="+str(limit),headers=headers)
        
        result =  x.json()
        return result
    except Exception as e:
        print("error get data ==>  " ,e)
        return None

def ListConfigDefault(page,limit):
    try:
        headers = {
                'Content-Type': 'text/html',
                'Connection': 'keep-alive',
                'Accept': '*/*',
                'Content-Type': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
            }
        x = requests.get('http://127.0.0.1:5555/get-list-config-default?page='+str(page)+"&limit="+str(limit),headers=headers)
        
        result =  x.json()
        return result
    except Exception as e:
        print("error get data ==>  " ,e)
        return None

def ListStatus():
    try:
        headers = {
                'Content-Type': 'text/html',
                'Connection': 'keep-alive',
                'Accept': '*/*',
                'Content-Type': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
            }
        x = requests.get('http://127.0.0.1:5555/get-list-status',headers=headers)
        
        result =  x.json()
        return result
    except Exception as e:
        print("error get data ==>  " ,e)
        return None

def ListTag():
    try:
        headers = {
                'Content-Type': 'text/html',
                'Connection': 'keep-alive',
                'Accept': '*/*',
                'Content-Type': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
            }
        x = requests.get('http://127.0.0.1:5555/get-list-tag',headers=headers)
        
        result =  x.json()
        return result
    except Exception as e:
        print("error get data ==>  " ,e)
        return None

def GetProfileByUuid(uuid):
    try:
        headers = {
                'Content-Type': 'text/html',
                'Connection': 'keep-alive',
                'Accept': '*/*',
                'Content-Type': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
            }
        x = requests.get('http://127.0.0.1:5555/browser/get-profile-by-uuid?uuid='+uuid,headers=headers)
        
        result =  x.json()
        return result
    except Exception as e:
        print("error get data ==>  " ,e)
        return None

def CreateProfileByDefault(body):
    try:
        headers = {
                'Content-Type': 'text/html',
                'Connection': 'keep-alive',
                'Accept': '*/*',
                'Content-Type': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
            }
        x = requests.post('http://127.0.0.1:5555/create-profile-by-default',headers=headers,json=body)
        
        result =  x.json()
        return result
    except Exception as e:
        print("error get data ==>  " ,e)
        return None

def CreateProfileByCustomize(body):
    try:
        headers = {
                'Content-Type': 'text/html',
                'Connection': 'keep-alive',
                'Accept': '*/*',
                'Content-Type': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
            }
        x = requests.post('http://127.0.0.1:5555/create-profile-custom',headers=headers,json=body)
        
        result =  x.json()
        return result
    except Exception as e:
        print("error get data ==>  " ,e)
        return None

def UpdateNote(body):
    try:
        headers = {
                'Content-Type': 'text/html',
                'Connection': 'keep-alive',
                'Accept': '*/*',
                'Content-Type': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
            }
        x = requests.put('http://127.0.0.1:5555/update-note',headers=headers,json=body)
        
        result =  x.json()
        return result
    except Exception as e:
        print("error get data ==>  " ,e)
        return None

def UpdateName(body):
    try:
        headers = {
                'Content-Type': 'text/html',
                'Connection': 'keep-alive',
                'Accept': '*/*',
                'Content-Type': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
            }
        x = requests.put('http://127.0.0.1:5555/update-name',headers=headers,json=body)
        
        result =  x.json()
        return result
    except Exception as e:
        print("error get data ==>  " ,e)
        return None

def SyncTag(body):
    try:
        headers = {
                'Content-Type': 'text/html',
                'Connection': 'keep-alive',
                'Accept': '*/*',
                'Content-Type': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
            }
        x = requests.put('http://127.0.0.1:5555/sync-tags',headers=headers,json=body)
        
        result =  x.json()
        return result
    except Exception as e:
        print("error get data ==>  " ,e)
        return None

def ChangeStatus(body):
    try:
        headers = {
                'Content-Type': 'text/html',
                'Connection': 'keep-alive',
                'Accept': '*/*',
                'Content-Type': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
            }
        x = requests.put('http://127.0.0.1:5555/change-status',headers=headers,json=body)
        
        result =  x.json()
        return result
    except Exception as e:
        print("error get data ==>  " ,e)
        return None

def DeleteProfile(body):
    try:
        headers = {
                'Content-Type': 'text/html',
                'Connection': 'keep-alive',
                'Accept': '*/*',
                'Content-Type': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
            }
        x = requests.delete('http://127.0.0.1:5555/delete-profile',headers=headers,json=body)
        
        result =  x.json()
        return result
    except Exception as e:
        print("error get data ==>  " ,e)
        return None

def UpdateProxy(body):
    try:
        headers = {
                'Content-Type': 'text/html',
                'Connection': 'keep-alive',
                'Accept': '*/*',
                'Content-Type': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
            }
        x = requests.put('http://127.0.0.1:5555/update-proxy',headers=headers,json=body)
        
        result =  x.json()
        return result
    except Exception as e:
        print("error get data ==>  " ,e)
        return None

def GET_Custom(url):
    try:
        headers = {
                'Content-Type': 'text/html',
                'Connection': 'keep-alive',
                'Accept': '*/*',
                'Content-Type': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
            }
        x = requests.get(url,headers)
        
        result =  x.json()
        return result
    except Exception as e:
        print("error get data ==>  " ,e)
        return None

def POST_Custom(url,body):
    try:
        headers = {
                'Content-Type': 'text/html',
                'Connection': 'keep-alive',
                'Accept': '*/*',
                'Content-Type': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
            }
        x = requests.post(url,headers,json=body)
        
        result =  x.json()
        return result
    except Exception as e:
        print("error get data ==>  " ,e)
        return None

def PUT_Custom(url,body):
    try:
        headers = {
                'Content-Type': 'text/html',
                'Connection': 'keep-alive',
                'Accept': '*/*',
                'Content-Type': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
            }
        x = requests.put(url,headers,json=body)
        
        result =  x.json()
        return result
    except Exception as e:
        print("error get data ==>  " ,e)
        return None

def DELETE_Custom(url,body):
    try:
        headers = {
                'Content-Type': 'text/html',
                'Connection': 'keep-alive',
                'Accept': '*/*',
                'Content-Type': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
            }
        x = requests.delete(url,headers,json=body)
        
        result =  x.json()
        return result
    except Exception as e:
        print("error get data ==>  " ,e)
        return None