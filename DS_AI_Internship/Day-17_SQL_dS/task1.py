import sqlite3

# 1. Connect to database (creates internship.db if it doesn't exist)
conn = sqlite3.connect("internship.db")

# 2. Create a cursor object
cursor = conn.cursor()

# 3. Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS interns (
    id INTEGER,
    name TEXT,
    track TEXT,
    stipend INTEGER
)
""")

# 4. Insert sample data
cursor.execute("DELETE FROM interns")  # Clear old data (so no duplicates)

interns_data = [
    (1, "Pooja", "Data Science", 8000),
    (2, "Komal", "Web Dev", 7000),
    (3, "Veeresh", "AI/ML", 9000),
    (4, "Farzana", "Cyber Security", 7500),
    (5, "KBH", "Data Science", 8500),
]

cursor.executemany("INSERT INTO interns VALUES (?, ?, ?, ?)", interns_data)

# 5. Commit changes
conn.commit()

# 6. Run SELECT query (only name and track)
cursor.execute("SELECT name, track FROM interns")

results = cursor.fetchall()

print("Name and Track of all interns:")
print("------------------------------")
for row in results:
    print(f"Name: {row[0]}, Track: {row[1]}")

# 7. Close connection
conn.close()