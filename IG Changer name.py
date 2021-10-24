import requests
import json
from uuid import uuid4


request = requests.session()
uid = uuid4()
username = ''
password = ''
name = ''
csrf_info = ['csrftoken'] #define session id to log in your account without secure access

print("""       

Log In With Your Account Please: 

        """)
username = input("Username: ")
password = input("Password: ")
name = input("Name: ")     #Write Your name you want to change it
print("Please wait.....")

logurl = 'https://i.instagram.com/api/v1/accounts/login/'


header_info = {
    'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US",
    "X-IG-Capabilities": "3brTvw==",
    "X-IG-Connection-Type": "WIFI",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    'Host': 'i.instagram.com',
    'Connection': 'keep-alive'
}
nameurl = 'https://i.instagram.com/api/v1/accounts/set_phone_and_name/'
namedata = {
 
    "first_name": name
}
def cookie_function():
    global cookie_log 
          
    request_url = request.post(nameurl, headers=header_info, data=namedata, cookies=cookie_log).status_code
   
    
    if request_url == 200:
      print(f"Your Name is Changing To",name)
      input()
      print("Please Press Enter To Exit")
    else:
        print(f"Error Could not login into your account")
        input()
        exit()

logdata = {

    'uuid': uid,
    'password': password,
    'username': username,
    'device_id': uid,
    'from_reg': 'false',
    '_csrftoken': csrf_info,
    'login_attempt_countn': '0'
}
 
def login():
    global log, loginJS
    global cookie_log 
    log = request.post(logurl, headers=header_info, data=logdata)
    loginJS = log.json()
    if 'logged_in_user' in log.text:
        cookie_log = log.cookies
        cookie_info = cookie_log.get_dict()
        csrf_info = cookie_info['csrftoken']

        cookie_function()
        pass
    else:
        print("Error")
        exit()
login()
