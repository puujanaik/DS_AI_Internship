import sqlite3

conn = sqlite3.connect("internship.db")
cur = conn.cursor()

# Create table
cur.execute("CREATE TABLE IF NOT EXISTS interns (id INTEGER, name TEXT, track TEXT, stipend INTEGER)")

# Insert sample data
cur.execute("DELETE FROM interns")
data = [
    (1, "Amit", "Data Science", 6000),
    (2, "Riya", "Web Dev", 4500),
    (3, "John", "Data Science", 7000),
    (4, "Meena", "AI/ML", 8000),
    (5, "Ali", "Web Dev", 5000),
]
cur.executemany("INSERT INTO interns VALUES (?, ?, ?, ?)", data)
conn.commit()

# 1. Filter
print("Data Science interns with stipend > 5000:")
for row in cur.execute("SELECT * FROM interns WHERE track='Data Science' AND stipend > 5000"):
    print(row)

# 2. Average stipend per track
print("\nAverage stipend per track:")
for row in cur.execute("SELECT track, AVG(stipend) FROM interns GROUP BY track"):
    print(row)

# 3. Count interns per track
print("\nNumber of interns per track:")
for row in cur.execute("SELECT track, COUNT(*) FROM interns GROUP BY track"):
    print(row)

conn.close()