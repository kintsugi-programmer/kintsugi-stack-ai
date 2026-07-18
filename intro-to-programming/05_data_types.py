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
''''
