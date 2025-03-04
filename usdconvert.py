#convert from usd using engine

import variables

def usdconvert():
    from welcome import welcome
    if variables.engine == [1, 1]:
        #deny same currency selection
        print("You cannot convert to the same currency")
        welcome()
    elif variables.engine == [1, 2]:
        result = variables.amount * 0.95
        print(f"The result of your conversion from {variables.amount} {variables.currencies[0]} to {variables.currencies[1]} is {result: .2f}")
        welcome()
    elif variables.engine == [1, 3]:
        result = variables.amount * 152.33
        print(f"The result of your conversion from {variables.amount} {variables.currencies[0]} to {variables.currencies[2]} is {result: .2f}")
        welcome()
    elif variables.engine == [1, 4]:
        result = variables.amount * 0.79
        print(f"The result of your conversion from {variables.amount} {variables.currencies[0]} to {variables.currencies[3]} is {result: .2f}")
        welcome()
    elif variables.engine == [1, 5]:
        result = variables.amount * 780
        print(f"The result of your conversion from {variables.amount} {variables.currencies[0]} to {variables.currencies[4]} is {result: .2f}")
        welcome()
    else:
        print("You entered a wrong input")
        welcome()