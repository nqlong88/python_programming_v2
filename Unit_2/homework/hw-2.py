#problem 2:
# Fulltime: 40hrs/wk $50/h $60/h_OT
# Partime: 20hrs/wk $65/h $75/h_OT
# Contract: $120/h 25% tax

worker_types = ['full_time' , 'part_time' , 'contract']

hours = input ('please enter hours worked:')
worker_type = input (f'please select worker type: {worker_types}')

print (f'the worker is: {worker_type} and worked {hours} hours')

if worker_type == 'full_time':
    if int(hours) <= 40:
        weekly_wage = int(hours)*50
    else:
        weekly_wages = 40*50 + (int(hours)-40)*60
elif worker_type == 'part_time':
    if int(hours) <= 20:
        weekly_wage = int(hours)*65
    else:
        weekly_wages = 20*65 + (int(hours)-20)*75
else:
    weekly_wages = int(hours)*120*(1-.25)
        
print(f'the weekly wage amount is {weekly_wages}')