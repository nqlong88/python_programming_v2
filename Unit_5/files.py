#read a file:
text_file = open('lines.txt' , 'r') #mode r = read

lines = text_file.read()
text_file.close()

print(lines)


#write to file:
text_file = open('lines.txt', 'w') #mode w = wite -> w: overwrites

text_file.write('Here is a 2nd line') # this will overwrite the existing content
text_file.close()


#write to file:
text_file = open('lines.txt', 'a') #a: append

text_file.write('\nHere is a 3rd line') #\n: adds new line
text_file.close()


