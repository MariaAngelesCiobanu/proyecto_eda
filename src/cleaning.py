import pandas as pd


def clean(df: pd.DataFrame) -> pd.DataFrame:
    
    # eliminar duplicados
    df = df.drop_duplicates()

    # rellenar nulos
    df["country"] = df["country"].fillna("Unknown")
    df["director"] = df["director"].fillna("Unknown")

    return df