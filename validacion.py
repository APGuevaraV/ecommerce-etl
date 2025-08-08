import pandas as pd

df = pd.read_parquet("data/staging/sales.parquet")


print(df.shape)       # filas y columnas
print(df.head())      # primeras 5 filas
print(df.columns)     # nombres de columnas

print(df.isna().sum())       # columnas con valores faltantes
print(df.dtypes)             # tipos de datos
print(df.describe())         # estadísticas rápidas
