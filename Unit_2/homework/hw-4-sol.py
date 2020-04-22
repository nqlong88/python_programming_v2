#generate range of individual

import random

one_to_14 = range(1,15)

fifteen_to_64 = range(15,65)

sixtyfive_over = range(65,100)

population = []

for num in range (1,100): #run for 100 people
    val = random.random()  # create radom between 1.0 - 1.0
    if val >= 0.8: #happens 20% of the time
        #add > 65
        population.append(random.choice(sixtyfive_over))
    elif val >= 0.21:
        #add 14-64
        population.append(random.choice(fifteen_to_64))
    else:
        #add 1-14
        population.append(random.choice(one_to_14))
print(population)


#Questions part: find total number who die
# find over 80
# find 15% of that number
#multiply by sample size
over_80 = 0
for people in population:
    if people >= 80:
        over_80 += 1
        
print (over_80*.15)
        


