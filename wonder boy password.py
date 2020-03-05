#create a varriable in order to store Wonder Boy's password

password = ''
passwordAttempt = 0
print("Welcome to Oprimal Dad's vault of gadgets!")

while password != "wonderboyiscool2020":
    print("Please enter your password in order to access some fun tech!")
    password = input()
    password = password.lower()
    passwordAttempt = passwordAttempt + 1

    if password == "wonderboyiscool2020":
        print("you entered the correct password!")
        print("take whatever you need!")
    elif passwordAttempt == 3:
        print("sorry bud, you're out of attempts")
        break
