import sqlite3
import pandas as pd

# Connect to SQLite database
conn = sqlite3.connect("internship.db")
cur = conn.cursor()

# Create interns table
cur.execute("""
CREATE TABLE IF NOT EXISTS interns (
    id INTEGER,
    name TEXT,
    track TEXT,
    stipend INTEGER
)
""")

# Create mentors table
cur.execute("""
CREATE TABLE IF NOT EXISTS mentors (
    mentor_id INTEGER,
    mentor_name TEXT,
    track TEXT
)
""")

# Clear old data
cur.execute("DELETE FROM interns")
cur.execute("DELETE FROM mentors")

# Insert sample data into interns
interns_data = [
    (1, "Amit", "Data Science", 6000),
    (2, "Riya", "Web Dev", 4500),
    (3, "John", "Data Science", 7000),
    (4, "Meena", "AI/ML", 8000),
    (5, "Ali", "Web Dev", 5000),
]
cur.executemany("INSERT INTO interns VALUES (?, ?, ?, ?)", interns_data)

# Insert sample data into mentors
mentors_data = [
    (1, "Dr. Sharma", "Data Science"),
    (2, "Ms. Patel", "Web Dev"),
    (3, "Mr. Rao", "AI/ML"),
]
cur.executemany("INSERT INTO mentors VALUES (?, ?, ?)", mentors_data)

conn.commit()

# INNER JOIN query
query = """
SELECT interns.name AS intern_name,
       interns.track,
       mentors.mentor_name
FROM interns
INNER JOIN mentors
ON interns.track = mentors.track
"""

# Load result into Pandas DataFrame
df = pd.read_sql_query(query, conn)

# Print result
print("Interns with their Mentors:")
print(df)

# Close connection
conn.close()