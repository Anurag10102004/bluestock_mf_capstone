# Data Dictionary

## fund_master

| Column      | Data Type | Description                    |
| ----------- | --------- | ------------------------------ |
| amfi_code   | Integer   | Unique mutual fund scheme code |
| fund_house  | Text      | Name of fund house             |
| scheme_name | Text      | Mutual fund scheme name        |
| category    | Text      | Equity/Debt category           |

## nav_history

| Column    | Data Type | Description      |
| --------- | --------- | ---------------- |
| amfi_code | Integer   | Mutual fund code |
| date      | Date      | NAV date         |
| nav       | Float     | Net Asset Value  |

## investor_transactions

| Column           | Data Type | Description               |
| ---------------- | --------- | ------------------------- |
| transaction_id   | Integer   | Unique transaction ID     |
| investor_id      | Integer   | Unique investor ID        |
| amfi_code        | Integer   | Mutual fund scheme code   |
| transaction_date | Date      | Date of transaction       |
| transaction_type | Text      | SIP, Lumpsum, Redemption  |
| amount_inr       | Float     | Transaction amount in INR |
| kyc_status       | Text      | KYC verification status   |

## scheme_performance

| Column            | Data Type | Description                       |
| ----------------- | --------- | --------------------------------- |
| amfi_code         | Integer   | Mutual fund scheme code           |
| scheme_name       | Text      | Scheme name                       |
| expense_ratio_pct | Float     | Expense ratio percentage          |
| return_1yr_pct    | Float     | One-year return                   |
| return_3yr_pct    | Float     | Three-year return                 |
| return_5yr_pct    | Float     | Five-year return                  |
| sharpe_ratio      | Float     | Risk-adjusted performance metric  |
| aum_crore         | Float     | Assets Under Management (₹ Crore) |

## Source References

| Dataset                   | Source          |
| ------------------------- | --------------- |
| nav_history.csv           | Project dataset |
| investor_transactions.csv | Project dataset |
| scheme_performance.csv    | Project dataset |
