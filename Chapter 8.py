#Exercise4 
file = open(input("Enter a file name: "))
li = list()
for line in file:
    word = line.rstrip().split()
    for element in word:
        if element in li:
            continue
        else:
            li.append(element)
li.sort()
print(li)

# Exercises5
doc = open(input("Enter a file name: "))
count = 0
for line in doc:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    print(words[1])
    count += 1
print('There were %d lines in the file with From as the first word' % count)

# Exercises6

max = None
min = None
my_list = []

while True:
    num = input("Enter a number: ")
    if num == 'done':
        break
    try:
        num1 = float(num)
    except:
        print('Invalid input')
        quit()
    my_list.append(num)
    count = count+1
    total = total + num1
    if max == None and min == None:
        max = num1
        min = num1
    if max == None or num1 > max:
        max = num1
    if min == None or num1 < min:
        min = num1
print('done')
print("Maximum: ", max)
print("Minimum: ", min)
