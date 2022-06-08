import requests
from  bs4 import BeautifulSoup

url = "https://www.autocentrum.pl/paliwa/ceny-paliw/"
page = requests.get(url)
parsed_html = BeautifulSoup(page.content, "html.parser")

container = parsed_html.find('a', class_="station-detail-wrapper on text-center active")
price = container.find('div', class_="price")
price = price.text.strip().replace(" ", "").replace("\n", "")
print(price[:-2].replace(',', '.'))
