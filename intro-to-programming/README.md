# intro-to-programming

![certifications/Siddhant Bali - Intro to Programming.png](<../certifications/Siddhant Bali - Intro to Programming.png>)

## intro-to-programming/01-arithmetic-and-variables.py

```py
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
```

## intro-to-programming/03-functions.py

```py
# functions
'''
function is block of code designed to perform a perform a specific task
reduce redundancy, way faster and good than writing same code at multiple times
avoid mistakes
more smart coding
saves time
smart modification 
'''

# simple example

# define a fucntion
def add_three(input_var):
    output_var = input_var + 3
    return output_var
    
    
'''
every function is composed of two pieces: a header and a body.

header: specifies name of function and its arguements
def add_three(input_var)

body: specifies the work that function does
    output_var = input_var + 3
    retun output_var
every LOC(line of code) in the fucntion body must be indented as exactly four spaces. 4 spaces/ tab. you can play with arguements and also retuen any value
    
def: keyword that tells python we are about define a function

add_three: name you choose for your function

(input_var):function's arguement(name of variable the function will use as an the input). fucntion cna have multiple arguements

return: keyword that tells python we are baout to exit a fucntion

output_var: value that is returned when the fucntion is exited

for every function, the parentheses enclosing the function arguemrnt(s) must be followed by colon ":".


'''

# how to run/call a function
new_number = add_three(10) # run the fucntion with 10 as input
print(new_number)# crosscheck expected value 13
# goldern-sword@Siddhants-MacBook-Air intro-to-programming % python3 03_functions.py
# 13

'''
 new_number = add_three(10)

new_number: this variable
=: sets the value of
add_three(10): the output we get when we run the fuction with 10 as input. when the function runs, it runs all codes in the body, from top to bottom
 
'''

# in python when we write add_three(), these empty parentheses are written just to make it clear that we are referring to a fucntion, as opposed to a variable or another python object. this writing manners, these parenthese should always be empty, even if function has arguements.

# naming functions: use only lowercase_letters,with words seperated by underscores_ instead of spaces.

# complex example
pay_rate_hr = 15 # 15$ per hr salary
tax_bracket_dec = .12 # 12% of salary cut to taxes
def get_pay(num_hours):
    pay_pretax = num_hours * pay_rate_hr
    pay_aftertax = pay_pretax * (1- tax_bracket_dec)
    return pay_aftertax

pay_fulltime = get_pay(40) # calculate pay based on working 40hrs
print(pay_fulltime) # 528.0

print(get_pay(30))# 396.0

# varibale "scope": part of the code where it is accessible.
# variables defined inside the fucntion body cannot be accessed outside of the function
# print(pay_aftertax) # no
'''
Traceback (most recent call last):
  File "/Users/goldern-sword/git/personal/kintsugi-stack-ai/intro-to-programming/03_functions.py", line 79, in <module>
    print(pay_aftertax)
          ^^^^^^^^^^^^
NameError: name 'pay_aftertax' is not defined
'''
# local scope vars, eg: pay_aftertax, can't accessed outisde fucntion get_pay()
# global scope vars, eg: pay_rate_hr, can be accessed anywhere

# function with multiple arguements
# more generalized, more useful, address more cases, more complicated
def get_pay_full(num_hours, pay_rate_hr, tax_brac_desc):
    return ((num_hours*pay_rate_hr)*(1-tax_brac_desc))

print(get_pay_full(40,24,.22))
# 748.8000000000001

# function with no arguements 
def print_hello():
    print("Hello, world !")
    
print_hello()# Hello, world !
```

## intro-to-programming/05-data-types.py

```

## intro-to-programming/07-conditions-and-conditional-statements.py
py
# datatypes

# intro
# each value has a corresponding data type
# types of datatypes: integer, floats, booleans, strings, dictionaries, sets, lists,tuples, etc.

# they are imp. as they set rules for action, actions should match the data type
# "cat"/"dog" no
# 12.0/2.0 yes

# integers
# integers are numebrs without any fractional part and can be positive and negative or zero
# ...,-3,-2,-1,0,1,2,3,....

x =14
print(x)
print(type(x))
# 14
# <class 'int'>

# floats 
# floats are numbers with fractional parts
# they can have many numbers after decimal
nearly_pi = 3.141592653589793238462643383279502884197169399375105820974944
print(nearly_pi)
print(type(nearly_pi))
# 3.141592653589793
# <class 'float'>

# we can also specify float with a fraction 
almost_pi = 22/7
print(almost_pi)
print(type(almost_pi))
# 3.142857142857143
# <class 'float'>

# round(): function helps to round a number to a specified number of decimal places.

rounded_pi = round(almost_pi,5)
print(rounded_pi)
print(type(rounded_pi))
# 3.14286
# <class 'float'>

# math.ceil(): rounds to nearest bigger  integer
import math
print(math.ceil(2.5))
print(math.ceil(2.2))
print(math.ceil(2.8))
print(math.ceil(-2.5))
print(math.ceil(-2.2))
print(math.ceil(-2.8))
'''
3
3
3
-2
-2
-2
'''

y_float = 1. # 1. , 1.0 , 1.00, 1.000 all considered as float
print(y_float)
print(type(y_float))
# 1.0
# <class 'float'>

# boolean
# represent one of only 2 values True, false

z_one = True
print(z_one)
print(type(z_one))
# True
# <class 'bool'>

z_one = False
print(z_one)
# False

# booleans are used to represent the truth of an expression. 
z_two = (1<2) # 1<2 is True
print(z_two)
# True
print(type(z_two))
# <class 'bool'>

z_two = (1>2) # 1>2 is False
print(z_two)
# False
print(type(z_two))
# <class 'bool'>

z_two = not z_two # not True is False, not False is True
print(z_two)
# True
print(type(z_two))
# <class 'bool'>

# what's happen if we multiple stuff with boolean values'
print(3 * True)
print(-3.1 * True)
print(type("abc" * False))
print(len("abc" * False))
# 3
# -3.1
# <class 'str'>
# 0

# boolean arithmetic
print(False + False)
print(True + False)
print(False + True)
print(True + True)
print(False + True + True + True)
# 0
# 1
# 1
# 2
# 3

# strings
# represent text
# collection of char ( alphabet letters, punctuation, numerical digits or symbols)
w = "hello, Python!"
print(w)
print(type(w))
print(len(w)) #len() function:  length of string
# hello, Python!
# <class 'str'>
# 14

w = "" # empty string (shortest string)
print(w)
print(type(w))
print(len(w))
# 
# <class 'str'>
# 0

my_number = "1.12321"
print(my_number)
print(type(my_number))
# 1.12321
# <class 'str'>

# float(): convert the string to float datatype , which is convertible
my_number = float(my_number)
print(my_number )
print(type(my_number))
# 1.12321
# <class 'float'>

print(int(1.2321))
print(int(1.747))
print(int(-3.94535))
print(int(-2.19774))
# 1
# 1
# -3
# -2

# concatnation of strings
# adding of strings
new_string = "abc"+"def"
print(new_string)
print(type(new_string))
# abcdef
# <class 'str'>

# subtraction & division is not possible
# multiplication by int(float and string not possible obv)

newest_string = "abc"*3
print(newest_string)
print(type(newest_string))
# abcabcabc
# <class 'str'>

# will_not_work = "abc" * 3.
'''
Traceback (most recent call last):
  File "/Users/goldern-sword/git/personal/kintsugi-stack-ai/intro-to-programming/05_data_types.py", line 149, in <module>
    will_not_work = "abc" * 3.
                    ~~~~~~^~~~

TypeError: can't multiply sequence by non-int of type 'float'
goldern-sword@Siddhants-MacBook-Air intro-to-programming %
'''


# complex example
def cost_of_project(engraving, solid_gold):
    cost = ((not solid_gold) *(50+(len(engraving)*7)))+(solid_gold*(100+(len(engraving)*10)))
    return cost
# reason for () at not solid_gold, operator precedence: Python evaluates * before not
```

## intro-to-programming/07-conditions-and-conditional-statements.py

```py
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

# here forgot to put semicolon after if and else and elif
def get_grade(score):
    # "A" - any grade 90-100, inclusive
    # "B" - any grade 80-89, inclusive
    # "C" - any grade 70-79, inclusive
    # "D" - any grade 60-69, inclusive
    # "F" - any grade <60
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else :
        return "F"
    
# here (gb-15)*1000 *0.10 is wrong, ((gb-15)*1000 )*0.10 is write
def get_phone_bill(gb):
    if gb<=15:
        return 100
    else:
        return 100 + ((gb-15)*1000 )*0.10
```

## intro-to-programming/09-intro-to-lists.py

```py
# Intro to Lists
# Organise data
# work with efficiently
# get an item at a specified position (first, second, third, etc),
# check the number of items, and
# add and remove items.

# can help to classify
# When doing data science, you need a way to organize your data so you can work with it efficiently. 
# Python has many data structures available for holding your data, such as lists, sets, dictionaries, and tuples.

flowers = "pink primrose,hard-leaved pocket orchid,canterbury bells,sweet pea,english marigold,tiger lily,moon orchid,bird of paradise,monkshood,globe thistle" # bad way to store data

print(type(flowers))
print(flowers)
# <class 'str'>
# pink primrose,hard-leaved pocket orchid,canterbury bells,sweet pea,english marigold,tiger lily,moon orchid,bird of paradise,monkshood,globe thistle

flowers_list = ["pink primrose", "hard-leaved pocket orchid", "canterbury bells", "sweet pea", "english marigold", "tiger lily", "moon orchid", "bird of paradise", "monkshood", "globe thistle"] # list representation

print(type(flowers_list))
print(flowers_list)
# <class 'list'>
# ['pink primrose', 'hard-leaved pocket orchid', 'canterbury bells', 'sweet pea', 'english marigold', 'tiger lily', 'moon orchid', 'bird of paradise', 'monkshood', 'globe thistle']

# length: len()
# The list has ten entries
print(len(flowers_list))
# 10

# indexing
# We can refer to any item in the list according to its position in the list (first, second, third, etc). This is called indexing.

# Note that Python uses zero-based indexing, which means that:

# to pull the first entry in the list, you use 0,
# to pull the second entry in the list, you use 1, and
# to pull the final entry in the list, you use one less than the length of the list.
print("First entry:", flowers_list[0])
print("Second entry:", flowers_list[1])

# The list has length ten, so we refer to final entry with 9
print("Last entry:", flowers_list[9])
# First entry: pink primrose
# Second entry: hard-leaved pocket orchid
# Last entry: globe thistle

# You may have noticed that in the code cell above, we use a single print() to print multiple items (both a Python string (like "First entry:") and a value from the list (like flowers_list[0]). To print multiple things in Python with a single command, we need only separate them with a comma.

# slicing
# You can also pull a segment of a list (for instance, the first three entries or the last two entries). This is called slicing. For instance:

# to pull the first x entries, you use [:x], and
# to pull the last y entries, you use [-y:].

print("First three entries:", flowers_list[:3]) # 0,1,2
print("Final two entries:", flowers_list[-2:]) # -2,-1
# First three entries: ['pink primrose', 'hard-leaved pocket orchid', 'canterbury bells']
# Final two entries: ['monkshood', 'globe thistle']

# As you can see above, when we slice a list, it returns a new, shortened list.

# .remove()
# Removing items
# Remove an item from a list with .remove(), and put the item you would like to remove in parentheses.

flowers_list.remove("globe thistle")
print(flowers_list)
# ['pink primrose', 'hard-leaved pocket orchid', 'canterbury bells', 'sweet pea', 'english marigold', 'tiger lily', 'moon orchid', 'bird of paradise', 'monkshood']

# .append()
# Adding items
# Add an item to a list with .append(), and put the item you would like to add in parentheses.

flowers_list.append("snapdragon")
print(flowers_list)
# ['pink primrose', 'hard-leaved pocket orchid', 'canterbury bells', 'sweet pea', 'english marigold', 'tiger lily', 'moon orchid', 'bird of paradise', 'monkshood', 'snapdragon']

# Lists are not just for strings
# So far, we have only worked with lists where each item in the list is a string. But lists can have items with any data type, including booleans, integers, and floats.

# As an example, consider hardcover book sales in the first week of April 2000 in a retail store.

hardcover_sales = [139, 128, 172, 139, 191, 168, 170]
# Here, hardcover_sales is a list of integers. Similar to when working with strings, you can still do things like get the length, pull individual entries, and extend the list.

# len()
print("Length of the list:", len(hardcover_sales))
print("Entry at index 2:", hardcover_sales[2])
# Length of the list: 7
# Entry at index 2: 172
# You can also get the minimum with min() and the maximum with max().

# min() & max()
print("Minimum:", min(hardcover_sales))
print("Maximum:", max(hardcover_sales))
# Minimum: 128
# Maximum: 191

# sum()
# To add every item in the list, use sum().

print("Total books sold in one week:", sum(hardcover_sales))
# Total books sold in one week: 1107
# We can also do similar calculations with slices of the list. In the next code cell, we take the sum from the first five days (sum(hardcover_sales[:5])), and then divide by five to get the average number of books sold in the first five days.

print("Average books sold in first five days:", sum(hardcover_sales[:5])/5)
# Average books sold in first five days: 153.8

alphabet = "A.B.C.D.E.F.G.H.I.J.K.L.M.N.O.P.Q.R.S.T.U.V.W.X.Y.Z"
address = "Mr. H. Potter,The cupboard under the Stairs,4 Privet Drive,Little Whinging,Surrey"
letters = alphabet.split(".")
formatted_address = address.split(",")
test_ratings = [1, 2, 3, 4, 5]
test_liked = [i>=4 for i in test_ratings]
print(test_liked) # [False, False, False, True, True]
print(sum(test_liked)) # 2
print(sum(test_liked)/len(test_liked)) # 0.4
```