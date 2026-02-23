# Step 1: Create a file and write 5 numbers into it
with open("numbers.txt", "w") as file:
    file.write("10\n")
    file.write("20\n")
    file.write("30\n")
    file.write("40\n")
    file.write("50\n")

# Step 2: Open the file and read its contents
with open("numbers.txt", "r") as file:
    content = file.read()

# Step 3: Print the file content
print("Numbers in the file are:")
print(content)
