# tool to check if username in Instagram can be change or no
import requests
import uuid
import random

print("Check 14 Days usernames in Instagram \n")

random_choose = "abcdefghijklmnopqrwstuvwxyz1234567890"
try:
	file_username = open("users.txt", "r")
except FileNotFoundError:
	print ("please make file users.txt")
	input()

while 1:
	email = random.choice(random_choose)+random.choice(random_choose)+random.choice(random_choose)+random.choice(random_choose)+random.choice(random_choose)+random.choice(random_choose)+"@gmail.com"
	password = random.choice(random_choose)+random.choice(random_choose)+random.choice(random_choose)+random.choice(random_choose)+random.choice(random_choose)+random.choice(random_choose)+random.choice(random_choose)+random.choice(random_choose)
	
	username = file_username.readline().split("\n")[0]
	if username == "":
		exit()
	  
	uid = str(uuid.uuid4())

	
	url = "https://i.instagram.com/api/v1/accounts/create_validated/"
	
	header_login = {
		'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
		"Accept": "*/*",
		"Accept-Encoding": "gzip, deflate",
		"Accept-Language": "en-US",
		"X-IG-Capabilities": "3brTvw==",
		"X-IG-Connection-Type": "WIFI",
		"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
		'Host': 'i.instagram.com'
}
	data_log = {
		"device_id": uid,
		"uuid": uid,
		"email": email,
		"password": password,
		"_csrftoken": "3IsBQzwjBN5xG242t0xPmw9vBq6tMcDo",
		"firt_name": "",
		"username": username
}
	request_get = requests.post(url, data=data_log, headers=header_login)
	
	if "username_held_by_others" in request_get.text:
		print(f"@{username} has 14 Days you can not change it ")
		with open("14 Days.txt", "a") as file:
			file.write(f"{username}\n")
	
	elif "username_is_taken" in request_get.text:
		print(f"@{username} has Not 14 Days you can change it now")
		with open("Not 14 Days.txt", "a") as file:
			file.write(f"{username}\n")
	
	else:
		print(f"Error >>  @{username}")
		print(request_get.text)
