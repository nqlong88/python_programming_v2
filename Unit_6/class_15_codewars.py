'''
def digital_root(n):
    sum = 0
    test = int(str(n)[::])
    for item in str(n):
        sum += int(item)
        test = sum
    while len(str(test))>1:
        for char in str(test):
            sum += int(char)
            test = sum
    return sum

print(digital_root(456))
'''
def digital_root(n):
    test = int(str(n)[::]) 
    while len(str(test)) > 1:
        total = 0
        print(test)
        for item in str(test):
            total += int(item)
            test = total
    return test



print(digital_root(456))