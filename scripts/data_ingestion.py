import pandas as pd
from pathlib import Path

DATA_PATH = Path("data/raw")

for file in DATA_PATH.glob("*.csv"):
    print("\n" + "=" * 60)
    print(f"FILE: {file.name}")

    df = pd.read_csv(file)

    print("\nShape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())