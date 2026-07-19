# Python is famous for Data Science and Machine Learning. 
# super simple

# printing a simple message
print("Hello, world!") 
# goldern-sword@Siddhants-MacBook-Air kaggle-course-intro-to-programming % python3 -u "/Users/goldern-sword/git/personal/kaggle-course-intro-to-programming/arithmetic_and_variables.py" Hello, world!

# code inside box is called code cell
# computer response is called output of code
# terminal is CLI based communication with computer brain

# arithmetics
print(1+2)
print(9-5)
print(2*3)
print(10/5)
print(2**3)
# 3
# 4
# 6
# 2.0
# 8

# python follow PEMDAS Rule
# Parentheses > Exponents(power/roots) > Multiply & Divide(left to right) > Add & Subtract(left to right)
print(((1+3)*(9-2)/2)**2)
# 196.0

# comments
# usefull annotations/notes
'''
help devs 
to understand code
better
'''
# single line
'''
m 
u
l
t
i

l
i
n
e
'''
# print(((1+3)*(9-2)/2)**2) # also helps to soft delete code

# variables
# store data temporary, when same file run, not persistent storage
test_var = 4+5 # var init/declaration & assignment
# 9
print(test_var)
# 9
'''
manners:
- no spaces(no test var)
- only letters,numbers,underscores(no test!var)
- only start with underscore or letter(no 1_test)
'''

# variables manipulation
my_var = 3 # set value
print(my_var) # print value/lookup
my_var =1 # change value
print(my_var) # print new value
print(test_var) # at next cell block you can use previous cell block stuff
my_var = my_var*test_var
print(my_var) 
# 9

# multiple vars
# for long cal, convinience, readablility, developer experience(dx)
num_years = 4 
days_per_year = 365
hours_per_day = 24
mins_per_hour = 60
secs_per_min = 60
total_secs = secs_per_min * mins_per_hour * hours_per_day * days_per_year * num_years
print(total_secs)
# 126144000
# total_secs = 60 * 60 * 24 * 365 * 4 # far more tedious
# also helps easily when updating value
days_per_year = 365.5
total_secs = secs_per_min * mins_per_hour * hours_per_day * days_per_year * num_years
print(total_secs)
# 126316800.0

# debugging
# common error, typos
# print(hours_per_da)
# Traceback (most recent call last):
#   File "/Users/goldern-sword/git/personal/kaggle-course-intro-to-programming/01_arithmetic_and_variables.py", line 93, in <module>
#     print(hours_per_da)
#           ^^^^^^^^^^^^
# NameError: name 'hours_per_da' is not defined. Did you mean: 'hours_per_day'?
# goldern-sword@Siddhants-MacBook-Air kaggle-course-intro-to-programming % 
print(hours_per_day) #24