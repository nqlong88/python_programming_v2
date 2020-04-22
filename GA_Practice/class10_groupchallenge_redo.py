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
    def __init__(self):
        self.order_list = []

    def open_file(self,input_file):#need to be able to pass in input file here
        with open(input_file,'r') as input_file: #open file as read only
            # note on file structure: it is a LIST, with Dictionary as items that contains: id, name, email, orders dict.
            self.order_list = json.load(input_file) #assign order_list to the newly opnened file: open = json.load(file)
    
    #- get the total number of orders
    def total_order(self): # dont need to pass in new var. use self var above
        total_order = 0
        for order_id in self.order_list:
            total_order +=len(order_id['orders'])
        return print(total_order)

    #- get the person with the most orders 
    '''TBU'''
    '''
    def most_orders(self):
        self.max_orders = 0
        for order_id in self.order_list:
            if len(order_id['orders']) > self.max_orders:
                self.max_orders = len(order_id['orders'])
                
        return print(self.max_orders)
    '''

    #- get the person with the largest total order value
    def most_value(self):
        dollar_order = 0
        person =''
        for order_id in self.order_list:
            for order in order_id['orders']:
                dollar_order += order['price'] #how to covert $val -> numbers?
            order_id['total_order'] = dollar_order
        return print(self.order_list)




    #- ge the most expensive item ordered

    #- get the most frequently ordered item



    

orders1 = OrderManager()

orders1.open_file('orders.json')
orders1.total_order()
#orders1.most_orders()
orders1.most_value()













'''
    def file_reader(self,input_file): #need to be able to pass in input file here
        with open(input_file,'r') as input_file: #open file as read only
            self.order_list = json.load(input_file) #pass new
    
'''


