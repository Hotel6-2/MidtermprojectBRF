import json
import argparse

def read_orders(file_name):
    with open(file_name, 'r') as file:
        orders = json.load(file)
    return orders

def create_customers_file(orders):
    customers = {}
    for order in orders:
        phone = order['phone']
        name = order['name']
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

def main():
    parser = argparse.ArgumentParser(description='Process Dosa restaurant orders.')
    parser.add_argument('orders_file', type=str, help='The JSON file containing the orders')
    args = parser.parse_args()
    orders_file = args.orders_file
    orders = read_orders(orders_file)
    create_customers_file(orders)
    create_items_file(orders)

if __name__ == "__main__":
    main()