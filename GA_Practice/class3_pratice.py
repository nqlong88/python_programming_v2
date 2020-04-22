# 1. Count negative but even reading. Then sum. build the nubmer list to print the numbers
# 2. Sum all positive number
# 3. check for how many even numbers
# 4. then count letters

#readings = [25, 18, -5, 11, -3, -15, 8, -18, 6, 4 , 'b', 'c', 'd'] -> WHY ERROR W STRING HERE?

readings = [25, 18, -5, 11, -3, -15, 8, -18, 6, 4]

#1
count = 0
total = 0 
count_tally = []
for reading in readings:
    if reading > 0 and reading % 2 == 0: # make sure to use == for equal / and function: needs repeated variable
            count +=1
            count_tally.append(reading) 
    if reading > 0 and reading % 2 == 0:
        total += reading
print (f'the numbers are {count_tally}')
print (f'there are total {count} results with sum total equals to {total}')
print (f'average is {total/count}')
    
#4
'''letter = 0
for reading in readings:
    if reading != "":
        letter += 1
print (f'the number of letters is {letter}')'''


#5. string count:

list_of_snacks = ['hot chocolate', 'dark chocolate', 'milk chocolate', 'candy', 'bubble gum', 'sparkling water','still water']

chocolate = 0
for food_item  in list_of_snacks:
    if 'chocolate' in food_item:
        chocolate += 1
print (f'there are {chocolate} chocolate items')

food_drink = 0

for items in list_of_snacks:
    if 'chocolate' or 'water' in items:
        food_drink += 1
print (f'there are {food_drink} chocolate or water items')
