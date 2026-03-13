# Task 3: Product Pricing (Dictionaries)

price_dict = {
    "Laptop": 75000,
    "Mouse": 800,
    "Keyboard": 1500,
    "Monitor": 12000,
    "Headphones": 3000,
    "Webcam": 2000
}

print("Initial Prices:", price_dict)

# Add product
price_dict["Tablet"] = 25000

# Update price
price_dict["Mouse"] = 900

# Remove safely
product_to_remove = "Speaker"

if product_to_remove in price_dict:
    del price_dict[product_to_remove]
else:
    print(product_to_remove, "not found")

print("Updated Price Dictionary:", price_dict)

# Average price
total = 0

for price in price_dict.values():
    total += price

average = total / len(price_dict)

print("Average Price:", average)

# Max and Min price
max_product = max(price_dict, key=price_dict.get)
min_product = min(price_dict, key=price_dict.get)

print("Most Expensive:", max_product, price_dict[max_product])
print("Cheapest:", min_product, price_dict[min_product])