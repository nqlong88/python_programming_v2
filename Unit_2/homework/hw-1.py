# Problem 1

#print numbers between [1,500, 20,000] divisable by 7 and multiple of 5

numbers = []

for number in range(1500,20000):
    if number % 7 == 0 and number % 5 == 0:
        numbers.append(number)
print(numbers, end='')


# Problem 2

