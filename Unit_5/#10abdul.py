
'''
# create a class OrderManager
# Implement methods to do the following:
#- read a file called orders.json, store
# in a class variable called orderlist
​
#- get the total number of orders
#- get the person with the most orders
#- get the person with the largest total order value
#- ge the most expensive item ordered
#- get the most frequently ordered item
'''
​
​import json
​
class OrderManager:
    def __init__(self):
        self.orderlist = []
        
    def filereader (self,input_file):
        with open(input_file, 'r') as input_file:
            self.orderlist = json.load(input_file)
    
    def total_orders(self):
        total_orders = 0
        for item in self.orderlist:
            total_orders += len(item['orders']) 
           
        return total_orders
​
o = OrderManager()
o.filereader('orders.json')
print (o.total_orders())
