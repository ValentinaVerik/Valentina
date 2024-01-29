import requests
from bs4 import BeautifulSoup
import pandas as pd

alldata=[]
for i in range(1,3):
    url = f"https://www.eurovaistine.lt/paieska/rezultatai?q=paracetamolis&page={i}"
response=requests.get(url)
print(response.status_code)
#     soup=BeautifulSoup(response.content,'html.parser')
