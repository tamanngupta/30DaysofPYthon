import webbrowser
import requests


url = 'https://mail.google.com/mail/u/0/#inbox'
responses = requests.get(url)
print(responses)
