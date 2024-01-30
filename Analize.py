import pandas as pd
import matplotlib.pyplot as plt

# file_path = "C:/Users/GS/PycharmProjects/pythonKursas/gintarine2.csv"
#
# gintarine_df = pd.read_csv(file_path)
#
# gintarine_df['product__title'].str.split(',', expand=True)
# gintarine_df =
# print()

file_path = "C:/Users/GS/PycharmProjects/pythonKursas/eurovaistine.csv"
eurovaistine_df = pd.read_csv(file_path)
eurovaistine_df['Price'] = eurovaistine_df['Price'].replace(-2, '[+,]', regex=True).astype(float)

# products_df['Price'] = products_df['Price'].replace('[€,]', '', regex=True).astype(float)
# products_df['Quantity'] = products_df['Quantity'].replace('[+,]', '', regex=True).astype(float)