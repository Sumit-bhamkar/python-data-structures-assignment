# Task 2: Categories (Sets)

products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones", "Webcam", "Tablet", "Charger"]

categories = [
    "Electronics",
    "Accessories",
    "Accessories",
    "Electronics",
    "Audio",
    "Electronics",
    "Electronics",
    "Accessories"
]

# Create set
categories_set = set(categories)

print("Unique Categories:", categories_set)

# Add new category
categories_set.add("Gaming")

# Duplicate ignored
categories_set.add("Electronics")

print("Categories after adding:", categories_set)

# Check category
print("Is 'Audio' present?", "Audio" in categories_set)

# Total unique categories
print("Total Unique Categories:", len(categories_set))