import pandas as pd

def load_dataset(path: str):

    df = pd.read_csv(path, encoding="latin1")

    return {
        "dataframe": df,
        "columns": df.columns.tolist(),
        "shape": df.shape,
        "dtypes": df.dtypes.astype(str).to_dict(),
        "nulls": df.isnull().sum().to_dict()
    }