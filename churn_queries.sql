-- ============================================================
-- CUSTOMER CHURN ANALYSIS - SQL QUERIES
-- Author: Venkata Ganesh Kumar Nethuluri
-- Email: ganeshkumarnethuluri@gmail.com
-- ============================================================
-- HOW TO USE:
-- Run these queries in MySQL Workbench, DB Browser for SQLite,
-- or any SQL tool after importing telco_churn.csv as a table.
-- ============================================================

-- ── QUERY 1: Overall Churn Rate ─────────────────────────────
SELECT
    Churn,
    COUNT(*) AS total_customers,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 2) AS percentage
FROM telco_churn
GROUP BY Churn;

-- ── QUERY 2: Churn Rate by Contract Type ────────────────────
SELECT
    Contract,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned,
    ROUND(SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0
          / COUNT(*), 2) AS churn_rate_pct
FROM telco_churn
GROUP BY Contract
ORDER BY churn_rate_pct DESC;

-- ── QUERY 3: Churn Rate by Internet Service ──────────────────
SELECT
    InternetService,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned,
    ROUND(SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0
          / COUNT(*), 2) AS churn_rate_pct
FROM telco_churn
GROUP BY InternetService
ORDER BY churn_rate_pct DESC;

-- ── QUERY 4: Churn by Payment Method ────────────────────────
SELECT
    PaymentMethod,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned,
    ROUND(SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0
          / COUNT(*), 2) AS churn_rate_pct
FROM telco_churn
GROUP BY PaymentMethod
ORDER BY churn_rate_pct DESC;

-- ── QUERY 5: Churn by Tenure Group ──────────────────────────
SELECT
    CASE
        WHEN tenure BETWEEN 0  AND 12 THEN '0-12 months'
        WHEN tenure BETWEEN 13 AND 24 THEN '13-24 months'
        WHEN tenure BETWEEN 25 AND 48 THEN '25-48 months'
        ELSE '49+ months'
    END AS tenure_group,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned,
    ROUND(SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0
          / COUNT(*), 2) AS churn_rate_pct
FROM telco_churn
GROUP BY tenure_group
ORDER BY churn_rate_pct DESC;

-- ── QUERY 6: Average Monthly Charges for Churned vs Not ─────
SELECT
    Churn,
    ROUND(AVG(MonthlyCharges), 2)  AS avg_monthly_charges,
    ROUND(AVG(TotalCharges), 2)    AS avg_total_charges,
    ROUND(AVG(tenure), 1)          AS avg_tenure_months
FROM telco_churn
GROUP BY Churn;

-- ── QUERY 7: Senior Citizen Churn Analysis ───────────────────
SELECT
    CASE WHEN SeniorCitizen = 1 THEN 'Senior Citizen'
         ELSE 'Non-Senior'
    END AS customer_type,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned,
    ROUND(SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0
          / COUNT(*), 2) AS churn_rate_pct
FROM telco_churn
GROUP BY SeniorCitizen;

-- ── QUERY 8: High Risk Customers (for retention targeting) ───
SELECT
    customerID,
    Contract,
    tenure,
    MonthlyCharges,
    InternetService,
    PaymentMethod
FROM telco_churn
WHERE Churn = 'No'
  AND Contract = 'Month-to-month'
  AND tenure < 12
  AND MonthlyCharges > 65
ORDER BY MonthlyCharges DESC
LIMIT 20;

-- ── QUERY 9: Revenue at Risk from Churned Customers ─────────
SELECT
    ROUND(SUM(CAST(TotalCharges AS DECIMAL(10,2))), 2) AS total_revenue_lost,
    COUNT(*) AS total_churned_customers,
    ROUND(AVG(CAST(MonthlyCharges AS DECIMAL(10,2))), 2) AS avg_monthly_lost
FROM telco_churn
WHERE Churn = 'Yes';

-- ── QUERY 10: Full Churn Profile Summary ─────────────────────
SELECT
    'Total Customers'       AS metric, COUNT(*)              AS value FROM telco_churn
UNION ALL
SELECT
    'Total Churned'         AS metric,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)          AS value
FROM telco_churn
UNION ALL
SELECT
    'Churn Rate %'          AS metric,
    ROUND(SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 1)
FROM telco_churn;
