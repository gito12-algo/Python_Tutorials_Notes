calculate_to_unit = 24
name_of_unit = "hours"

def days_to_units(num_of_days, custom_message):
    print(f"{num_of_days} days are {num_of_days* calculate_to_unit} {name_of_unit}")
    print(custom_message)

days_to_units(20, "Awesome!")
days_to_units(45,"looks good")