import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# 1. Connect to the SQLite database
conn = sqlite3.connect("sales_data.db")

# 2. Execute SQL query to get total quantity and revenue per product
query = """
SELECT 
    product,
    SUM(quantity) AS total_quantity,
    SUM(quantity * price) AS total_revenue
FROM sales
GROUP BY product
ORDER BY total_revenue DESC;
"""

# 3. Load the result into a Pandas DataFrame
df = pd.read_sql_query(query, conn)

# 4. Display the result
print("\nSales Summary:")
print(df)

# 5. Plot revenue by product
plt.figure(figsize=(8, 5))
plt.bar(df['product'], df['total_revenue'])
plt.title('Total Revenue by Product')
plt.xlabel('Product')
plt.ylabel('Revenue')
plt.tight_layout()

# 6. Save the chart
plt.savefig("sales_revenue_chart.png")
print("\nChart saved as sales_revenue_chart.png")

# Close the connection
conn.close()
