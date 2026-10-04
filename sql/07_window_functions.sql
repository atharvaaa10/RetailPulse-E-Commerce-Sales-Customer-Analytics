-- ====================================================================
-- RetailPulse - SQL Practice: 07 Window Functions
-- Objectives: ROW_NUMBER(), RANK(), DENSE_RANK(), LAG(), LEAD(), Cumulative SUM, NTILE()
-- Note: Do NOT provide solutions. Practice writing queries yourself.
-- ====================================================================

-- Question 1:
-- Rank products within each Category by Listed_Price descending using DENSE_RANK().
-- Display Category, Product_Name, Listed_Price, and the price rank.
-- TODO: Write your SQL query here:



-- Question 2:
-- Identify the top 3 highest-spending customers in each State using ROW_NUMBER() or DENSE_RANK().
-- TODO: Write your SQL query here:



-- Question 3:
-- Calculate running cumulative total revenue over time, ordered chronologically by Order_Date.
-- Display Order_Date, Daily_Revenue, and Cumulative_Revenue.
-- TODO: Write your SQL query here:



-- Question 4:
-- Use LAG() to compute the monthly revenue difference and percentage change compared to the previous month.
-- TODO: Write your SQL query here:



-- Question 5:
-- Use NTILE(4) to divide customers into 4 quartiles based on their total monetary spend (Monetary Quartile 1 to 4).
-- TODO: Write your SQL query here:



-- Question 6:
-- For each customer order, use LAG(Order_Date) OVER (PARTITION BY Customer_ID ORDER BY Order_Date)
-- to calculate the days elapsed between consecutive orders for returning customers.
-- TODO: Write your SQL query here:

