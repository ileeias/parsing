import requests
from bs4 import BeautifulSoup

response = requests.get('https://small.kz/ru/almaty/catalog-goods')
# with open('small.html', 'wb') as file:
#     file.write(response.content)

soup = BeautifulSoup(response.text, 'html.parser')
# goods = soup.find('div', class_='goods')

# print(goods.find('div', class_='goodInfo').find('p').text)
# good_info_list = goods.find_all('div', class_='goodInfo').find('p').text
# for i in range(0, len(good_info_list), 1):
#     print()

# elem = soup.find('a', class_='link-nav')
# print(elem)
# print(elem.text)
# print(elem['href'])
# catalog = soup.find('a', class_='catalogRead')
# images = catalog.find_all('img')
# # find_all(<TAG>, class_=<CLASS>) - Находить все тэги <TAG> с классом <CLASS>, ответ list
# image = images[1]  # Берем вторую картинку, так как в листе их две, у второй индекс 1
# image_src = image['src']  # Берем src у картинки, это и есть ссылка на картинку
# print(image_src)
#
# response = requests.get(image_src)  # Кидаем запрос на юрл с картинкой
# with open('banner.png', 'wb') as file:  # Открываем файл в бинарном режиме
#     file.write(response.content)  # Записываем в него картинку
#
# banner = soup.find('div', class_='catalogInfoBanner')
# print(banner)
gros =[]
goods = soup.find('div', class_='goods')
good_info_list = goods.find_all('div', class_='goodInfo')
good_preview = goods.find_all('div', class_='goodPreview')
for i in range(len(good_info_list)):
    print("Продукт", (' '.join((good_info_list[i].find_next('p').text).split())), end=' ')
    print('---', *(good_preview[i].find_next(class_='activePrice').text).split(), 'Тенге')