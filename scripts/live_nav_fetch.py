import requests
import pandas as pd
from pathlib import Path

output_folder = Path("data/raw")

schemes = {
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for scheme_name, code in schemes.items():

    url = f"https://api.mfapi.in/mf/{code}"

    try:
        response = requests.get(url)
        data = response.json()

        df = pd.DataFrame(data["data"])

        file_name = output_folder / f"{scheme_name}.csv"

        df.to_csv(file_name, index=False)

        print(f"✓ Saved {scheme_name}")

    except Exception as e:
        print(f"✗ Error for {scheme_name}: {e}")

print("\nAll NAV files downloaded.")