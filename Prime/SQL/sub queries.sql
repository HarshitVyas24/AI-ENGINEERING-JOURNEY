USE price;

SELECT * FROM customers;
SELECT * FROM orders;


-- SUB queries (USING WHERE)

SELECT * 
FROM orders 
WHERE amount > (
	SELECT AVG(amount)
    FROM orders

);

-- USING SELECT (operation ---> column under operation--->the key )

SELECT name, (
	SELECT COUNT(*)
    FROM orders o
    WHERE o.customer_id = c.customer_id
) AS order_count
FROM customers c;


-- SUB QUERIES with FROM

SELECT 

	summary.customer_id,
    summary.avg_amount

FROM (
	SELECT 
		customer_id,
        AVG(amount) AS avg_amount
	FROM orders
    GROUP BY customer_id
) AS summary ;

