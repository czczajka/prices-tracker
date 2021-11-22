import requests
from  bs4 import BeautifulSoup

url = "https://www.nbp.pl/Kursy/KursyA.html"
page = requests.get(url)
parsed_html = BeautifulSoup(page.content, "html.parser")
table = parsed_html.body.find('table', class_="nbptable")
for row in table.findAll("tr"):
    if row.find("td") != None and row.find("td").text == "dolar amerykański":
        price = row.findAll("td")[2].text
        print(price.replace(',','.'))

