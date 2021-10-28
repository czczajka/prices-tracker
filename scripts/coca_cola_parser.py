import requests
from  bs4 import BeautifulSoup

url = "https://www.carrefour.pl/napoje/napoje-gazowane-i-niegazowane/cola"
page = requests.get(url)
parsed_html = BeautifulSoup(page.content, "html.parser")

container = parsed_html.find('div', class_="jss286")
for row in container.findAll("div", attrs={"class" : "jss287"}):
    x = row.find('a')
    if x['title'] == "Coca-Cola Napój gazowany 500 ml":
        y = row.find('div', class_='jss300')
        print(y.text[:-3].replace(',', '.'))
