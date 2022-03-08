import requests
from bs4 import BeautifulSoup
from requests.api import request

req = input("Введите запрос: ")
references = []

def split(str):
    res = str[7:]
    res = res.split('&', 1)[0]
    return res

for i in range(0,2):

    url = f"https://www.google.com/search?q={req}&start={i*10}"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    h3s = soup.find_all('h3')
    print(f"------PAGE {i+1} ----------")
    for h3 in h3s:
        references.append(h3.parent)
        ref = str(h3.parent.get("href"))
        print(str(h3.find("div").text)+' ' + split(ref) + "\n --------------------------------")
