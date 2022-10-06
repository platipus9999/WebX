import os
try:
    from fake_useragent import UserAgent
    import requests
except (ModuleNotFoundError):
    os.system('pip install requests fake_useragent ')

user_agent = UserAgent().random

headers = {
    'user-agent': user_agent,
    'Content-Type': 'application/json'
}

proxies = {
  'http':  '1.1.1.1:8080',
  'https': '1.1.1.1:8080'
}  

sended = 0

choice = int(input("""
██     ██ ███████ ██████  ██   ██ 
██     ██ ██      ██   ██  ██ ██  
██  █  ██ █████   ██████    ███   
██ ███ ██ ██      ██   ██  ██ ██  
 ███ ███  ███████ ██████  ██   ██ 
 
[1]Spam Webhook [2]Delete Webhook

Choice > """))

webhook = input("Webhook URL > ")
thread = int(input("Number Threads > "))
req = requests.get(webhook)

if req.status_code == 200:
    pass
else:
    input("Invalid Url !")

def spam():
        data = requests.post(webhook, json={'content': message},headers=headers)
        if data.status_code == 204:
            print(f"{sended} Message Sended!")

if choice not in [1, 2]:
    input("Are you dumb ? ")

elif choice == 1:
    message = input("Message > ")
    nombre = int(input("Number of Message [0 = inf] > "))
    while sended != nombre:
        spam()
        sended += 1
         
elif choice == 2:
        req = requests.delete(webhook, headers=headers)
        if req.status_code == 204:
            input("Webhook has been successfully deleted ! ")
        else:
            input("Requests Error ! ")       
