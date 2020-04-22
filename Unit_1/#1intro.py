#print hello world
print('hello world')
#Terminal, round = not saved ' x = saved (hit ctrl + s)

#create variables to store first and last name
first_name = 'Long'
last_name = 'Nguyen'
age = 32

#strong concaternation: to join strings together
full_name = first_name + ' ' + last_name

print(first_name)
print(full_name)

#use ''' and ''' to create comments for segment
'''
#use format string to print 
#print('hello, my name is' + full_name + 'and i am' + age + 'years old')
#str() can covert age from integer to string
#Solution:use f to create format string use { } here specifically
'''

print(f'My name is {full_name} and i am {age} years old')

'''
create variables to store the names of all your classmates
print all the names in the following message
The members of my cohort are: ....and they are awesome
'''

#long way using f function to join strings
Member_1 = 'Justin'
Member_2 = 'Griffin'
Member_3 = 'Princeton'

print(f'The members of my cohort are: {Member_1}, {Member_2}, {Member_3} and they are awesome')

Member_list = ['Justin','Griffin', 'Princeton']
print(f'The members of my cohort are: {Member_list} and they are awesome')

#Will figure this out next class