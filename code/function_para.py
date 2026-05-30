# information can be passed into function as parameters
# Parameters are also called arguments

calculate_to_unit = 24
name_of_unit = "hours"

def days_to_units(num_of_days):
    print(f"{num_of_days} days are {num_of_days* calculate_to_unit} {name_of_unit}")

days_to_units(20)
days_to_units(35)
days_to_units(50)
days_to_units(110)