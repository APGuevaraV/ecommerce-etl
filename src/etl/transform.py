import pandas as pd


def clean_orders(df: pd.DataFrame) -> pd.DataFrame:
    """
    Limpia y transforma el DataFrame de órdenes.
    """
    df = df.drop_duplicates()

    # Eliminar filas con valores nulos
    df = df.dropna(subset=['Quantity', 'UnitPrice'])

    # Calcular Revenue
    if 'Quantity' in df.columns and 'UnitPrice' in df.columns:
        df['Revenue'] = df['Quantity'] * df['UnitPrice']

    df = df[df['Revenue'] > 0]

    print(f"[Transform] DataFrame limpio con {len(df)} filas")
    return df
