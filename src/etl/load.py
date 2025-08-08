import pandas as pd
from sqlalchemy import create_engine


def load_to_sql(df: pd.DataFrame, table_name: str,
                db_path: str = "data/processed/warehouse.db"):
    """
    Carga un DataFrame a una tabla SQLite.
    """
    engine = create_engine(f"sqlite:///{db_path}", echo=False)
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    print(f"[Load] Datos cargados en la tabla '{table_name}' de {db_path}")
