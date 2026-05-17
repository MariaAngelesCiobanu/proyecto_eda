import pandas as pd


def build_features(df: pd.DataFrame) -> pd.DataFrame:

    # antigüedad del contenido
    df["content_age"] = 2026 - df["release_year"]

    # década
    df["decade"] = (df["release_year"] // 10) * 10

    # duración numérica
    df["duration_num"] = df["duration"].str.extract(r'(\d+)').astype(float)

    return df