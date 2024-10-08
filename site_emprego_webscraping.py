import bs4
import requests

url = requests.get('https://www.infojobs.com.br/empregos.aspx?palabra=Desenvolvedor') #alterar ultima palavra do link para analisar outras vagas
soup = bs4.BeautifulSoup(url.text,"html.parser")
soup_links = soup.find_all('a',class_='text-decoration-none')
print(len(soup_links)) #analisando quantos links existe

#Looping para captura das primeiras vagas disponibilizadas pelo site
for link in soup_links:
    with open('empregos.txt', 'a') as empregos:
        link1 = link.text
        link2 = link.get('href')
        link1 = str(link1)
        link2 = str(link2)

        empregos.write(link1)
        empregos.write("\n")
        empregos.write(link2)