import pandas as pd
import json
import seaborn as sns
import matplotlib.pyplot as plt

"""
EUROVAISTINE
"""

file_path = "C:/Users/Vytautas/PycharmProjects/pythonKursas/Valentina/eurovaistineVA.csv"
eurovaistine_df = pd.read_csv(file_path)

eurovaistine_df[['PAVADIN', 'euro_gramai', 'euro_tipas', 'euro_kiekis']] = eurovaistine_df['pavadinimas'].str.split(",", n=3, expand=True)
# print(eurovaistine_df)

# eurovaistine_df['kaina'] = eurovaistine_df['kaina']/ 100

"""
GAVOME PAGRINDINE LENTELE
"""

df_eurovaistine = pd.DataFrame(eurovaistine_df)
df_eurovaistine.to_csv('eurovaistineVA.csv', index=False)
# print(df_eurovaistine)

"""
PRATRYNEM STULPELIUS
"""

eurovaistine1_df = eurovaistine_df.drop(eurovaistine_df.columns[[0,1,3]], axis = 1)
eurovaistine2_df = eurovaistine1_df.rename(columns={'kaina':'euro_kaina'})

#print(eurovaistine2_df)
df_eurovaistine2 = pd.DataFrame(eurovaistine2_df)
df_eurovaistine2.to_csv('2eurovaistineVA.csv', index=False)
# print(df_eurovaistine2)
eurovaistine2_df[['Pav_pirmas_z', 'kita']] = eurovaistine2_df['PAVADIN'].str.split(" ",n=1, expand=True)
eurovaistine3_df = eurovaistine2_df.drop(eurovaistine2_df.columns[[6]], axis = 1)
df_eurovaistine3 = pd.DataFrame(eurovaistine3_df)
df_eurovaistine3.to_csv('2eurovaistineVA.csv', index=False)
# print(eurovaistine3_df)


"""
GAVOME KAINOS VIDURKI PAGAL VAISTINE
"""

df = pd.read_csv('2eurovaistineVA.csv')
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 2000)

# print(df.head())
#
# print(df.shape)
# print(df.columns)
# print(df.dtypes)


euro_average_kaina = df_eurovaistine3['euro_kaina'].mean().round(2)
print(euro_average_kaina)

'''
GAL TRINSIME
'''
# EURO_PRODUKTAI_df = df_eurovaistine3.groupby('Pav_pirmas_z').size()
# print(EURO_PRODUKTAI_df)
# palette_color = sns.color_palette ("deep")
# EURO_PRODUKTAI_df.plot.pie(y = 'PRODUkTAI', colors=palette_color, autopct='%.0f%%',legend=False, figsize = (30,10), textprops={'fontsize': 22})
# plt.ylabel('')
# plt.show()

'''
EUROVAISTINĖS VAISTINĖS ASORTIMENTO ANALIZĖ
'''

sns.barplot(x='euro_kaina',y='Pav_pirmas_z',  data=eurovaistine3_df, hue='Pav_pirmas_z', palette='Set2', dodge=False)
plt.title('EUROVAISTINĖS ASORTIMENTAS')
plt.ylabel('ASORTIMENTAS')
plt.xlabel('KAINA, EUR')
plt.legend([])
# plt.savefig("Pictures\EURO ASORTIMENTAS.png")
plt.tight_layout()
plt.show()

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
gintarine_df['product__price--regular'] = gintarine_df['product__price--regular'].str.replace('N/A', '0')
gintarine1_df = gintarine_df.drop(gintarine_df.columns[[0,1,3]], axis = 1)
gintarine2_df = gintarine1_df.rename(columns={'product__price--regular':'gintarine_kaina'})
gintarine2_df['gintarine_kaina'] = pd.to_numeric(gintarine2_df['gintarine_kaina']).replace('N/A', '')
# print(gintarine2_df)
gintarine2_df[['Pav_pirmas_z', 'kita']] = gintarine2_df['PAVADIN'].str.split(" ",n=1, expand=True)
gintarine3_df = gintarine2_df.drop(gintarine2_df.columns[[6]], axis = 1)
df_gintarine3 = pd.DataFrame(gintarine3_df)
df_gintarine3.to_csv('2gintarineVA.csv', index=False)
# print(gintarine3_df)

"""
GAVOME KAINOS VIDURKI PAGAL VAISTINE
"""
gintarine_average_kaina = df_gintarine3['gintarine_kaina'].mean().round(2)
print(gintarine_average_kaina)

'''
GINTARINĖS VAISTINĖS ASORTIMENTO ANALIZĖ
'''
df = pd.read_csv('2gintarineVA.csv')
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 2000)

# print(df.head())
#
# print(df.shape)
# print(df.columns)
# print(df.dtypes)

sns.barplot(x='gintarine_kaina', y='Pav_pirmas_z',  data=gintarine3_df, hue='Pav_pirmas_z', palette='Set2', dodge=False)
plt.title('GINTARINES ASORTIMENTAS')
plt.ylabel('ASORTIMENTAS')
plt.xlabel('KAINA, EUR')
plt.legend([])
plt.tight_layout()
plt.show()
# plt.savefig("Pictures\GINTARINES ASORTIMENTAS.png")

"""
METU
"""

file_path = "C:/Users/Vytautas/PycharmProjects/pythonKursas/Valentina/metu_VA.csv"
metu_df = pd.read_csv(file_path)

metu_df[['PAVADIN', 'metu_gramai', 'metu_tipas', 'metu_kiekis']] = metu_df['1'].str.split(",", n=3, expand=True)
# print(metu_df)
"""
GAVOME PAGRINDINĘ LENTELĘ
"""
df_metu=pd.DataFrame(metu_df)
df_metu.to_csv('metu_VA.csv', index=False)
# print(df_metu)
"""
PRATRYNĖM LENTELĘ
"""
metu1_df = metu_df.drop(metu_df.columns[[0,1,3]], axis = 1)
metu2_df = metu1_df.rename(columns={'2':'metu_kaina'})
# print(metu1_df)

metu2_df[['Pav_pirmas_z', 'kita']] = metu2_df['PAVADIN'].str.split(" ",n=1, expand=True)
metu3_df = metu2_df.drop(metu2_df.columns[[6]], axis = 1)
df_metu3 = pd.DataFrame(metu3_df)
df_metu3.to_csv('2metuVA.csv', index=False)
# print(metu3_df)

"""
GAVOME KAINOS VIDURKI PAGAL VAISTINE
"""
metu_average_kaina = df_metu3['metu_kaina'].mean().round(2)
print(metu_average_kaina)

'''
100 METŲ VAISTINĖS ASORTIMENTO ANALIZĖ
'''
df = pd.read_csv('2metuVA.csv')
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 2000)

# print(df.head())
#
# print(df.shape)
# print(df.columns)
# print(df.dtypes)

# sns.barplot(x='metu_kaina', y='Pav_pirmas_z',  data=metu3_df, hue='Pav_pirmas_z', palette='Set2', dodge=False)
# plt.title('100 METU ASORTIMENTAS')
# plt.ylabel('ASORTIMENTAS')
# plt.xlabel('KAINA, EUR')
# plt.legend([])
# plt.tight_layout()
# plt.show()
# # plt.savefig("C:\Users\Vytautas\PycharmProjects\pythonKursas\Pictures\GINTARINES ASORTIMENTAS.png")

# """
# SUJUNGIAM LENTELES
# """
#
# sujungta_df = df_eurovaistine2.merge(df_gintarine2, on='PAVADIN').merge(df_metu2, on='PAVADIN')
# # print(sujungta_df)
# df_sujungta = pd.DataFrame(sujungta_df)
# df_sujungta.to_csv('sujungta.csv', index=False)
# print(sujungta_df)

"""
TRIJŲ VAISTINIŲ VIDUTINIŲ KAINŲ PALYGINIMAS/ATVAIZDAVIMAS
"""

plt.figure(figsize = (12,6))
plt.bar(eurovaistine3_df["euro_average_kaina"], gintarine3_df['gintarine_average_kaina'], metu3_df['metu_average_kaina'], color="teal")
plt.title('Vidutinių kainų palyginimas')
plt.xlabel('Vaistinės')
plt.ylabel('Kaina, Eur')
plt.grid(True)
plt.show()