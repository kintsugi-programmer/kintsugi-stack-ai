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