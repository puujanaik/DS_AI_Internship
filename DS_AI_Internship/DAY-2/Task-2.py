
# Ask for total bill amount
bill = float(input("Enter total bill amount: "))

# Ask for number of people
people = int(input("Enter number of people: "))

# Calculate share per person
share = bill / people

# Output result
print("Total Bill:", bill)
print("Each person pays:", share)

# Bonus: check data types
print(type(bill))
print(type(people))
print(type(share))
