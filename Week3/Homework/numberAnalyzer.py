userInput = input("Input a number: ")
positiveOrNegative = "Positive"
evenOrOdd = ""
betweenTenAndFifty = False

if(not userInput.isnumeric()):
    if(userInput.__contains__("-")):
        if(not userInput.replace("-", "", 1).isnumeric()):
            print("Please input a number.")
            exit()
        positiveOrNegative = "Negative"
    else:
        print("Please input a number.")
        exit()

userInput = int(userInput)

if(userInput%2 == 0):
    evenOrOdd = "Even"
else:
    evenOrOdd = "Odd"

if(userInput > 10 and userInput < 50):
    betweenTenAndFifty = True

print(f"The number {userInput} is an {positiveOrNegative.lower()} {evenOrOdd.lower()} number that is {"between 10 and 50" if betweenTenAndFifty else "outside the range of 10 and 50"}.")