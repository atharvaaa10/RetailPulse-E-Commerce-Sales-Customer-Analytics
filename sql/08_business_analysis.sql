-- ====================================================================
-- RetailPulse - SQL Practice: 08 Comprehensive Business Analysis
-- Objectives: Real-world business reporting, RFM scoring, cohort retention, supply chain SLA analysis
-- Note: Do NOT provide solutions. Practice writing queries yourself.
-- ====================================================================

-- Analysis 1: Executive KPI Summary
-- Calculate overall metrics: Total Revenue, Total Net Revenue (after discounts), Total Orders,
-- Average Order Value (AOV), Total Customers, and Overall Return Rate %.
-- TODO: Write your SQL query here:



-- Analysis 2: Full RFM Segmentation
-- Compute Recency (days since last purchase), Frequency (total orders), and Monetary value (total spend)
-- for each customer. Score each dimension from 1 to 5 using NTILE(5) and concatenate into an RFM_Score.
-- TODO: Write your SQL query here:



-- Analysis 3: Monthly Customer Cohort Retention Matrix
-- Identify each customer's cohort month (month of their first purchase).
-- Track how many customers from each cohort make repeat purchases in month 1, month 2, month 3, etc.
-- TODO: Write your SQL query here:



-- Analysis 4: Product Margin & Profitability Analysis
-- Join transactions with products to compute Net Sales, Total COGS (Cost of Goods Sold = Cost_Price * Quantity),
-- Gross Profit (Net Sales - COGS), and Gross Margin % by Category and Subcategory.
-- Identify categories with below-target profit margins.
-- TODO: Write your SQL query here:



-- Analysis 5: Delivery SLA Breach & Return Correlation
-- Analyze whether orders with Delivery_Days > 7 days experience a higher return rate
-- compared to orders delivered within 3 days or 4-7 days.
-- Group by Delivery_Bucket and compute Total Orders, Returned Orders, and Return Rate %.
-- TODO: Write your SQL query here:



-- Analysis 6: Payment Method Profitability & Risk Profile
-- For each payment method, calculate: Total Orders, Total Revenue, Average Discount %,
-- Cancellation Rate %, and Return Rate %.
-- Highlight high-risk payment channels.
-- TODO: Write your SQL query here:

