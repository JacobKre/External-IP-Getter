import requests
from win10toast import ToastNotifier
from bs4 import BeautifulSoup

toaster = ToastNotifier()
URL = 'https://whatsmyip.com/'
content = requests.get(URL)
soup = BeautifulSoup(content.text, 'html.parser')
ip = soup.find("p", {"id": "shownIpv4"}).text
file = open("C:/Users/techs/Desktop/IP Getter/SavedIP.txt", "r").read()

if file == ip:
    toaster.show_toast("IP Address Status:", "The external IP address hasn't changed")
else:
    toaster.show_toast("IP Address Status:", f"The external IP is outdated and has been changed to {ip}")
    open("C:/Users/techs/Desktop/IP Getter/SavedIP.txt", "w").write(f"{ip}")