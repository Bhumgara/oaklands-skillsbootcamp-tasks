userInput = input("Input a number: ")

if(not userInput.isnumeric()):
    if(userInput.__contains__("-")):
        if(not userInput.replace("-", "", 1).isnumeric()):
            print("Please input a number.")
            exit()
    else:
        print("Please input a number.")
        exit()

userInput = int(userInput)

if(userInput%2 == 0):
    print(f"{userInput} is an even number!")
else:
    print(f"{userInput} is an odd number!")