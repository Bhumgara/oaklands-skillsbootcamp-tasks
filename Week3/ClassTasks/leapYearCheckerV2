yearInput = input("Input a year including BCE or CE: ")
yearInput = yearInput.replace(" ", "")

yearNumber = ''.join(ch for ch in yearInput if ch.isdigit())
if (yearInput.lower().__contains__("b")):
    yearEra = "BCE"
else:
    yearEra = "CE"

if(not yearNumber.isnumeric()):
    exit()
else:
    yearNumber = int(yearNumber)
    
if(yearNumber % 4 == 0 and yearEra == "CE") or ((yearNumber-1) % 4 == 0 and yearEra == "BCE" and yearNumber <= 45):
    print(f"{yearNumber} {yearEra} is a leap year!")
else:
    print(f"{yearNumber} {yearEra} is not a leap year!")