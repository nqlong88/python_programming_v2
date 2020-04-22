#bonus problem: 190,000 individuals. 1-14: 20% / 15-64: 60% / >65: 20%

#Create a list age distribution
individual_ages =[ ]
population = 290000
import random

for individual in range (0,population):
    if individual < population*.20:
        age = random.randint(1,14)
        individual_ages.append(age)
    elif individual > population*.2 and individual <= population*.8: 
        age = random.randint(15,64)
        individual_ages.append(age)
    else: 
        age = random.randint(65,105)
        individual_ages.append(age)
print('begin')
print (individual_ages, end='')
print(f' -> there are {len(individual_ages)} people in the sample ')

# problem: people > 65
count_oldage = 0
for age in individual_ages:
    if age >= 65:
        count_oldage +=1
print(f'-> There are {count_oldage} people >= 65')

# problem: people < 15
count_15 = 0
for age in individual_ages:
    if age < 15:
        count_15 +=1
print(f'-> There are {count_15} people < 15')

# average age
average_age = sum(individual_ages)/len(individual_ages)
print(f'-> The average age is {average_age}')

# how many people likely to die: 15% for those > 80

count_80 = 0
mortality = 0
for age in individual_ages:
    if age >= 80:
        count_80 +=1
        mortality = int(count_80*.15)

print (f'-> There are {count_80} people at the age 80 and above. at 15% mort rate  expected mortality is {mortality}')


#DONT FOR GET TO SCALE SAMPLE SIZE UP