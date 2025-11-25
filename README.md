# Task 7 – Basic Sales Summary from a Tiny SQLite Database (Python + SQL)

This folder contains a **GitHub-ready** solution for:

> TASK 7: Get Basic Sales Summary from a Tiny SQLite Database using Python

## 📂 Contents

- `sales_data.db` – Tiny SQLite database with a single table: `sales`.
- `task7_sales_summary.py` – Python script that:
  - Connects to `sales_data.db`
  - Runs an aggregation SQL query
  - Prints a basic sales summary
  - Plots a bar chart of revenue per product and saves it as `sales_chart.png`

## 🗄 Database Schema

The `sales` table has the following columns:

```sql
CREATE TABLE sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT,
    quantity INTEGER,
    price REAL
);
```

Sample data is already inserted, including products like **Laptop**, **Mouse**, **Keyboard**, and **Monitor**.

## ▶️ How to Run

1. Make sure you have **Python 3** installed.
2. Install required libraries (only once):

   ```bash
   pip install pandas matplotlib
   ```

3. Run the script:

   ```bash
   python task7_sales_summary.py
   ```

4. You will see:
   - A printed table of total quantity and revenue per product in the terminal.
   - A bar chart image saved as: `sales_chart.png`.

## 🧮 SQL Logic Used

Inside the script, the key SQL query is:

```sql
SELECT 
    product,
    SUM(quantity) AS total_qty,
    SUM(quantity * price) AS revenue
FROM sales
GROUP BY product
ORDER BY revenue DESC;
```

This:
- Groups data **by product**
- Calculates **total quantity** sold per product
- Calculates **total revenue** per product as `SUM(quantity * price)`

## ✅ Learning Outcomes

- How to connect Python to a **SQLite** database using `sqlite3`
- How to run SQL queries and load results into **pandas**
- How to print tabular results
- How to create a simple **matplotlib** bar chart from SQL results

You can directly upload these files to a GitHub repository as your solution for **Task 7**.
