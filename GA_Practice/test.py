# find max
list_item = [4,5,6,1,2,3]
max = 0

for item in list_item:
    if item > max:
        max = item
print(f'the max is {max}')

# rearrange list:
''''
new_list =[]
min = 10000
index = 0

list_item = [6,1,2]


while index <= len(list_item)-1:
    if list_item[index] < min:
        min = list_item[index]
    new_list.append(min)
    index += 1

print (f'new list is {new_list}')
print (f'min is: {min}')  
'''

a=[12,0,39,50,1]
i=0
while i<len(a):
    key=i
    j=i+1
    while j<len(a):
        if a[key]>a[j]: # if previous no. larger that next
            key=j # previous number becomes next: putting larger number behind ; i+1
        j+=1 # check for all numbers
    a[i],a[key]= a[key],a[i] # i and key are the same
    i+=1
print(a)