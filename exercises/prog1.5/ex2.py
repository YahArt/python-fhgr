def calculate_dog_years(human_years):
    # The first two human years are 10.5 dog years each
    if human_years <= 2:
        return human_years * 10.5
    else:
        # The human years are bigger then 2
        return 2 * 10.5 + (human_years - 2) * 4

human_years = int(input("Please enter your human age in years: "))
if human_years < 0:
    print("You certainly do NOT have a negative age I assume or are you perhaps a Time Travelling Wizard...")
else:
    print("Your human years of", human_years, "are the equivalence of", calculate_dog_years(human_years), "dog years")
