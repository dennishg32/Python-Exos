# Exercise 2

dictionary_days = dict()
try:
    file = open(input("Enter a file name: "))
except FileNotFoundError:
    print('File cannot be opened:', file)
    exit()

for line in file:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    else:
        if words[2] not in dictionary_days:
            dictionary_days[words[2]] = 1
        else:
            dictionary_days[words[2]] += 1

print(dictionary_days)

# Exercise 4
dictionary_days = dict()
max = 0
max_address = ''
try:
    file = open(input("Enter a file name: "))
except FileNotFoundError:
    print('File cannot be opened:', file)
    exit()

for line in file:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    if words[1] not in dictionary_days:
        dictionary_days[words[1]] = 1
    else:
        dictionary_days[words[1]] += 1

for address in dictionary_days:
    if dictionary_days[address] > max:
        max = dictionary_days[address]
        max_address = address
print(max_address, max)

# Exercises 5

file_name = input("Enter a file name: ")
lines = [line.strip('\n') for line in open(file_name, 'r')
         if line.startswith("From ")]
who_dict = {}

for line in lines:
    line = line.split()
    email = line[1]
    domain = email.split("@")[1]
    who_dict[domain] = who_dict.get(domain, 0) + 1

print(who_dict)

# Exercises 3
dictionary_addresses = dict()
try:
    file = open(input("Enter a file name: "))
except FileNotFoundError:
    print('File cannot be opened:', file)
    exit()

for line in file:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    else:
        if words[1] not in dictionary_addresses:
            dictionary_addresses[words[1]] = 1
        else:
            dictionary_addresses[words[1]] += 1

print(dictionary_addresses)
