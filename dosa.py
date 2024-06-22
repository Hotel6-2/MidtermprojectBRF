import json
import sys

def read_orders(file_name):
    with open(file_name, 'r') as file:
        orders = json.load(file)
    return orders

def create_customers_file(orders):
    customers = {}
    for order in orders:
        phone = order['phone']
        name = order['customer']
        customers[phone] = name
    
    with open('customers.json', 'w') as file:
        json.dump(customers, file, indent=4)

def create_items_file(orders):
    items = {}
    for order in orders:
        for item in order['items']:
            name = item['name']
            price = item['price']
            if name not in items:
                items[name] = {'price': price, 'orders': 0}
            items[name]['orders'] += 1
    
    with open('items.json', 'w') as file:
        json.dump(items, file, indent=4)

if __name__ == "__main__":
    orders = read_orders(sys.argv[1])
    create_customers_file(orders)
    create_items_file(orders)
