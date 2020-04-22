'''
# create a class OrderManager
# Implement methods to do the following:
#- read a file called orders.json, store
# in a class variable called orderlist

#- get the total number of orders
#- get the person with the most orders
#- get the person with the largest total order value
#- ge the most expensive item ordered
#- get the most frequently ordered item
'''

import json

class OrderManager:
    def __init__(self): #constructer/default init (self)
        self.order_list = [] # this is to create a new variable/property in Class: orderlist will be assigned to orders.json
    
    def file_reader(self, input_file): # this is a method to read file
        with open(input_file, 'r') as input_file:
            self.order_list = json.load(input_file)
    
    def total_orders(self): # this is a method to count orders
        total_orders = 0
        for item in self.order_list:
            total_orders += len(item['orders'])
        return total_orders

#now need to specify an object in OrderManager Class: object = ordermanager

o = OrderManager() #to create an object within Class - object "o" - dont forget ()
o.file_reader('orders.json') # to apply a method: Open file orders.json here

print(o.total_orders()) #one file orders.json opened. this apply "total_orders" method - don't forget ()





           
    