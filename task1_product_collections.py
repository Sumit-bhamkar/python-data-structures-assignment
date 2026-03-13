# Task 1: Product Collections (Lists & Tuples)

# 1. Create a list of products
products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones", "Webcam"]

# 2. Create a tuple
sample_product = ("Laptop", 75000, "Electronics")

# 3. Print 2nd and last product
print("Second Product:", products[1])
print("Last Product:", products[-1])

# 4. Append two new products
products.append("Tablet")
products.append("Charger")

print("Updated Product List:", products)

# Extra: Convert tuple → list → update → tuple
sample_product_list = list(sample_product)
sample_product_list[1] = 72000
sample_product = tuple(sample_product_list)

print("Updated Sample Product:", sample_product)