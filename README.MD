Summary: The purpose of this script is to read a list of orders made by customers from a JSON file. The script will then create two new JSON files, one containing a list of customers, and one containing a list of items and how many times they have been ordered. 

First we have the main() which is called once the correct name of the python script is called and the JSON data file name is provided. We use argparse to provide help and information with this step as well as grab the JSON file name provided and make it a variable. 

Next we run the three action functions with the JSON data file name being provided as an argument. 

read_orders, takes the file name and loads it into memory and returns that data to main()

create_customers_file takes the JSON data and iterates through it and creates a new JSON file, that is formatted and collects the phone number and name of the customer. 

create_items_file takes the JSON data and iterates though each order and adds an entry for each unique item and adds to the number of orders. It produces a formatted JSON file with each item, its cost and how many times it was ordered. 
