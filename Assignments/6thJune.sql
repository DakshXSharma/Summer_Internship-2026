-- How many unique nodes are there on the Data Bank system?
SELECT COUNT(DISTINCT node_id) AS unique_nodes
FROM customer_nodes;

-- What is the number of nodes per region?
SELECT 
    r.region_name,
    COUNT(DISTINCT c.node_id) AS total_nodes
FROM customer_nodes c
JOIN regions r
ON c.region_id = r.region_id
GROUP BY r.region_name;

-- How many customers are allocated to each region?
SELECT 
    r.region_name,
    COUNT(DISTINCT c.customer_id) AS total_customers
FROM customer_nodes c
JOIN regions r
ON c.region_id = r.region_id
GROUP BY r.region_name;

-- How many days on average are customers reallocated to a different node?
SELECT 
    AVG(DATEDIFF(DAY, start_date, end_date)) AS avg_reallocation_days
FROM customer_nodes
WHERE end_date != '9999-12-31';

-- What is the median, 80th and 95th percentile for this same reallocation days metric for each region?
WITH cte AS (
    SELECT 
        r.region_name,
        DATEDIFF(DAY, c.start_date, c.end_date) AS reallocation_days
    FROM customer_nodes c
    JOIN regions r
    ON c.region_id = r.region_id
    WHERE c.end_date != '9999-12-31'
)
SELECT DISTINCT
    region_name,
    PERCENTILE_CONT(0.5)
    WITHIN GROUP (ORDER BY reallocation_days)
    OVER (PARTITION BY region_name) AS median,
    PERCENTILE_CONT(0.8)
    WITHIN GROUP (ORDER BY reallocation_days)
    OVER (PARTITION BY region_name) AS percentile_80,
    PERCENTILE_CONT(0.95)
    WITHIN GROUP (ORDER BY reallocation_days)
    OVER (PARTITION BY region_name) AS percentile_95
FROM cte;

-- What is the unique count and total amount for each transaction type?
SELECT 
    txn_type,
    COUNT(*) AS transaction_count,
    SUM(txn_amount) AS total_amount
FROM customer_transactions
GROUP BY txn_type;

-- What is the average total historical deposit counts and amounts for all customers?
WITH deposit_data AS (
    SELECT 
        customer_id,
        COUNT(*) AS deposit_count,
        SUM(txn_amount) AS total_deposit_amount
    FROM customer_transactions
    WHERE txn_type = 'deposit'
    GROUP BY customer_id
)
SELECT 
    AVG(CAST(deposit_count AS FLOAT)) AS avg_deposit_count,
    AVG(CAST(total_deposit_amount AS FLOAT)) AS avg_deposit_amount
FROM deposit_data;

-- For each month - how many Data Bank customers make more than 1 deposit and either 1 purchase or 1 withdrawal in a single month?
WITH monthly_transactions AS (
    SELECT 
        customer_id,
        MONTH(txn_date) AS month_number,
        SUM(CASE 
            WHEN txn_type = 'deposit' THEN 1 
            ELSE 0 
        END) AS deposit_count,
        SUM(CASE 
            WHEN txn_type = 'purchase' THEN 1 
            ELSE 0 
        END) AS purchase_count,
        SUM(CASE 
            WHEN txn_type = 'withdrawal' THEN 1 
            ELSE 0 
        END) AS withdrawal_count
    FROM customer_transactions
    GROUP BY customer_id, MONTH(txn_date)
)
SELECT 
    month_number,
    COUNT(customer_id) AS customer_count
FROM monthly_transactions
WHERE deposit_count > 1
AND (
    purchase_count >= 1
    OR withdrawal_count >= 1
)
GROUP BY month_number
ORDER BY month_number;