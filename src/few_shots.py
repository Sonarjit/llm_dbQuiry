few_shots = [
    {'Question' : "How many t-shirts do we have left for Nike in XS size and white color?",
     'SQLQuery' : "SELECT sum(stock_quantity) FROM t_shirts WHERE brand = 'Nike' AND color = 'White' AND size = 'XS'",
     },
    {'Question': "How much is the total price of the inventory for all S-size t-shirts?",
     'SQLQuery':"SELECT SUM(price*stock_quantity) FROM t_shirts WHERE size = 'S'",
     },
    {'Question': "If we have to sell all the Levi’s T-shirts today with discounts applied. How much revenue  our store will generate (post discounts)?" ,
     'SQLQuery' : """SELECT sum(a.total_amount * ((100-COALESCE(discounts.pct_discount,0))/100)) as total_revenue from
(select sum(price*stock_quantity) as total_amount, t_shirt_id from t_shirts where brand = 'Levi'
group by t_shirt_id) a left join discounts on a.t_shirt_id = discounts.t_shirt_id
 """,
     } ,
     {'Question' : "If we have to sell all the Levi’s T-shirts today. How much revenue our store will generate without discount?" ,
      'SQLQuery': "SELECT SUM(price * stock_quantity) FROM t_shirts WHERE brand = 'Levi'",
      },
    {'Question': "How many white color Levi's shirt I have?",
     'SQLQuery' : "SELECT sum(stock_quantity) FROM t_shirts WHERE brand = 'Levi' AND color = 'White'",
     },

     {
        "Question": "What is the total revenue we would generate if we sold all remaining extra large black Levi shirts at their final discounted price?",
        "SQLQuery": "SELECT SUM(t.stock_quantity * t.price * (1 - COALESCE(d.pct_discount, 0) / 100)) AS potential_revenue FROM t_shirts t LEFT JOIN discounts d ON t.t_shirt_id = d.t_shirt_id WHERE LOWER(t.brand) = 'levi' AND LOWER(t.color) = 'black' AND t.size = 'XL';"
    },
    {
        "Question": "Find all brands that currently have a t-shirt with a discount greater than 20% but still have more than 50 items left in stock.",
        "SQLQuery": "SELECT DISTINCT t.brand FROM t_shirts t INNER JOIN discounts d ON t.t_shirt_id = d.t_shirt_id WHERE d.pct_discount > 20.00 AND t.stock_quantity > 50;"
    },
    {
        "Question": "Which specific t-shirt ID has the highest dollar amount deducted from its original price due to a discount?",
        "SQLQuery": "SELECT t.t_shirt_id FROM t_shirts t INNER JOIN discounts d ON t.t_shirt_id = d.t_shirt_id ORDER BY (t.price * (d.pct_discount / 100)) DESC LIMIT 1;"
    },
    {
        "Question": "Show the average percentage discount applied to Nike shirts compared to Adidas shirts.",
        "SQLQuery": "SELECT t.brand, AVG(COALESCE(d.pct_discount, 0)) AS avg_discount FROM t_shirts t LEFT JOIN discounts d ON t.t_shirt_id = d.t_shirt_id WHERE LOWER(t.brand) IN ('nike', 'adidas') GROUP BY t.brand;"
    },
    {
        "Question": "List the total number of items left in stock for each size, but only include shirts that do not have any active discounts.",
        "SQLQuery": "SELECT t.size, SUM(t.stock_quantity) AS total_stock FROM t_shirts t LEFT JOIN discounts d ON t.t_shirt_id = d.t_shirt_id WHERE d.discount_id IS NULL GROUP BY t.size;"
    },
    {
        "Question": "How many medium or large Van Huesen shirts are priced under 30 dollars after applying their active discount?",
        "SQLQuery": "SELECT COUNT(*) FROM t_shirts t LEFT JOIN discounts d ON t.t_shirt_id = d.t_shirt_id WHERE LOWER(t.brand) = 'van huesen' AND t.size IN ('M', 'L') AND (t.price * (1 - COALESCE(d.pct_discount, 0) / 100)) < 30;"
    },
    {
        "Question": "Find the color and size of the cheapest Van Huesen shirt taking into account its current discount.",
        "SQLQuery": "SELECT t.color, t.size FROM t_shirts t LEFT JOIN discounts d ON t.t_shirt_id = d.t_shirt_id WHERE LOWER(t.brand) = 'van huesen' ORDER BY (t.price * (1 - COALESCE(d.pct_discount, 0) / 100)) ASC LIMIT 1;"
    },
    {
        "Question": "List all combinations of brand and color where the total stock quantity across all sizes is less than 15 units.",
        "SQLQuery": "SELECT t.brand, t.color FROM t_shirts t GROUP BY t.brand, t.color HAVING SUM(t.stock_quantity) < 15;"
    },
    {
        "Question": "Calculate the total inventory value based on original price for shirts that have a discount, grouped by whether they are small or extra small.",
        "SQLQuery": "SELECT t.size, SUM(t.stock_quantity * t.price) AS total_value FROM t_shirts t INNER JOIN discounts d ON t.t_shirt_id = d.t_shirt_id WHERE t.size IN ('XS', 'S') GROUP BY t.size;"
    },
    {
        "Question": "Show a list of all unique brands along with a column indicating 'Has Promotion' if any of its shirts are discounted, or 'No Promotion' if none are.",
        "SQLQuery": "SELECT t.brand, CASE WHEN COUNT(d.discount_id) > 0 THEN 'Has Promotion' ELSE 'No Promotion' END AS promotion_status FROM t_shirts t LEFT JOIN discounts d ON t.t_shirt_id = d.t_shirt_id GROUP BY t.brand;"
    },
    {
        "Question": "How much potential revenue are we losing due to discounts on Nike shirts?",
        "SQLQuery": "SELECT SUM(t.stock_quantity * t.price * (d.pct_discount / 100)) AS revenue_lost FROM t_shirts t INNER JOIN discounts d ON t.t_shirt_id = d.t_shirt_id WHERE LOWER(t.brand) = 'nike';"
    },
    {
        "Question": "Which brands do not have any items on discount right now?",
        "SQLQuery": "SELECT t.brand FROM t_shirts t LEFT JOIN discounts d ON t.t_shirt_id = d.t_shirt_id GROUP BY t.brand HAVING COUNT(d.discount_id) = 0;"
    },
    {
        "Question": "What is the total count of t-shirts currently on sale versus those sold at full price?",
        "SQLQuery": "SELECT CASE WHEN d.discount_id IS NOT NULL THEN 'On Sale' ELSE 'Full Price' END AS pricing_status, SUM(t.stock_quantity) AS total_items FROM t_shirts t LEFT JOIN discounts d ON t.t_shirt_id = d.t_shirt_id GROUP BY pricing_status;"
    },
    {
        "Question": "Show the highest final price (after discount) for each brand.",
        "SQLQuery": "SELECT t.brand, MAX(t.price * (1 - COALESCE(d.pct_discount, 0) / 100)) AS highest_final_price FROM t_shirts t LEFT JOIN discounts d ON t.t_shirt_id = d.t_shirt_id GROUP BY t.brand;"
    },
    {
        "Question": "Find the total stock of Nike shirts that are either red in size small, or black in size large.",
        "SQLQuery": "SELECT SUM(t.stock_quantity) FROM t_shirts t WHERE LOWER(t.brand) = 'nike' AND ((LOWER(t.color) = 'red' AND t.size = 'S') OR (LOWER(t.color) = 'black' AND t.size = 'L'));"
    },
    {
        "Question": "List the IDs of shirts that have a stock of more than 100 but have never been discounted.",
        "SQLQuery": "SELECT t.t_shirt_id FROM t_shirts t LEFT JOIN discounts d ON t.t_shirt_id = d.t_shirt_id WHERE t.stock_quantity > 100 AND d.discount_id IS NULL;"
    },
    {
        "Question": "What is the average original price of medium shirts that have a discount of 15 percent or more?",
        "SQLQuery": "SELECT AVG(t.price) FROM t_shirts t INNER JOIN discounts d ON t.t_shirt_id = d.t_shirt_id WHERE t.size = 'M' AND d.pct_discount >= 15.00;"
    },
    {
        "Question": "How many different colors does Adidas currently manufacture in extra large that are actually in stock?",
        "SQLQuery": "SELECT COUNT(DISTINCT t.color) FROM t_shirts t WHERE LOWER(t.brand) = 'adidas' AND t.size = 'XL' AND t.stock_quantity > 0;"
    },
    {
        "Question": "Which specific size has the highest average discount percentage applied to it across all brands?",
        "SQLQuery": "SELECT t.size FROM t_shirts t INNER JOIN discounts d ON t.t_shirt_id = d.t_shirt_id GROUP BY t.size ORDER BY AVG(d.pct_discount) DESC LIMIT 1;"
    },
    {
        "Question": "Provide a complete inventory summary showing the brand, total items, and total base value of all white shirts.",
        "SQLQuery": "SELECT t.brand, SUM(t.stock_quantity) AS total_items, SUM(t.stock_quantity * t.price) AS total_base_value FROM t_shirts t WHERE LOWER(t.color) = 'white' GROUP BY t.brand;"
    }
]
