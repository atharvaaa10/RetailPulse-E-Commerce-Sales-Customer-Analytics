-- ====================================================================
-- RetailPulse - SQL Practice: 06 Common Table Expressions (CTEs)
-- Objectives: Single CTEs, Multiple CTEs, CTEs for modular aggregation and pipeline logic
-- Note: Do NOT provide solutions. Practice writing queries yourself.
-- ====================================================================

-- Question 1:
-- Use a CTE named CustomerSpending to calculate total spend per Customer_ID.
-- In the outer query, calculate the average, minimum, and maximum customer total spend across all customers.
-- TODO: Write your SQL query here:



-- Question 2:
-- Write a CTE named CategoryMetrics that calculates Total_Revenue, Total_Units, and Average_Discount per Category.
-- In the outer query, filter for categories with Total_Revenue exceeding the median or specified threshold.
-- TODO: Write your SQL query here:



-- Question 3:
-- Use multiple CTEs:
-- 1. MonthlySales: Aggregate monthly revenue and order count.
-- 2. SalesGrowth: Calculate Month-over-Month (MoM) revenue difference.
-- Select all columns from the final CTE.
-- TODO: Write your SQL query here:



-- Question 4:
-- Use a CTE to compute the return rate per supplier (Total Returns / Total Orders).
-- In the main query, rank suppliers by return rate descending and identify suppliers with return rates above 15%.
-- TODO: Write your SQL query here:

