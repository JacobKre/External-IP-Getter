import requests
from win10toast import ToastNotifier
from bs4 import BeautifulSoup
from mailjet_rest import Client
from dotenv import load_dotenv
import os

load_dotenv()
mailbullet_api_key = os.getenv("API_KEY")
mailbullet_api_secret = os.getenv("API_SECRET")

toaster = ToastNotifier()
URL = 'https://whatsmyip.com/'
content = requests.get(URL)
soup = BeautifulSoup(content.text, 'html.parser')
ip = soup.find("p", {"id": "shownIpv4"}).text
file = open("SavedIP.txt", "r").read()

if file == ip:
    toaster.show_toast("IP Address Status:", "The external IP address hasn't changed")
else:
    toaster.show_toast("IP Address Status:", f"The external IP is outdated and has been changed to {ip}")
    open("SavedIP.txt", "w").write(f"{ip}")

    api_key = mailjet_api_key
    api_secret = mailjet_api_secret
    mailjet = Client(auth=(api_key, api_secret), version='v3.1')
    data = {
    'Messages': [
        {
        "From": {
            "Email": "ANY EMAIL YOU WANT THE MESSAGE TO COME FROM",
            "Name": "SENDER NAME"
        },
        "To": [
            {
            "Email": "EMAIL THE MESSAGE SHOULD BE SENT TO",
            "Name": "RECIPIENT NAME"
            }
        ],
        "Subject": "A Bunch Of New Random Numbers",
        "TextPart": "Random numbers!",
        "HTMLPart": f"Hello there, I have a bunch of new random numbers which are all totally meaningless for you:<br>{ip}",
        "CustomID": "RandomNUmbers"
        }
    ]
    }
    result = mailjet.send.create(data=data)
    if result.status_code == 200:
        print('Email Sent Successfully!')
    else:
        print('Something went wrong when trying to send the email!')
