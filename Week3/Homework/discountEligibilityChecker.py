totalAmount = int(input("What is the total amount? "))
member = input("Are you a member? [Y/N] ").lower()

if member.__contains__("y"):
    memberBool = True
elif member.__contains__("n"):
    memberBool = False
else:
    print("Please input Y or N.")
    exit()

if totalAmount > 100 and memberBool:
    print(f"You have a discount of 15%, your total is now {totalAmount*0.85}.")
elif totalAmount > 100 and not memberBool:
    print(f"You have a discount of 10%, your total is now {totalAmount*0.90}.")
else:
    print(f"You are not eligible for a discount, your total is {totalAmount}.")
