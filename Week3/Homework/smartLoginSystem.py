mainUsername = "admin"
mainPassword = "1234"
loggedOut = True
tries = 0
failedEntryPhrase = "Incorrect username or password."

while loggedOut:
    if tries >= 3:
        print("You're locked out.")
        exit()
    print(f"You've tried {tries} times, {3 - tries} remaining.")
    givenUser = input("Username: ")
    givenPassw = input("Password: ")
    tries += 1

    if givenPassw != mainPassword or givenUser != mainUsername:
        print(failedEntryPhrase)
        continue
    else:
        print("Well done, you're now logged in.")
        loggedOut = False