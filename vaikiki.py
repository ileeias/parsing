# import requests
# from bs4 import BeautifulSoup
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) '
#                   'Chrome/50.0.2661.102 Safari/537.36'
# }
# response = requests.get('https://www.lcwaikiki.kz/ru-RU/KZ/product-group/men', headers=headers)
#
# soup = BeautifulSoup(response.text, 'html.parser')
# catalog = soup.find_all('h5', class_="product-card__title")[:10]
# images = soup.find_all('img', class_='product-image__image')[:5]
# num = 0
# for i in images:
#     response = requests.get(i['src'])
#     img = open(f'image_{num}.png', 'wb')
#     img.write(response.content)
#     img.close()
#     num +=1
"""response = requests.get('https://www.lcwaikiki.kz/ru-RU/KZ/product/LC-WAIKIKI/%D0%94%D0%BB%D1%8F-%D0%BC%D1%83%D0%B6%D1%87%D0%B8%D0%BD/%D0%94%D0%B6%D0%B8%D0%BD%D1%81%D0%BE%D0%B2%D1%8B%D0%B5-%D1%88%D0%BE%D1%80%D1%82%D1%8B/7066371/4227857', headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')
card_title = soup.find('h1', class_="product-title seo")
card_price = soup.find('div', class_="basket-discount")
card_size = soup.find_all('div', class_='option-size')
print((card_title.text).strip())
print(card_price.text)
for i in range(3):
    print(card_size.find('a'))"""


import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/50.0.2661.102 Safari/537.36'
}
response = requests.get('https://www.lcwaikiki.kz/ru-RU/KZ/product/LC-WAIKIKI/%D0%94%D0%BB%D1%8F-%D0%BC'
                        '%D1%83%D0%B6%D1%87%D0%B8%D0%BD/%D0%94%D0%B6%D0%B8%D0%BD%D1%81%D0%BE%D0%B2%D0%B0%D1'
                        '%8F-%D1%80%D1%83%D0%B1%D0%B0%D1%88%D0%BA%D0%B0/7068563/4295673', headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')
material = soup.find('div', class_='panel-body')
print(material.find_all('p')[2].text)