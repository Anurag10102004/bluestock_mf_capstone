import pandas as pd
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

csv_path = os.path.join(
    base_dir,
    "data",
    "processed",
    "scheme_performance_clean.csv"
)

performance = pd.read_csv(csv_path)

risk = "High"   # Change to Low / Moderate / High

recommendations = (
    performance[
        performance['risk_grade'].str.lower() == risk.lower()
    ]
    .sort_values(
        'sharpe_ratio',
        ascending=False
    )
    [['scheme_name',
      'fund_house',
      'sharpe_ratio',
      'risk_grade']]
    .head(3)
)

print("\nTop 3 Recommended Funds:\n")
print(recommendations)