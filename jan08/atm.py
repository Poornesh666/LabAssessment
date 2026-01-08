balance = int(input("Enter your balance: "))
withdraw = int(input("Enter amount to withdraw: "))
if withdraw > balance:
    print("Insufficient funds")
else:
    if withdraw % 100 != 0:
        print("Not a multiple of 100")
    else:
        print(f"Remaining balance: {balance-withdraw}")