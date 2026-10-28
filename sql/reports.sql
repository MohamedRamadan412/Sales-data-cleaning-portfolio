-- Run these queries against the sales table created by pipeline.py.

-- 1. Total revenue and order count
SELECT
    COUNT(*) AS total_orders,
    ROUND(SUM(revenue), 2) AS total_revenue
FROM sales;

-- 2. Revenue by product
SELECT
    product,
    SUM(quantity) AS units_sold,
    ROUND(SUM(revenue), 2) AS revenue
FROM sales
GROUP BY product
ORDER BY revenue DESC;

-- 3. Revenue by city
SELECT
    city,
    ROUND(SUM(revenue), 2) AS revenue
FROM sales
GROUP BY city
ORDER BY revenue DESC;

-- 4. Daily revenue
SELECT
    order_date,
    ROUND(SUM(revenue), 2) AS daily_revenue
FROM sales
GROUP BY order_date
ORDER BY order_date;
