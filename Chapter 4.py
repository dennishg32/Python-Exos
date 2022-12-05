# Exercise 4
'What is the purpose of the "def" keyword in Python?'
'''b) It indicates the start of a function'''

# Exercise 5

def fred():
    print("Zap")


def jane():
    print("ABC")

jane()
fred()
jane()

"""
# d)ABC Zap ABC
"""


# Exercise 6
def computepay(hours, rate):
    if hours <= 40:
        return hours * rate
    elif hours > 40:
        return (40 * rate + (hours-40)*1.5*rate)

hours = float(input("Enter Hours:"))
rate = float(input("Enter the Rate:"))

pay = computepay(hours, rate)
print("Pay:",pay)


# Exercise 7


def computegrade(score):
    try:
        if score > 1.0 or score < 0.0:
            return "Bad Score"
        elif score > 0.9:
            return "A"
        elif score > 0.8:
            return "B"
        elif score > 0.7:
            return "C"
        elif score > 0.6:
            return "D"
        elif score <= 0.6:
            return "F"
    except:
        return "Bad score"


score = computegrade(float(input("Enter score: ")))
print(score)
