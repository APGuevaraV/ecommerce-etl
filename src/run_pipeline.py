from etl.ingest import ingest_csv
from etl.transform import clean_orders
from etl.load import load_to_sql


RAW_FILE = "data/raw/sales.csv"
STAGING_FILE = "data/staging/sales.parquet"
TABLE_NAME = "orders"


def main():
    print(" Iniciando pipeline ETL...")

    df_raw = ingest_csv(RAW_FILE, STAGING_FILE)

    df_clean = clean_orders(df_raw)

    load_to_sql(df_clean, TABLE_NAME)

    print("✅ Pipeline completado.")


if __name__ == "__main__":
    main()
