# Kennedy Watson
# SCIS 111-113
# Family dictionary

# Create dictionary with the 8 family members and relationships
family = {
    "Nicole": "Mom",
    "Devin": "Dad",
    "Kaelynn": "Sister",
    "Kooper": "Brother",
    "Patricia": "Grandma",
    "James": "Grandpa",
    "Shareka": "Aunt",
    "Michelle":"Aunt 2",
    "Michael": "Uncle"
}

# Print the individual relationships
print("Relationship of Nicole:", family.get("Nicole"))  
print("Relationship of Kaelynn:", family["Kaelynn"])         # Using []

# Print all keys (names) and values (relationships)
print("Family Members (Keys):", family.keys())
print("Relationships (Values):", family.values())

# Update a relationship
family["Kooper"] = "Younger Brother"
print("\nUpdated Kooper's relationship:", family["Kooper"])

# Add a new family member
family["Chris"] = "Cousin"
print("\nAdded Chris to the family. Updated dictionary:")
print(family)

# Check for a specific key using "in"
print("\nIs 'Nicole' in the family?", "Nicole" in family)
print("Is 'Sharon' in the family?", "Sharon" in family)

# Print  dictionary
print("\nComplete Family Dictionary:")
print(family)
