# Creating contacts dictionary
contacts = {
    "Pooja": "7618714163",
    "Krishn": "987654321",
    "Komal": "123456789"
}

# Adding a new contact
contacts["Kiran"] = "8496024156"

# Updating an existing contact
contacts["Krishn"] = "9645278517"

print("Lookup Pooja:", contacts.get("Pooja", "Contact not found"))
print("Lookup Mohan:", contacts.get("Mohan", "Contact not found"))


print("\nAll Contacts:")
for name, phone in contacts.items():
    print("Contact:", name, "| Phone:", phone)
