import matplotlib.pyplot as plt
import sqlite3
import pandas as pd


conn = sqlite3.connect("data/processed/warehouse.db")


df = pd.read_sql("SELECT * FROM orders", conn)

# Ventas por mes
# Convertir a fecha y agrupar por mes
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df['month'] = df['InvoiceDate'].dt.to_period('M')

ventas_por_mes = df.groupby('month')['Revenue'].sum()

# Graficar
ventas_por_mes.plot(kind='bar', figsize=(10, 5))
plt.title("Ventas por mes")
plt.xlabel("Mes")
plt.ylabel("Monto total")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

ventas_por_paises = df.groupby('Country')[
    'Quantity'].sum().sort_values(ascending=False)
top_n = 7
ventas_paises_reducido = ventas_por_paises[:top_n]
ventas_paises_reducido['Otros'] = ventas_por_paises[top_n:].sum()

ventas_paises_reducido.plot(kind='pie',
                            autopct='%1.1f%%',
                            figsize=(7, 7),
                            wedgeprops={'width': 0.4})
plt.title("Porcentaje de pedidos por país")
plt.ylabel("")
plt.show()
conn.close()
