import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

eurovaistine_data = []
for i in range(1, 3):
    target = f"https://www.eurovaistine.lt/paieska/rezultatai?q=paracetamolis&page={i}"
    response = requests.get(target)
    soup = BeautifulSoup(response.content, 'html.parser')
    script_tags = soup.find_all('script', type='application/json')

    for script in script_tags:
        data_component_name = script.get('data-component-name')
        if data_component_name and 'ProductsList' in data_component_name:
            products_json = json.loads(script.string)
            for product in products_json['products']:
                for variant in product['variants']:
                    item = {
                        'pavadinimas': variant['name'],
                        'gamintojas': variant['brand'],
                        'kaina': variant['price']['price'] #.replace(-2, '.').astype(float)
                    }
                    eurovaistine_data.append(item)

json_data = json.dumps(eurovaistine_data, indent=4, ensure_ascii=False)
# print(json_data)


df_eurovaistine = pd.DataFrame(eurovaistine_data)
df_eurovaistine.to_csv('eurovaistine.csv', index=False)
print(df_eurovaistine)



# gintarine_data = []
# for i in range(1, 4):
#     target = f"https://www.gintarine.lt/search?q=paracetamolis&pagenumber={i}"
#     response = requests.get(target)
#     # print(response.status_code) # kodas 200
#     soup = BeautifulSoup(response.content, 'html.parser')
#
#     gintarine = soup.find_all('div', {'data-productid': True})
#
#     for product in gintarine:
#         brand = product.find('div', class_='product__brand').text.strip()
#         title = product.find('div', class_='product__title').text.strip()
#         price = product.find('span', class_='product__price--regular')
#         if price:
#             price_text = price.text.strip().replace('€', '')
#         else:
#             price_text = " N/A "
#         gintarine_data.append({
#             'product__brand': brand,
#             'product__title': title,
#             'product__price--regular': price_text
#         })
# #print(gintarine_data)
#
# df_gintarine=pd.DataFrame(gintarine_data)
# df_gintarine.to_csv('gintarine2.csv', index=False)
# print(df_gintarine)


# metu_data=[]
# for i in range(1,6):
#     target = f"https://www.100metu.lt/search/p{i}?q=paracetamol"
#     response=requests.get(target)
#     # print(response.status_code) # kodas 200
#     soup=BeautifulSoup(response.content,'html.parser')
#
#     metu = soup.find_all('span', class_='info-cont')
#     print(metu)
#     for product in metu:
#         brand = product.find('span', class_='cat').text.strip()
#         title = product.find('span', class_='title').text.strip()
#         price = product.find('span', class_='price').text.strip().replace(' €', '')
#
#         metu_data.append([brand, title, price])
#
# # print(metu_data)
#
# df_metu=pd.DataFrame(metu_data)
# df_metu.to_csv('metu1.csv', index=False)
# print(df_metu)