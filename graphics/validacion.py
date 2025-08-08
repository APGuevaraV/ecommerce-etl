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


conn.close()
