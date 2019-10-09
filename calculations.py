def numunits(carbs, perunit, number, startscale, rnge):
    # Base food units, no high
    units = round(carbs / perunit, 2)
    print("You should give " + str(units) + " for the food.")

    # Extra units for the high
    if number >= startscale:
        exunits = (number - (startscale - rnge)) / (rnge / .5)
        print("You should give an extra " + str(exunits) + " units for the food.")
        print("You should give a total of " + str(units + exunits) + " units")
    else:
        print("Your number is great! You need to give no extra units!")

    # Finishing
    input("\nPress enter when finished . . . ")


def intro():
    data = {}
    # Ugly code to keep attempting to get the correct input per meal
    while True:
        # carbs:unit at breakfast
        try:
            data["Breakfast"] = int(input("For every ___ carbs at breakfast, I give 1 unit." +
                                          "(Answer with a whole number): ").strip())
            break
        except ValueError:
            print("I'm sorry, that is not an accepted input, please try again.\n")
    while True:
        # carbs:unit at lunch
        try:
            data["Lunch"] = int(input("For every ___ carbs at lunch, I give 1 unit.Answer with a whole number): ")
                                .strip())
            break
        except ValueError:
            print("I'm sorry, that is not an accepted input, please try again.\n")
    while True:
        # carbs:unit at dinner
        try:
            data["Dinner"] = int(input("For every ___ carbs at dinner, I give 1 unit." +
                                       "(Answer with a whole number): ").strip())
            break
        except ValueError:
            print("I'm sorry, that is not an accepted input, please try again.\n")
    while True:
        # Bg for start of sliding scale
        try:
            data["startScale"] = int(input("At what blood glucose does your sliding scale begin: ").strip())
            break
        except ValueError:
            print("I'm sorry, that is not an accepted input, please try again.\n")
    while True:
        # Range for sliding scale
        try:
            data["rnge"] = int(input("For every ___ points above the start of my sliding scale, I increase my dosage."
                                     "(Answer with a whole number): ").strip())
            break
        except ValueError:
            print("I'm sorry, that is not an accepted input, please try again.\n")
    return data


def getcarbs():
    # Loop simply so its not in the main. Keeps trying to get carbs until number is input
    while True:
        try:
            carbs = int(input("How many carbs are in your meal: ").strip())
            break
        except ValueError:
            print("That was not an accepted input, please try again.")
    return carbs


def getnum():
    # Loop simply so its not in the main. Keeps trying to get BG until number is input
    while True:
        try:
            number = int(input("What is your current blood glucose: ").strip())
            break
        except ValueError:
            print("That was not an accepted input, please try again.")
    return number
