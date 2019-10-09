def numunits(carbs, perunit, number, startscale, rnge):
    units = round(carbs / perunit, 2)
    print("You should give " + str(units) + " for the food.")
    if number >= startscale:
        exunits = (number - (startscale - rnge)) / (rnge / .5)
        print("You should give an extra " + str(exunits) + " units for the food.")
    else:
        print("Your number is great! You need to give no extra units!")


def intro():
    data = {}
    while True:
        try:
            data["Breakfast"] = int(input("For every ___ carbs at breakfast, I give 1 unit." +
                                          "(Answer with a whole number): ").strip())
            break
        except ValueError:
            print("I'm sorry, that is not an accepted input, please try again.\n")
    while True:
        try:
            data["Lunch"] = int(input("For every ___ carbs at lunch, I give 1 unit.Answer with a whole number): ")
                                .strip())
            break
        except ValueError:
            print("I'm sorry, that is not an accepted input, please try again.\n")
    while True:
        try:
            data["Dinner"] = int(input("For every ___ carbs at dinner, I give 1 unit." +
                                       "(Answer with a whole number): ").strip())
            break
        except ValueError:
            print("I'm sorry, that is not an accepted input, please try again.\n")
    while True:
        try:
            data["startScale"] = int(input("At what blood glucose does your sliding scale begin: ").strip())
            break
        except ValueError:
            print("I'm sorry, that is not an accepted input, please try again.\n")
    while True:
        try:
            data["rnge"] = int(input("For every ___ points above the start of my sliding scale, I increase my dosage."
                                     "(Answer with a whole number): ").strip())
            break
        except ValueError:
            print("I'm sorry, that is not an accepted input, please try again.\n")
    return data


def getcarbs():
    while True:
        try:
            carbs = int(input("How many carbs are in your meal: ").strip())
            break
        except ValueError:
            print("That was not an accepted input, please try again.")
    return carbs


def getnum():
    while True:
        try:
            number = int(input("What is your current blood glucose: ").strip())
            break
        except ValueError:
            print("That was not an accepted input, please try again.")
    return number
