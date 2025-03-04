#welcome message

import variables

def welcome():
    from getInput import getInput
    print("WELCOME TO CURRENCY CONVERSION CENTER")
    print("Convert all your currencies at ease")

    #loop through currency selection list
    for index, currency in enumerate(variables.currencies):
        print(f"{index + 1}. {currency}")

    getInput()