import requests
from bs4 import BeautifulSoup

x = requests.get('https://toscrape.com/')
if x.status_code == 200:
    objSoup = BeautifulSoup(x.content, 'html.parser')
    tables = objSoup.findAll('table')
    if len(tables) > 1:
        tbl = tables[1]
        tbltr = tbl.findAll('tr')
        i = 0
        for element in tbltr:
            if i != 0:
                tds = element.findAll('td')
                if tds:
                    print(tds[0].text)
            i += 1
    else:
        print("Tabela não encontrada")
else:
    print("Erro na requisição:", x.status_code)