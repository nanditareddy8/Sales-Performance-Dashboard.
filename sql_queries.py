import pandas as pd
import sqlite3

# 1. Read the cleaned data
df = pd.read_csv("clean_superstore.csv")

# 2. Connect to a SQLite database (this creates a file called sales_data.db)
conn = sqlite3.connect("sales_data.db")

# 3. Load the data into a SQL table called 'sales'
df.to_sql("sales", conn, if_exists="replace", index=False)
print("✅ Data successfully loaded into SQLite database!")

# 4. Run a basic SQL query to check the total sales
query = """
SELECT SUM(sales) AS total_revenue
FROM sales;
"""

# 5. Execute the query and print the result
result = pd.read_sql(query, conn)
print("\n--- Total Revenue ---")
print(result)

# 6. Close the connection
# --- QUERY 1: Sales by Region ---
print("\n--- 1. Total Sales by Region ---")
q1 = """
SELECT region, ROUND(SUM(sales), 2) AS total_sales
FROM sales
GROUP BY region
ORDER BY total_sales DESC;
"""
print(pd.read_sql(q1, conn))

# --- QUERY 2: Top 10 Customers ---
print("\n--- 2. Top 10 Customers by Revenue ---")
q2 = """
SELECT customer_name, ROUND(SUM(sales), 2) AS total_spent
FROM sales
GROUP BY customer_name
ORDER BY total_spent DESC
LIMIT 10;
"""
print(pd.read_sql(q2, conn))

# --- QUERY 3: Monthly Sales Trend ---
# Since order_date is stored as text in SQLite, we use STRFTIME to extract the year and month
print("\n--- 3. Monthly Sales Trend (Top 5) ---")
q3 = """
SELECT STRFTIME('%Y-%m', order_date) AS month, ROUND(SUM(sales), 2) AS total_sales
FROM sales
GROUP BY month
ORDER BY month DESC
LIMIT 5;
"""
print(pd.read_sql(q3, conn))
conn.close()