import random
import string

while True:
    length=int(input("Enter your password:"))
    #create character set
    upper_case=string.ascii_uppercase
    lower_case=string.ascii_lowercase
    letter=string.ascii_letters
    digit=string.digits
    symbol=string.punctuation

    #combine all character
    character=upper_case+lower_case+letter+digit+symbol

    #generate randon character
    password=" "

    #stor to password
    for val in range(length):
        password+=random.choice(character)
        print(password)

    # change the password
    n= input("change your password (yes/no):").lower()
    if n=="yes":
        password=" "
        for val in range(length):
            password+=random.choice(character)
            print(password)
            continue
    elif n=="no":
        print("Thank your for visiting")
        break

