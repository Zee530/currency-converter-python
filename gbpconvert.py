#convert from gbp using engine

import variables

def gbpconvert():
    from welcome import welcome
    # gbp conversion logic
    if variables.engine == [4, 4]:
        print("You cannot convert to the same currency")
        welcome()
    elif variables.engine == [4, 1]:
        result = variables.amount * 1.26
        print(f"The result of your conversion from {variables.amount} {variables.currencies[3]} to {variables.currencies[0]} is {result: .2f}")
        welcome()
    elif variables.engine == [4, 2]:
        result = variables.amount * 1.20
        print(
            f"The result of your conversion from {variables.amount} {variables.currencies[3]} to {variables.currencies[1]} is {result: .2f}")
        welcome()
    elif variables.engine == [4, 3]:
        result = variables.amount * 191.16
        print(
            f"The result of your conversion from {variables.amount} {variables.currencies[3]} to {variables.currencies[2]} is {result: .2f}")
        welcome()
    elif variables.engine == [4, 5]:
        result = variables.amount * 1906.07
        print(
            f"The result of your conversion from {variables.amount} {variables.currencies[3]} to {variables.currencies[4]} is {result: .2f}")
        welcome()
    else:
        print("You entered a wrong input")
        welcome()