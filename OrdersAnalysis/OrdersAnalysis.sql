create table df_orders (
    order_id int primary key,
    order_date date,
    ship_mode varchar(20),
    segment varchar(20),
    country varchar(20),
    city varchar(20),
    state varchar(20),
    postal_code varchar(20),
    region varchar(20),
    category varchar(20),
    sub_category varchar(20),
    product_id varchar(50),
    quantity int,
    discount decimal(7,2),
    sale_price decimal(7,2),
    profit decimal(7,2)
);

select * from df_orders;

#find top 10 highest reveue generating products 
select product_id, sum(sale_price) as sales
from df_orders
group by product_id
order by sales desc
limit 10;


#find top 5 highest selling products in each region
with cte as (
    select region, product_id, sum(sale_price) as sales
    from df_orders
    group by region, product_id
)
select region, product_id, sales
from (
    select region, product_id, sales,
           row_number() over (partition by region order by sales desc) as rn
    from cte
) as ranked
where rn <= 5;

#find month over month growth comparison for 2022 and 2023 sales eg : jan 2022 vs jan 2023
#Calculate total sales for each month in 2022
SELECT 
    MONTH(order_date) AS month,
    YEAR(order_date) AS year,
    SUM(sale_price) AS total_sales_2022
FROM 
    df_orders
WHERE 
    YEAR(order_date) = 2022
GROUP BY 
    MONTH(order_date);

#Calculate total sales for each month in 2023
SELECT 
    MONTH(order_date) AS month,
    YEAR(order_date) AS year,
    SUM(sale_price) AS total_sales_2023
FROM 
    df_orders
WHERE 
    YEAR(order_date) = 2023
GROUP BY 
    MONTH(order_date);

#Calculate month-over-month growth comparison for 2022 and 2023
SELECT 
    2022_sales.month AS month,
    2022_sales.total_sales_2022 AS sales_2022,
    2023_sales.total_sales_2023 AS sales_2023,
    (2023_sales.total_sales_2023 - 2022_sales.total_sales_2022) / 2022_sales.total_sales_2022 AS growth_rate
FROM 
    (
        SELECT 
            MONTH(order_date) AS month,
            SUM(sale_price) AS total_sales_2022
        FROM 
            df_orders
        WHERE 
            YEAR(order_date) = 2022
        GROUP BY 
            MONTH(order_date)
    ) AS 2022_sales
INNER JOIN 
    (
        SELECT 
            MONTH(order_date) AS month,
            SUM(sale_price) AS total_sales_2023
        FROM 
            df_orders
        WHERE 
            YEAR(order_date) = 2023
        GROUP BY 
            MONTH(order_date)
    ) AS 2023_sales ON 2022_sales.month = 2023_sales.month;




#for each category which month had highest sales 
SELECT category, MONTH(order_date) AS month, SUM(sale_price) AS total_sales
FROM df_orders
GROUP BY category, MONTH(order_date)
HAVING total_sales = (
    SELECT MAX(sub.total_sales)
    FROM (
        SELECT category, MONTH(order_date) AS month, SUM(sale_price) AS total_sales
        FROM df_orders
        GROUP BY category, MONTH(order_date)
    ) AS sub
    WHERE sub.category = df_orders.category
)
ORDER BY category, month;




#which sub category had highest growth by profit in 2023 compare to 2022
WITH cte AS (
    SELECT 
        sub_category,
        YEAR(order_date) AS order_year,
        SUM(profit) AS profit
    FROM df_orders
    WHERE YEAR(order_date) IN (2022, 2023)
    GROUP BY sub_category, YEAR(order_date)
),
cte2 AS (
    SELECT 
        sub_category,
        SUM(CASE WHEN order_year = 2022 THEN profit ELSE 0 END) AS profit_2022,
        SUM(CASE WHEN order_year = 2023 THEN profit ELSE 0 END) AS profit_2023
    FROM cte
    GROUP BY sub_category
)
SELECT 
    sub_category,
    profit_2022,
    profit_2023,
    (profit_2023 - profit_2022) AS profit_growth
FROM cte2
ORDER BY profit_growth DESC
LIMIT 1