import pandas as pd
import json
import matplotlib.pyplot as plt

"""
EUROVAISTINE
"""

# file_path = "C:/Users/Vytautas/PycharmProjects/pythonKursas/Valentina/eurovaistineVA.csv"
# eurovaistine_df = pd.read_csv(file_path)
#
# eurovaistine_df[['PAVADIN', 'euro_gramai', 'euro_tipas', 'euro_kiekis']] = eurovaistine_df['pavadinimas'].str.split(",", n=3, expand=True)
# print(eurovaistine_df)

# eurovaistine_df['kaina'] = eurovaistine_df['kaina']/ 100

"""
GAVOME PAGRINDINE LENTELE
"""

# df_eurovaistine = pd.DataFrame(eurovaistine_df)
# df_eurovaistine.to_csv('eurovaistineVA.csv', index=False)
# # print(df_eurovaistine)
#
# """
# PRATRYNEM STULPELIUS
# """
#
# eurovaistine1_df = eurovaistine_df.drop(eurovaistine_df.columns[[0,1,3]], axis = 1)
# eurovaistine2_df = eurovaistine1_df.rename(columns={'kaina':'euro_kaina'})
# # print(eurovaistine1_df)
# df_eurovaistine2 = pd.DataFrame(eurovaistine2_df)
# df_eurovaistine2.to_csv('2eurovaistineVA.csv', index=False)
# print(df_eurovaistine2)
#
# """
# GAVOME KAINOS VIDURKI PAGAL VAISTINE
# """
#
# filtered_euro_df = df_eurovaistine2['euro_pavadinimas'].value_counts()
# # print(filtered_euro_df)
#
# average_kaina_euro = SUM(filtered_euro_df).groupby('euro_pavadinimas')['euro_kaina'].mean().round(2)
# print(average_kaina_euro)

"""
GINTARINE
"""
file_path = "C:/Users/Vytautas/PycharmProjects/pythonKursas/Valentina/gintarineVA.csv"
gintarine_df = pd.read_csv(file_path)

gintarine_df[['PAVADIN', 'gintar_gramai', 'gintar_tipas', 'gintar_kiekis']] = gintarine_df['product__title'].str.split(",", n=3, expand=True)
# print(gintarine_df)

"""
GAVOME PAGRINDINE LENTELE
"""

df_gintarine=pd.DataFrame(gintarine_df)
df_gintarine.to_csv('gintarineVA.csv', index=False)
# print(df_gintarine)

"""
PRATRYNEM STULPELIUS
"""

gintarine1_df = gintarine_df.drop(gintarine_df.columns[[0,1,3]], axis = 1)
gintarine2_df = gintarine1_df.rename(columns={'product__price--regular':'gintarine_kaina'})
# # print(gintarine1_df)
df_gintarine2 = pd.DataFrame(gintarine2_df)
df_gintarine2.to_csv('2gintarineVA.csv', index=False)
print(df_gintarine2)

"""
GAVOME KAINOS VIDURKI PAGAL VAISTINE
"""

#
#
#


"""
METU
"""

# file_path = "C:/Users/Vytautas/PycharmProjects/pythonKursas/Valentina/metu_VA.csv"
# metu_df = pd.read_csv(file_path)
#
# metu_df[['metu_pavadinimas', 'metu_gramai', 'metu_tipas', 'metu_kiekis']] = metu_df['1'].str.split(",", n=3, expand=True)
# print(metu_df)
"""
GAVOME PAGRINDINĘ LENTELĘ
"""
# df_metu=pd.DataFrame(metu_df)
# df_metu.to_csv('metu_VA.csv', index=False)
# print(df_metu)
"""
PRATRYNĖM LENTELĘ
"""
# metu1_df = metu_df.drop(metu_df.columns[[0,1]], axis = 1)
# metu2_df = metu1_df.rename(columns={'2':'metu_kaina'})
# # print(metu1_df)
# df_metu2 = pd.DataFrame(metu2_df)
# df_metu2.to_csv('2metuVA.csv', index=False)

"""
GAVOME KAINOS VIDURKI PAGAL VAISTINE
"""
