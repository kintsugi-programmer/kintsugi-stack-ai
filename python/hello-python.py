'''
python
name comes from monty python comedy show
preety good language
readable 
simple
'''

egg_amt =0 # we dont need to declare variable, we dont need to declare datatype, like other lang
egg_amt = egg_amt+4
if egg_amt > 0: # : indicates that new codeblock is starting, indented, python use whitespaces instead of {} curly braces like other lang
    print("But I don't want ANY egg!")

viking_song = "Egg " * egg_amt # operator overloading(polymorphism-ish)
print(viking_song)

# goldern-sword@Siddhants-MacBook-Air kintsugi-stack-ai % python3 -u "/Users/goldern
# -sword/git/personal/kintsugi-stack-ai/python/hello-python.py"
# But I don't want ANY egg!
# Egg Egg Egg Egg 
# goldern-sword@Siddhants-MacBook-Air kintsugi-stack-ai % 


'''
print
is a python function that displays the value passed to the screen
'''

# comment

'''
c
o
m
m
e
n
t
'''

# = is assignment operator 

# 'string'
# "string"

# type() fucntion tells datatype
print(type(1))
print(type(-1))
print(type(1.1))
# <class 'int'>
# <class 'int'>
# <class 'float'>

# Arthmatics
'''
Operator	Name	Description
a + b	Addition	Sum of a and b
a - b	Subtraction	Difference of a and b
a * b	Multiplication	Product of a and b
a / b	True division	Quotient of a and b
a // b	Floor division	Quotient of a and b, removing fractional parts
a % b	Modulus	Integer remainder after division of a by b
a ** b	Exponentiation	a raised to the power of b
-a	Negation	The negative of a
'''
print(5/2) # gives float always
print(6/2)
print(5//2) # rounded off to next int
print(6//2)
# 2.5
# 3.0
# 2
# 3

# Order of ops
# PEMDAS - Parentheses, Exponents, Multiplication/Division, Addition/Subtraction.

print(8-3+2)
print(-3+4*2)
# 7
# 5

hat_height_cm = 25
my_height_cm = 190
# How tall am I, in meters, when wearing my hat?
total_height_meters = hat_height_cm + my_height_cm / 100
print("Height in meters =", total_height_meters, "?")
total_height_meters = (hat_height_cm + my_height_cm) / 100 # PARENTHESES FORCES THE OTHER OF SUB_EXPRESSIONS
print("Height in meters =", total_height_meters)
# Height in meters = 26.9 ?
# Height in meters = 2.15

# builtin func to play with numbers
print(min(1,2,3))
print(max(1,2,3))
print(abs(32))
print(abs(-32))
print(float(10))
print(int(3.33))
print(int("807")+1)
# 1
# 3
# 32
# 32
# 10.0
# 3
# 808


'''
Notebooks are composed of blocks (called "cells") of text and code. Each of these is editable, though you'll mainly be editing the code cells to answer some questions.

swap
tmp = a
a = b
b = tmp

or
a, b = b, a

'''