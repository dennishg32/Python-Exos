# Exercise 1

doc = open(input("Enter a file name: "))
for line in doc:                 
    shout = line.rstrip().upper()       
    print(shout)
    

# Exercise 2
total = 0
count = 0

docfile = input('Enter the file name: ')
try:
    doc = open(docfile)
except FileNotFoundError:
    print('File cant be opened: ', docfile)
    quit()

for line in doc:
    if line.startswith('X-DSPAM-Confidence: '):
        count = count + 1
        colonChar = line.find(':')
        ExtractNumber = line[colonChar + 1:].strip()
        SPAM_C = float(ExtractNumber)
        total = total + SPAM_C

average = total / count
print('Average spam confidence: ', average)

# Exercise
file = input('Enter the file name: ')
try:
    if file == 'na na boo boo':
        print('NA NA BOO BOO TO YOU - You have been punk\'d!')
        exit()
    doc = open(file)
except FileNotFoundError:
    print('File cant be opened:', file)
    exit()
count = 0
for line in doc:
    if line.startswith('Subject:'):
        count += 1
print('There were', count, 'subject lines in', file)
