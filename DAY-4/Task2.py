# several duplicate IDs:
raw_logs = ["ID01", "ID02", "ID01", "ID05", "ID02", "ID08", "ID01"]

# set function
unique_users = set()

for id in raw_logs:
    unique_users.add(id)
# comparison
print("Unique Users:", unique_users)
print("ID05 in users:", "ID05" in unique_users)
print("Total entries:", len(raw_logs))
print("Unique count:", len(unique_users))

