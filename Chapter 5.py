# Exercise 1

count = 0
total = 0
while True:
    num = input("Enter a number: ")
    if num == 'done':
        break
    try:
        num1 = float(num)
    except:
        print('Invalid input')
        continue
    count = count+1
    total = total + num1
print('done')
print(total, count, total/count)


# Exercise 2
count = 0
total = 0
max = None
min = None

while True:
    num = input("Enter a number: ")
    if num == 'done':
        break
    try:
        num1 = int(num)
    except:
        print('Invalid input')
        continue
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
print(total, count, max, min)
