import requests
from  bs4 import BeautifulSoup

url = "https://aktualnecenniki.pl/cennik-mcdonald-tabela/"
page = requests.get(url)
parsed_html = BeautifulSoup(page.content, "html.parser")
table = parsed_html.body.find('table')
for row in table.findAll("tr"):
    if row.find("td").text == "Big Mac":
        price = row.findAll("td")[1].text[:-2]
        print(price.replace(',','.'))
