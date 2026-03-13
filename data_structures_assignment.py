# -----------------------------------------
# Task 1: Product Collections (Lists & Tuples)
# -----------------------------------------

# 1. Create a list of products
products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones", "Webcam"]

# 2. Create a tuple (product_name, price, category)
sample_product = ("Laptop", 75000, "Electronics")

# 3. Print the 2nd and last product
print("Second Product:", products[1])
print("Last Product:", products[-1])

# 4. Append two new products
products.append("Tablet")
products.append("Charger")

print("Updated Product List:", products)

# Extra (optional): Convert tuple -> list, update price, convert back to tuple
sample_product_list = list(sample_product)
sample_product_list[1] = 72000
sample_product = tuple(sample_product_list)

print("Updated Sample Product Tuple:", sample_product)



# -----------------------------------------
# Task 2: Categories (Sets)
# -----------------------------------------

# Create a parallel category list
categories = ["Electronics", "Accessories", "Accessories", "Electronics", "Audio", "Electronics", "Electronics", "Accessories"]

# 1. Create set of categories
categories_set = set(categories)

print("Unique Categories:", categories_set)

# 2. Add new category
categories_set.add("Gaming")

# Try adding duplicate
categories_set.add("Electronics")

print("Categories after adding:", categories_set)

# 3. Check if category exists
print("Is 'Audio' category present?", "Audio" in categories_set)

# Extra: Count unique categories
print("Total Unique Categories:", len(categories_set))



# -----------------------------------------
# Task 3: Product Pricing (Dictionaries)
# -----------------------------------------

# 1. Create dictionary
price_dict = {
    "Laptop": 75000,
    "Mouse": 800,
    "Keyboard": 1500,
    "Monitor": 12000,
    "Headphones": 3000,
    "Webcam": 2000
}

print("Initial Price Dictionary:", price_dict)

# Add new product
price_dict["Tablet"] = 25000

# Update price
price_dict["Mouse"] = 900

# Remove product safely
product_to_remove = "Speaker"

if product_to_remove in price_dict:
    del price_dict[product_to_remove]
else:
    print(product_to_remove, "not found in dictionary")

print("Updated Price Dictionary:", price_dict)

# Calculate average price
total_price = 0
for price in price_dict.values():
    total_price += price

average_price = total_price / len(price_dict)

print("Average Price:", average_price)

# Extra: Find max and min price product
max_product = max(price_dict, key=price_dict.get)
min_product = min(price_dict, key=price_dict.get)

print("Most Expensive Product:", max_product, price_dict[max_product])
print("Cheapest Product:", min_product, price_dict[min_product])



# -----------------------------------------
# Task 4: Combined Operations
# -----------------------------------------

# Create catalog list of tuples (product_name, price, category)
catalog = []

for i in range(len(products)):
    product_name = products[i]

    if product_name in price_dict:
        price = price_dict[product_name]
        category = categories[i]
        catalog.append((product_name, price, category))

print("Catalog:", catalog)

# Create category -> products dictionary
category_to_products = {}

for product_name, price, category in catalog:
    if category not in category_to_products:
        category_to_products[category] = []

    category_to_products[category].append(product_name)

print("Category to Products Mapping:", category_to_products)

# Find category with maximum products
max_category = None
max_count = 0

for category, product_list in category_to_products.items():
    if len(product_list) > max_count:
        max_count = len(product_list)
        max_category = category

print("Category with Maximum Products:", max_category)
print("Products in that Category:", category_to_products[max_category])