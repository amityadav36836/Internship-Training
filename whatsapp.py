import pywhatkit
import time


contacts = {
    "+91XXXXXXXXXXXX": "Hello,what are you doing",
}

for number, msg in contacts.items():
    print(f"Sending message to {number}...")
    pywhatkit.sendwhatmsg_instantly(number, msg)
    time.sleep(5) 