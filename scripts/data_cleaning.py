import pandas as pd

# Load nav_history
df = pd.read_csv("data/raw/02_nav_history.csv")

print("Original Shape:", df.shape)

# Date convert
df["date"] = pd.to_datetime(df["date"])

# Sort
df = df.sort_values(["amfi_code", "date"])

# Remove duplicates
df = df.drop_duplicates()

# NAV > 0
df = df[df["nav"] > 0]

print("Cleaned Shape:", df.shape)

# Save
df.to_csv(
    "data/processed/nav_history_clean.csv",
    index=False
)

print("Saved Successfully")
# =====================================
# INVESTOR TRANSACTIONS CLEANING
# =====================================

import pandas as pd

trans_df = pd.read_csv("data/raw/08_investor_transactions.csv")

# Date format fix
trans_df["transaction_date"] = pd.to_datetime(
    trans_df["transaction_date"]
)

# Remove duplicates
trans_df = trans_df.drop_duplicates()

# Amount validation
trans_df = trans_df[trans_df["amount_inr"] > 0]

# Transaction type standardization
trans_df["transaction_type"] = (
    trans_df["transaction_type"]
    .str.strip()
    .str.title()
)

# KYC status validation
print("\nKYC Status Values:")
print(trans_df["kyc_status"].unique())

# Save cleaned file
trans_df.to_csv(
    "data/processed/investor_transactions_clean.csv",
    index=False
)

print("Investor transactions cleaned successfully")
# =====================================
# SCHEME PERFORMANCE CLEANING
# =====================================

perf_df = pd.read_csv("data/raw/07_scheme_performance.csv")

print("\nOriginal Performance Shape:", perf_df.shape)

# Remove duplicates
perf_df = perf_df.drop_duplicates()

# Validate return columns
return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in return_cols:
    perf_df[col] = pd.to_numeric(
        perf_df[col],
        errors="coerce"
    )

# Expense ratio validation
anomalies = perf_df[
    (perf_df["expense_ratio_pct"] < 0.1) |
    (perf_df["expense_ratio_pct"] > 2.5)
]

print("\nExpense Ratio Anomalies:")
print(anomalies.shape[0])

# Save cleaned file
perf_df.to_csv(
    "data/processed/scheme_performance_clean.csv",
    index=False
)

print("Scheme performance cleaned successfully")