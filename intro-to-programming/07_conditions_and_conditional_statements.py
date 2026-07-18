# Conditions and Conditional Statements

# conditions are statements that are either True or False
print(2>3)
# False

var_1 = 1
var_2 = 2
print(var_1<1)
print(var_2>=var_1)
# False
# True

# condition's common symbols
# Symbol	Meaning
# ==	equals
# !=	does not equal
# <	less than
# <=	less than or equal to
# >	greater than
# >=	greater than or equal to

# = is assignment equals
# == is comparison equals

# conditional statements
# use condititons to modify how your function runs.
# if condition is True, will execute one block of code, if False, then dont execute block of code
# more examples will come 

# "if" statements
# simplest
def evaluate_temp(temp):
    message = "Normal Temperature." # indentation for func
    if temp> 38:# indentation for func
        message = "Fever !!!" # indentation for if statement
    return message# indentation for func# outside if statement
print(evaluate_temp(37))
print(evaluate_temp(39))
# Normal Temperature.
# Fever !!!

# "if...else" statement
# block of code under else statement runs if "if" condition turns out to be false
def evaluate_temp_with_else(temp):
    if temp > 38:
        message = "Fever!"
    else:
        message = "Normal temperature."
    return message
print(evaluate_temp_with_else(37))
print(evaluate_temp_with_else(39))
# Normal temperature.
# Fever!

# "if...elif...else" statements
# elif is short of else if
# for multiple conditions
def evaluate_temp_with_elif(temp):
    if temp > 38:
        message = "Fever!"
    elif temp > 35:
        message = "Normal temperature."
    else:
        message = "Low temperature."
    return message
print(evaluate_temp_with_elif(36))
# Normal temperature.
print(evaluate_temp_with_elif(34))
# Low temperature.

# example
def get_taxes(earnings):
    if earnings < 12000:
        tax_owed = .25 * earnings
    else:
        tax_owed = .30 * earnings
    return tax_owed
ana_taxes = get_taxes(9000)
bob_taxes = get_taxes(15000)

print(ana_taxes)
print(bob_taxes)
# 2250.0
# 4500.0

def get_dose(weight):
    # Note: This function should not be used as medical advice, and represents a fake medication.
    # Dosage is 1.25 ml for anyone under 5.2 kg
    if weight < 5.2:
        dose = 1.25
    elif weight < 7.9:
        dose = 2.5
    elif weight < 10.4:
        dose = 3.75
    elif weight < 15.9:
        dose = 5
    elif weight < 21.2:
        dose = 7.5
    # Dosage is 10 ml for anyone 21.2 kg or over
    else:
        dose = 10
    return dose
print(get_dose(12))
# 5

# The order of the elif statements does matter here! Re-ordering the statements will return a very different result.

def add_three_or_eight(number):
    if number < 10:
        result = number + 3
    else:
        result = number + 8
    return result
print(add_three_or_eight(5))
print(add_three_or_eight(15))
# 8
# 23