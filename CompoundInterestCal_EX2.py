principle =0
rate=0
time=0

while principle <=0:
    principle= float(input("Enter your princile: "))
    if principle <=0:
        print("princile can't be equal or less then zero")

while rate <=0:
    rate= float(input("Enter your rate: "))
    if rate <=0:
        print("rate can't be equal or less then zero")

while time <=0:
    time= int(input("Enter your time: "))
    if time <=0:
        print("time can't be equal or less then zero")

total = principle * pow((1+ rate/100),time)

print(f"Balance after{time} years: {total:.2f}")