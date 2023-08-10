import requests

def OpenProfile():
    headers = {
                'Content-Type': 'text/html',
                'Connection': 'keep-alive',
                'Accept': '*/*',
                'Content-Type': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
            }
    x = requests.get('https://w3schools.com',headers)
    print(x.status_code)
    print(x)
    return x.status_code