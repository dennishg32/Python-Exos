# Exercise1
hours = float(input("Enter Hours:"))
rate = float(input("Enter the Rate:"))
if hours <= 40:
    print(hours * rate)
elif hours > 40:
    print("Pay:", 40 * rate + (hours-40)*1.5*rate)

# Exercise2
try:
    hours = float(input("Enter Hours:"))
    rate = float(input("Enter the Rate:"))
    if hours <= 40:
        print(hours * rate)
    elif hours > 40:
        print(40 * rate + (hours-40)*1.5*rate)
except:
    print("Error, please enter numeric input")

# Exercise3
count = 1
while (count > 0):
    try:    
        score = float(input("Enter score: "))
        if score > 1.0 or score < 0.0:
            print("Bad Score")
        elif score >= 0.9:
            print('A')
        elif score >= 0.8:
            print('B')
        elif score >= 0.7:
            print('C')
        elif score >= 0.6:
            print('D')
        elif score < 0.6:
            print('F')
    except:
        print("Bad score")
count + 1
