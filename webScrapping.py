from bs4 import BeautifulSoup
import requests

url = "https://github.com/Aethelwulf911?tab=repositories"
page = requests.get(url)

soup = BeautifulSoup(page.content,"html.parser")
#All page
print(soup)
#specific part
for i in soup.find_all('div',class_="h-card mt-md-n5"):
    print(i)
#only informations 
for i in soup.find_all('div',class_="h-card mt-md-n5"):
    print(i.text)
print("Done!")