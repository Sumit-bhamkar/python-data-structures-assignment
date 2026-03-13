# Task 4: Combined Operations

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

price_dict = {
    "Laptop": 75000,
    "Mouse": 900,
    "Keyboard": 1500,
    "Monitor": 12000,
    "Headphones": 3000,
    "Webcam": 2000,
    "Tablet": 25000
}

# Create catalog
catalog = []

for i in range(len(products)):
    product_name = products[i]

    if product_name in price_dict:
        price = price_dict[product_name]
        category = categories[i]
        catalog.append((product_name, price, category))

print("Catalog:", catalog)

# Category -> Products
category_to_products = {}

for product_name, price, category in catalog:
    if category not in category_to_products:
        category_to_products[category] = []

    category_to_products[category].append(product_name)

print("Category Mapping:", category_to_products)

# Category with max products
max_category = None
max_count = 0

for category, product_list in category_to_products.items():
    if len(product_list) > max_count:
        max_count = len(product_list)
        max_category = category

print("Category with Maximum Products:", max_category)
print("Products:", category_to_products[max_category])