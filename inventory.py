#This program helps manage the stock in a Nike warehouse.

#Import tabulate module for display of information
from tabulate import tabulate

#Shoe class.
class Shoe():
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    #Function reads information from inventory.txt file.
    #A Try-except block has been implemented and returns a statement if file is not found.
    def read_data(f):
        try:
            with open('inventory.txt', 'r') as f:
                    inventory = f.read()
                    return inventory
        except FileNotFoundError:
            print("The file you are trying to open does not exist.")
        finally:
            if f is not None:
                f.close()
                
#5 objects have been stored in the list shoes.                
shoes = []
shoes.append( (Shoe("South Africa", "SKU44386", "Air Max 90", 2300, 20)) )
shoes.append( (Shoe("China", "SKU90000", "Jordan 1", 3200, 50)) )
shoes.append( (Shoe("Vietnam", "SKU63221", "Blazer", 1700, 19)) )
shoes.append( (Shoe("United States", "SKU29077", "Cortez", 970, 60)) )
shoes.append( (Shoe("Russia", "SKU89999", "Air Force 1", 2000, 43)) )


#The search_function function finds a product in the list by entering a code.
def search_product():
    product_code = input("Enter product code:")
    for i in shoes:
        if product_code == i.code:
            product = i.country, i.code, i.product, i.cost, i.quantity
            print(product)

#The restock function finds the lowest quantity in the list and restocks it.
#The input function asks user to enter amount of items they'd like to stock.
def restock():
    quantity_of_products = []
    number_of_stock_items = int(input("Enter number of stock items:"))
    for i in shoes:
        quantity_of_products.append(i.quantity)
    lowest_quantity = min(quantity_of_products)
    for i in shoes:
        if lowest_quantity == i.quantity:
            i.quantity += number_of_stock_items
            print(i.product, "has been stocked.")

#This function finds the highest quantity prints the item for sale.
def for_sale():
    quantity_of_products = []
    for i in shoes:
        quantity_of_products.append(i.quantity)
    highest_quantity = max(quantity_of_products)
    for i in shoes:
        if highest_quantity == i.quantity:
            print(i.product, "for sale.")

#This function calculate the value of items.
#The cost and quantity have been multiplied to get the value.
#A new list shoe_items has been created with value added.
def value_per_item():
    shoe_items = []
    for i in shoes:
        value = i.cost*i.quantity
        i = [i.country, i.code, i.product, i.cost, i.quantity, value]
        shoe_items.append(i)
    return shoe_items

#The variable heading contains the headings for the table.
heading = ["Country", "Code", "Product", "Cost", "Quantity", "Value"]

#Value per item function has been called.
data = value_per_item()

#Print table.
print(tabulate(data, headers=heading, tablefmt="grid"))






    
                






