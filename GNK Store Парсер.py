import requests
from bs4 import BeautifulSoup
from time import sleep

headers = {"User-Agent":
           "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"}
text4 = ""

def get_url():
    for count in range(1, 7):
        url = "https://gnk-store.ru"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "lxml")
        data = soup.find("div", class_="col-6 col-lg-7 p-0 mb-3 mb-lg-0 pl-2")

        divPerchi = "https://gnk-store.ru" + data.find("a").get("href")

        url = f"https://gnk-store.ru/ekipirovka-vratarya/?page={count}"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "lxml")
        data = soup.find_all("div", class_="product-layout product-grid col-6 col-xs-6 col-sm-6 col-md-4 col-lg-4")
            
        for i in data:
            card_url = "https://gnk-store.ru" + i.find("a").get("href")
            yield card_url
        
for card in get_url():
    response = requests.get(card, headers=headers)
    sleep(2)
    soup = BeautifulSoup(response.text, "lxml")
    data = soup.find("div", class_="row")
    name = data.find("h1", class_="mb-2 mb-lg-3").text
    price = data.find("h2", class_="price").text
    text = data.find("h3", class_="mb-3").text
    data2 = data.find("div", class_="tab-pane active")

    text2 = data2.find_all("p")
    for j in text2:
        text3 = j.text
        text4 += text3 + "\n"
    try:
        text5 = data2.find("h4").text
        print(name)
        print(price)
        print(text)
        print(text5)
        print(text4)
        print()
        text4 = ""
    except:
        print(name)
        print(price)
        print(text)
        print(text4)
        print()
        text4 = ""
    
        
