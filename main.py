import os
#Auto import if you are not on window delete this and do in your terminal this: pip install requests colorama
try:
    import requests
    from colorama import Fore, init
except (ModuleNotFoundError):
    os.system('pip install requests colorama')
#---------------------------------------------------

init(convert=True)
nombre = 0
sended = 0

choice = int(input(f"\n\nWebX:\n\n1. {Fore.GREEN}Spam Webhook {Fore.RESET}[1]\n2. {Fore.RED}Delete Webhook {Fore.RESET}[2]\n\n{Fore.WHITE}Choice : {Fore.RESET}"))

if choice not in [1, 2]:
    input(f'---\n{Fore.BLUE}Webhook{Fore.RESET} -> {Fore.RED}Error{Fore.RESET} ')

if choice == 1:
    boucle = True
    while boucle == True:
        print(f"\n===========\n{Fore.RED}Webhook URL{Fore.RESET}")
        
        webhook = str(input(" > "))
        req = requests.get(webhook)

        if req.status_code == 200:
            print(f"{Fore.BLUE}Message{Fore.RESET}")
            message = str(input(" > "))
            b = int(input("Number of Message [0 = inf] \n> "))

            while nombre < b:
                _data = requests.post(webhook, json={'content': message}, headers={'Content-Type': 'application/json'})
                if _data.status_code == 204:
                    print(f"{Fore.GREEN} Message Sended!")
                    nombre += 1
        else:
            a = input("Invalid Webhook \nRetry ? [y/n] \n> ")
            if a == "y" or a == "Y":
                boucle = True 
            else:
                exit()        
           

if choice == 2:
    boucle = True

    while boucle == True:
        webhook = str(input(f"===========\n{Fore.RED}Webhook URL{Fore.RESET}\n> "))
        r = requests.get(webhook)
        
        if req.status_code == 200:
            requests.delete(webhook)
        else:
            a = input("Invalid Webhook \nRetry ? [y/n] \n> ")
            if a.lower == "y":
                boucle = True 
            else:
                exit() 
