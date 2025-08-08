import pandas as pd
from pathlib import Path


def ingest_csv(input_path: str, output_path: str) -> pd.DataFrame:
    """
    Lee un CSV desde input_path, lo guarda como Parquet en output_path 
    y devuelve un DataFrame.
    """
    df = pd.read_csv(input_path, parse_dates=True, encoding='latin-1')

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(output_path, index=False)

    print(f"[Ingest] Datos guardados en {output_path}")
    return df
