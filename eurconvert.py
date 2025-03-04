import variables

def eurconvert():
    from welcome import welcome
    # eur conversion logic
    if variables.engine == [2, 2]:
        print("You cannot convert to the same currency")
        welcome()
    elif variables.engine == [2, 1]:
        result = variables.amount * 1.05
        print(
            f"The result of your conversion from {variables.amount} {variables.currencies[1]} to {variables.currencies[0]} is {result: .2f}")
        welcome()
    elif variables.engine == [2, 3]:
        result = variables.amount * 158.71
        print(
            f"The result of your conversion from {variables.amount} {variables.currencies[1]} to {variables.currencies[2]} is {result: .2f}")
        welcome()
    elif variables.engine == [2, 4]:
        result = variables.amount * 0.83
        print(
            f"The result of your conversion from {variables.amount} {variables.currencies[1]} to {variables.currencies[3]} is {result: .2f}")
        welcome()
    elif variables.engine == [2, 5]:
        result = variables.amount * 1582.18
        print(
            f"The result of your conversion from {variables.amount} {variables.currencies[1]} to {variables.currencies[4]} is {result: .2f}")
        welcome()
    else:
        print("You entered a wrong input")
        welcome()