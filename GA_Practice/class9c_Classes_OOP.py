#Practice Sets/Tuples:

#1 using sets to remove duplicates in list:

list_name = [ 1,2,3,4,1,2]

non_dupe = set(list_name)
print(non_dupe) #should return {1,2,3,4}


#2 set:

set_sample = {1,2,3}
print(set_sample)



#Create class:

#create rectangle:

class Rectangle:
    def __init__(self, size): #needs to set all properties w self below
        self.l = size['l']
        self.w = size['w']

    def area(self):
        return self.l*self.w

r1 = Rectangle({'l':3,'w':4})

print(f'testing retangle class: {r1.area()}')


#create a CAPM class:

class CAPM:
    def __init__(self,rf,beta,mrp): #var(outside self): are variables to pass into method
        self.rf = rf #these self.var -> assigned to where that goes above: self.rf -> feeds rf
        self.beta = beta
        self.mrp = mrp
    
    def cost_of_equity(self):
        return self.rf + self.beta*self.mrp

    def sharpe_ratio(self,volatility):
        self.vol = volatility
        self.sharpe = (self.rf + self.beta*self.mrp)/self.vol
        return f'sharpe ratio is: {self.sharpe}'


stock1 = CAPM(2.5,1,5) # this is an OBJECT (one of many in CLASS CAPM)

print(f'expected return is: {stock1.cost_of_equity()}%')
print(stock1.sharpe_ratio(5))
    
#EXAMPLE create a stock portfolio  class: using dictionary input
'''
1. Initiate a portfolio
2. allow stock to be added to portfolio: dict(w,beta,stdev)
    stock = {'w': val, 'beta':val, 'stdev':val}
    Check total weight must be 1
    Find port return
    Find port vol.
3. calculate risk-adjusted return
'''

import json

class Portfolio:
    #1 initiate portfolio
    def __init__(self,portfolio_name): #initiate a portfolio
        self.name = portfolio_name
        self.positions = []
        print(self.name) # To print out portfolio's name
    #add stocks to portfolio
    def add_position(self,stock): # need stock here to pass in 
        #self.stock = stock
        self.port_weight = 0   #USE SELF HERE BECAUSE IT WILL NEEDED in def weight_check below:
        #pick a new stock
        if type(stock) is dict and stock['w'] != 0 and stock['beta'] != 0 and stock['stdev'] !=0:
            self.positions.append(stock)
            return print(self.positions)
        else:
            print('check stock input. please use dictionary: w: , beta: , stdev:')
    #check portfolio weight:   
    def weight_check(self):
        self.valid = True     #use BOOLEAN to simplify /self.: to use in return_analysis below
        for position in self.positions:
            self.port_weight += position['w']
        if self.port_weight > 1:
            self.valid = False    
        if self.valid:
            return print(f'weight is OK at: {self.port_weight*100}%')
        else:
            return print ('CHECK WEIGHT')

    #def return_analysis(self):
    def return_analysis(self):
        self.mrp = 5 #in case needed to be used somewhere
        self.rf = 2.5
        self.port_metrics = {}
        port_return = 0
        port_risk = 0
        sharpe_ratio = 0
        for position in self.positions:
            port_return += position['w']*(self.rf + position['beta']*self.mrp)
            port_risk += position['w']*position['stdev']
        sharpe_ratio = port_return/port_risk
        self.port_metrics['return'] = port_return
        self.port_metrics['risk'] = port_risk
        self.port_metrics['sharpe'] = sharpe_ratio
        if self.valid:
            return print(self.port_metrics)
        else:
            return print('Reconfigure port weight!')

             
#Implementation: Add portfolio 1        
p1 = Portfolio('All Weather')
p1.add_position({'w':0.3, 'beta':1.0, 'stdev':6}) # the way code written input has to be dictionary
p1.add_position({'w':0.5, 'beta':1.2, 'stdev':7})
p1.add_position({'w':0.1, 'beta':1.5, 'stdev':12})
p1.weight_check()
p1.return_analysis()

p2 = Portfolio('Risk Parity')
p2.add_position({'w':0.4, 'beta':-1.4, 'stdev':1}) # the way code written input has to be dictionary
p2.add_position({'w':0.5, 'beta':1.2, 'stdev':8})
p2.add_position({'w':0.1, 'beta':1.5, 'stdev':12})
p2.weight_check()
p2.return_analysis()

        