import requests
from bs4 import BeautifulSoup
response = requests.get(f'https://www.cocooncenter.com/')
soup = BeautifulSoup(response.content.decode('utf-8'),'lxml')
print(soup.prettify()) 

file_obj = open('chengdu_douban.html', 'w', encoding="utf-8")    # Open in write mode with douban.Html file,Specify the encoding as utf-8
file_obj.write(response.content.decode('utf-8'))    #Save the html content of the response
file_obj.close()
baseurl = "https://www.cocooncenter.com/" 

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
    }
productlinks= []
for x in range  (1,6):
    r = requests.get(f'https://www.cocooncenter.com/cp/sante.html?page={x}').text
    soup = BeautifulSoup(r.content,'lxml')
    productlist = soup.find_all('div',class_='item')

    for item in productlist:
        for link in item.find_all('a',href=True): 
            productlinks.append(baseurl + link['href'])
testlink = 'https://www.cocooncenter.com/orgakiddy-masque-chirurgical-facial-medical-haute-filtration-efb-98-50-masques/54447.html'
r= requests.get(testlink , headers=headers)

soup= BeautifulSoup(r.content ,'lxml')
name= soup.find('h1',class_='titre_produit').text.strip()
price =soup.find('span',class_='price').text.strip()
reviews = soup.find('p',class_='')
print(name, price)