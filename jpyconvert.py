import variables

def jpyconvert():
    from welcome import welcome
    # jpy conversion logic
    if variables.engine == [3, 3]:
        print("You cannot convert to the same currency")
        welcome()
    elif variables.engine == [3, 1]:
        result = variables.amount * 0.0066
        print(
            f"The result of your conversion from {variables.amount} {variables.currencies[2]} to {variables.currencies[0]} is {result: .2f}")
        welcome()
    elif variables.engine == [3, 2]:
        result = variables.amount * 0.0063
        print(
            f"The result of your conversion from {variables.amount} {variables.currencies[2]} to {variables.currencies[1]} is {result: .2f}")
        welcome()
    elif variables.engine == [3, 4]:
        result = variables.amount * 0.0052
        print(
            f"The result of your conversion from {variables.amount} {variables.currencies[2]} to {variables.currencies[3]} is {result: .2f}")
        welcome()
    elif variables.engine == [3, 5]:
        result = variables.amount * 9.97
        print(
            f"The result of your conversion from {variables.amount} {variables.currencies[2]} to {variables.currencies[4]} is {result: .2f}")
        welcome()
    else:
        print("You entered a wrong input")
        welcome()