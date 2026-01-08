units = int(input("Enter number of units consumed: "))
bill = 0

for i in range(units+1):
    if i<=100:
        bill += 2*i
    elif i>100 & i<=200:
        bill += 3*i
    else:
        bill += 5*i
        
print(f"Total bill: {bill}")