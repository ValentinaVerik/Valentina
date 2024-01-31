import pandas as pd
import matplotlib.pyplot as plt


# file_path = "C:/Users/Vytautas/PycharmProjects/pythonKursas/Valentina/eurovaistineVA.csv"
# eurovaistine_df = pd.read_csv(file_path)
#
# eurovaistine_df[['euro_pavadinimas', 'euro_gramai', 'euro_tipas', 'euro_kiekis']] = eurovaistine_df['pavadinimas'].str.split(",", n=3, expand=True)
# # print(eurovaistine_df)
# # eurovaistine_df = eurovaistine.df('kaina').replace
#
# df_eurovaistine = pd.DataFrame(eurovaistine_df)
# df_eurovaistine.to_csv('eurovaistineVA.csv', index=False)
# print(df_eurovaistine)


# file_path = "C:/Users/Vytautas/PycharmProjects/pythonKursas/Valentina/gintarineVA.csv"
# gintarine_df = pd.read_csv(file_path)
#
# gintarine_df[['gintar_pavadinimas', 'gintar_gramai', 'gintar_tipas', 'gintar_kiekis']] = gintarine_df['product__title'].str.split(",", n=3, expand=True)
# # print(gintarine_df)
#
# df_gintarine=pd.DataFrame(gintarine_df)
# df_gintarine.to_csv('gintarineVA.csv', index=False)
# print(df_gintarine)

file_path = "C:/Users/Vytautas/PycharmProjects/pythonKursas/Valentina/metu_VA.csv"
metu_df = pd.read_csv(file_path)

metu_df[['metu_pavadinimas', 'metu_gramai', 'metu_tipas', 'metu_kiekis']] = metu_df['1'].str.split(",", n=3, expand=True)
# print(metu_df)

df_metu=pd.DataFrame(metu_df)
df_metu.to_csv('metu_VA.csv', index=False)
print(df_metu)