import sqlite3

conn = sqlite3.connect("sales_data.db")
cur = conn.cursor()

# create table
cur.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    price REAL NOT NULL,
    sale_date TEXT
)
""")

# sample data
rows = [
    ("Product A", 10, 50, "2025-01-03"),
    ("Product B", 5, 100, "2025-01-04"),
    ("Product A", 7, 50, "2025-01-05"),
    ("Product C", 3, 150, "2025-01-06"),
]

cur.executemany("INSERT INTO sales (product, quantity, price, sale_date) VALUES (?, ?, ?, ?)", rows)
conn.commit()
conn.close()

print("sales_data.db created with sample data.")

