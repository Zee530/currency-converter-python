import variables

def ngnconvert():
    from welcome import welcome
    # ngn conversion logic
    if variables.engine == [5, 5]:
        print("You cannot convert to the same currency")
        welcome()
    elif variables.engine == [5, 1]:
        result = variables.amount * 0.00066
        print(
            f"The result of your conversion from {variables.amount} {variables.currencies[4]} to {variables.currencies[0]} is {result: .2f}")
        welcome()
    elif variables.engine == [5, 2]:
        result = variables.amount * 0.00063
        print(
            f"The result of your conversion from {variables.amount} {variables.currencies[4]} to {variables.currencies[1]} is {result: .2f}")
        welcome()
    elif variables.engine == [5, 3]:
        result = variables.amount * 0.10
        print(
            f"The result of your conversion from {variables.amount} {variables.currencies[4]} to {variables.currencies[2]} is {result: .2f}")
        welcome()
    elif variables.engine == [5, 4]:
        result = variables.amount * 0.00052
        print(
            f"The result of your conversion from {variables.amount} {variables.currencies[4]} to {variables.currencies[3]} is {result: .2f}")
        welcome()
    else:
        print("You entered a wrong input")
        welcome()