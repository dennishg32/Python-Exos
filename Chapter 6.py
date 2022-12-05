
#Exercise 5
str = 'X-DSPAM-Confidence: 0.8475'

colonChar = str.find(':')
ExtractNumber = str[colonChar + 1:]
convertNum = float(ExtractNumber)
print(convertNum)

#Exercise 6
#https://docs.python.org/3.5/library/stdtypes.html#string-methods