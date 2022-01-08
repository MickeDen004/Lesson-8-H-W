import requests

website_name = input('Enter URL: ')
response = requests.get(website_name)
info = response.content
with open("info.bin", "wb") as f:
    f.write(info)
