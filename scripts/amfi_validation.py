import pandas as pd

fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

master_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

missing_codes = master_codes - nav_codes

print("Total fund_master codes:", len(master_codes))
print("Total nav_history codes:", len(nav_codes))

if len(missing_codes) == 0:
    print("\n✅ All AMFI codes are present in NAV history.")
else:
    print("\n❌ Missing Codes:")
    print(missing_codes)