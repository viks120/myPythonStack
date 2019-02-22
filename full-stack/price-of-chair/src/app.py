import requests
from bs4 import  BeautifulSoup

request = requests.get("https://www.johnlewis.com/house-by-john-lewis-buiani-folding-chair-fsc-certified-beech-natural/p2397057")
content = request.content
soup = BeautifulSoup(content,"html.parser")

# Find Name of Chair
element = soup.find("h1", {"class": "product-header__title"})
print(element.text.strip())

price = "$115.00"

price_without_symbol = price[1:]

print(float(price_without_symbol))

