# Data Dictionary

## fund_master

| Column | Data Type | Description |
|----------|----------|----------|
| amfi_code | Integer | Unique mutual fund scheme code |
| fund_house | Text | Name of fund house |
| scheme_name | Text | Mutual fund scheme name |
| category | Text | Equity/Debt category |

## nav_history

| Column | Data Type | Description |
|----------|----------|----------|
| amfi_code | Integer | Mutual fund code |
| date | Date | NAV date |
| nav | Float | Net Asset Value |