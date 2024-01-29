import requests
from bs4 import BeautifulSoup
import pandas as pd

# eurovaistine_data=[]
# for i in range(1,3):
#     target = f"https://www.eurovaistine.lt/paieska/rezultatai?q=paracetamolis&page={i}"
# response=requests.get(target)
# # print(response.status_code) # kodas 200
# soup=BeautifulSoup(response.content,'html.parser')
#
# eurovaistine = soup.find_all('div', class_='productCard')
# for product in eurovaistine:
#     brand = product.find('div', class_='brand').text.strip()
#     title = product.find('div', class_='title').text.strip()
#     price = product.find('div', class_='productPrice text-end').text.strip()
# print(eurovaistine_data)

# gintarine_data=[]
# for i in range(1,4):
#     target = f"https://www.gintarine.lt/search?q=paracetamolis&pagenumber={i}"
# response=requests.get(target)
# # print(response.status_code) # kodas 200
# soup=BeautifulSoup(response.content,'html.parser')
#
# gintarine =soup.find_all('div', class_='product product-item product-item-24236')
# for product in gintarine:
#     brand = product.find('div', class_='product__brand'). text.strip()
#     title = product.find('div', class_='product__title').text.strip()
#     price = product.find('span', class_='product__price--regular').text.strip()
#
# print(gintarine_data)

metu_data=[]
for i in range(1,6):
    target = f"https://www.100metu.lt/search/p{i}?q=paracetamol"
    response=requests.get(target)
    # print(response.status_code) # kodas 200
    soup=BeautifulSoup(response.content,'html.parser')

    metu = soup.find_all('span', class_='info-cont')
    print(metu)
    for product in metu:
        brand = product.find('span', class_='cat').text.strip()
        title = product.find('span', class_='title').text.strip()
        price = product.find('span', class_='price').text.strip()

        metu_data.append([brand, title, price])


print(metu_data)