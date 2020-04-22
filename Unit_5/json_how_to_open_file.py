import json

with open('orders.json', 'r') as input_file:
    order_list = json.load(input_file)

print(order_list)