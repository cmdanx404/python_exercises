import json

json_data = '{"product": "Laptop", "price": 45000, "brand": "Acer"}'
data = json.loads(json_data)

print("Product:", data["product"])
print("Price:", data["price"])
