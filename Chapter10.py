# Exercise1
dictionary_addresses = dict()           
li = list()

try:
    file = open(input("Enter a file name: "))
except FileNotFoundError:
    print('File cannot be opened:', file)
    quit()

for line in file:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    else:
        if words[1] not in dictionary_addresses:
            dictionary_addresses[words[1]] = 1       
        else:
            dictionary_addresses[words[1]] += 1      

for key, val in list(dictionary_addresses.items()):
    li.append((val, key))              

li.sort(reverse=True)                  

for count, email in li[:1]:            
    print(email, count)


# Exercise 2
dictionary_hours = dict()
my_list = list()

try:
    file = open(input("Enter a file name: "))
except FileNotFoundError:
    print('File cannot be opened:', file)
    quit()

for line in file:
    words = line.split()
    if len(words) < 5 or words[0] != 'From':
        continue

    colon_char = words[5].find(':')
    hour = words[5][:colon_char]
    if hour not in dictionary_hours:
        dictionary_hours[hour] = 1
    else:
        dictionary_hours[hour] += 1

for key, val in list(dictionary_hours.items()):
    my_list.append((key, val))

my_list.sort()

for key, val in my_list:
    print(key, val)
    

#Exercise 3
import string

counts = 0                          
dict_counts = dict()
rel_list = list()

try:
    file = open(input("Enter a file name: "))
except FileNotFoundError:
    print('File cannot be opened:', file)
    exit()

for line in file:
    line = line.translate(str.maketrans('', '', string.digits))
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()

    
    words = line.split()
    for word in words:
        for letter in word:
            counts += 1
            if letter not in dict_counts:
                dict_counts[letter] = 1
            else:
                dict_counts[letter] += 1

for key, val in list(dict_counts.items()):
    rel_list.append((val / counts, key)) 

rel_list.sort(reverse=True)         

for key, val in rel_list:
    print(key, val)