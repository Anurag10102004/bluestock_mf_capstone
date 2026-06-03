-- 1. Top 5 Funds by AUM

SELECT scheme_name, aum_crore
FROM scheme_performance
ORDER BY aum_crore DESC
LIMIT 5;


-- 2. Funds with Expense Ratio less than 1%

SELECT scheme_name, expense_ratio_pct
FROM scheme_performance
WHERE expense_ratio_pct < 1;


-- 3. Average 1 Year Return

SELECT AVG(return_1yr_pct) AS avg_return
FROM scheme_performance;


-- 4. Count Funds by Category

SELECT category, COUNT(*) AS total_funds
FROM scheme_performance
GROUP BY category;


-- 5. Highest Sharpe Ratio Funds

SELECT scheme_name, sharpe_ratio
FROM scheme_performance
ORDER BY sharpe_ratio DESC
LIMIT 5;


-- 6. Transactions by State

SELECT state, COUNT(*) AS total_transactions
FROM investor_transactions
GROUP BY state
ORDER BY total_transactions DESC;


-- 7. Total Investment Amount

SELECT SUM(amount_inr) AS total_amount
FROM investor_transactions;


-- 8. Transactions by Gender

SELECT gender, COUNT(*) AS total
FROM investor_transactions
GROUP BY gender;


-- 9. Average NAV

SELECT AVG(nav) AS average_nav
FROM nav_history;


-- 10. Top 5 Funds by 5-Year Return

SELECT scheme_name, return_5yr_pct
FROM scheme_performance
ORDER BY return_5yr_pct DESC
LIMIT 5;