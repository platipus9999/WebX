import  requests, time
from pyshade import *


class WebX:
    def main():
        banner = """
██╗    ██╗███████╗██████╗ ██╗  ██╗
██║    ██║██╔════╝██╔══██╗╚██╗██╔╝
██║ █╗ ██║█████╗  ██████╔╝ ╚███╔╝ 
██║███╗██║██╔══╝  ██╔══██╗ ██╔██╗ 
╚███╔███╔╝███████╗██████╔╝██╔╝ ██╗
 ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝
    WebX ~ Spam/Delete Webhook
        Made by Platipus"""

        choice = int(Mode.Vertical(colors.purple_to_blue, banner+"\n[1]Spam Webhook\n[2]Check Webhook\n[3]Delete Webhook\n> ", 4, False, True))
        webhook = Mode.Horizontal(colors.purple_to_blue, "\nInput The Webhook > ", 4, False, True)
        if choice == 1:

            message = Mode.Horizontal(colors.purple_to_blue, "The Message You Want To Send > ", 4, False, True)
            name = Mode.Horizontal(colors.purple_to_blue, "[!]Optional | Name of The Webhook > ", 4, False, True)
            number = int(Mode.Horizontal(colors.purple_to_blue, "Number of Message > ", 4, False, True))
            thread = int(Mode.Horizontal(colors.purple_to_blue, "Number of Threads > ", 4, False, True))
            if name == '':
                return choice, webhook, message, number, thread
            else:
                return choice, webhook, message, number, thread, name

        elif choice == 2 or 3:
            return choice, webhook

    sended = 0
    headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; Touch; rv:11.0) like Gecko',
    'Content-Type': 'application/json'
}   
    def spam_webhook():
        if result[-1] == str:
            while WebX.sended != result[3]:
                res = requests.post(result[1], json={'content': result[2], 'username': result[-1]},headers=WebX.headers)
                if res.status_code == 204:
                    WebX.sended += 1
                    Mode.Horizontal(colors.purple_to_blue,f"[+]The Message Was Sent Successfully: Total[{WebX.sended}]", 5)

            Mode.Horizontal(colors.purple_to_blue,f"\n\n[!]Finish: Total Message Sent [{WebX.sended}]", 4)
            time.sleep(2)
            exit()
        else:
            while WebX.sended != result[3]:
                res = requests.post(result[1], json={'content': result[2]},headers=WebX.headers)
                if res.status_code == 204:
                    WebX.sended += 1
                    Mode.Horizontal(colors.purple_to_blue,f"[+]The Message Was Sent Successfully: Total[{WebX.sended}]", 5)

            Mode.Horizontal(colors.purple_to_blue,f"\n\n[!]Finish: Total Message Sent [{WebX.sended}]", 4)
            time.sleep(2)
            exit()


    def delete_webhook():

        res = requests.delete(result[1])
        Mode.Horizontal(colors.purple_to_blue, "[!]The Webhook Was Deleted Successfully", 4, False, True)

    def check_webhook():
        
        res = requests.get(result[1])
        if res.status_code == 200:
            Mode.Horizontal(colors.purple_to_blue, "[!]Your Webhook Is Alive", 4, False, True)
        else:
            Mode.Horizontal(colors.purple_to_blue, "[!]Your Webhook Is Dead", 4, False, True)

if '__main__' == __name__:
    result = WebX.main()
    
    if result[0] == 1:
        print("\n")
        for _ in range(result[4]):
            WebX.spam_webhook()

    elif result[0] == 2:
        print("\n")
        WebX.check_webhook()
        
    elif result[0] == 3:
        print("\n")
        WebX.delete_webhook()
