# Interests of two friends
friend_a = {"Python", "Cooking", "Hiking", "Movies"}
friend_b = {"Hiking", "Gaming", "Photography", "Python"}

common = friend_a.intersection(friend_b)
all_items = friend_a.union(friend_b)
unique_a = friend_a.difference(friend_b)

print("Common interests:", common)
print("All interests:", all_items)
print("Only Friend A:", unique_a)
