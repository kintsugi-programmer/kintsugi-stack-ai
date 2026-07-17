# functions
'''
function is block of code designed to perform a perform a specific task
reduce reduncy
avoid mistakes
more smart coding

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

