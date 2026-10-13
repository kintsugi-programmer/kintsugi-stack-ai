# help(): help displays 1. Header with arguements. 2. English desc.

# help(abs)
# Help on built-in function abs in module builtins:
# abs(x, /)
#     Return the absolute value of the argument.
# s line 1/4 (END) (press h for help or q to quit)

# help(round(-2.01))
# Help on int object:
# class int(object)
#  |  int([x]) -> integer
#  |  int(x, base=10) -> integer
#  |
#  |  Convert a number or string to an integer, or return 0 if no arguments
#  |  are given.  If x is a number, return x.__int__().  For floating-point
#  |  numbers, this truncates towards zero.
#  |
#  |  If x is not a number or if base is given, then x must be a string,
#  |  bytes, or bytearray instance representing an integer literal in the
#  |  given base.  The literal can be preceded by '+' or '-' and be surrounded

# help(print)
# Help on built-in function print in module builtins:
# print(*args, sep=' ', end='\n', file=None, flush=False)
#     Prints the values to a stream, or to sys.stdout by default.
#     sep
#       string inserted between values, default a space.
#     end
#       string appended after the last value, default a newline.
#     file
#       a file-like object (stream); defaults to the current sys.stdout.
#     flush
#       whether to forcibly flush the stream.

# defining functions
def least_difference(a,b,c):
    """
    Return the smallest difference between any two numbers
    among a, b and c.
    >>> least_difference(1, 5, -5)
    4
    """
    diff1=abs(a-b)
    diff2=abs(b-c)
    diff3=abs(a-c)
    return min(diff1,diff2,diff3)
# Functions start with a header introduced by the def keyword. The indented block of code following the : is run when the function is called.

# return is another keyword uniquely associated with functions. When Python encounters a return statement, it exits the function immediately, and passes the value on the right hand side to the calling context.

print(least_difference(1,10,100),
      least_difference(1,10,10),
      least_difference(5,6,7),
      # Python allows trailing commas in argument lists. How nice is that?
      )
# 9 0 1

# help(least_difference)
# Help on function least_difference in module __main__:
# least_difference(a, b, c)
#     Return the smallest difference between any two numbers
#     among a, b and c.
#     >>> least_difference(1, 5, -5)
#     4

# The docstring is a triple-quoted string (which may span multiple lines) that comes immediately after the header of a function. When we call help() on a function, it shows the docstring.

# Aside: The last two lines of the docstring are an example function call and result. 
# (The >>> is a reference to the command prompt used in Python interactive shells.) 
# Python doesn't run the example call - it's just there for the benefit of the reader. 
# The convention of including 1 or more example calls in a function's docstring is far from universally observed, but it can be very effective at helping someone understand your function. 

# For a real-world example, see this docstring for the numpy function np.eye.
def eye(N, M=None, k=0, dtype=float, order='C'):
    """
    Return a 2-D array with ones on the diagonal and zeros elsewhere.

    Parameters
    ----------
    N : int
      Number of rows in the output.
    M : int, optional
      Number of columns in the output. If None, defaults to `N`.
    k : int, optional
      Index of the diagonal: 0 (the default) refers to the main diagonal,
      a positive value refers to an upper diagonal, and a negative value
      to a lower diagonal.
    dtype : data-type, optional
      Data-type of the returned array.
    order : {'C', 'F'}, optional
        Whether the output should be stored in row-major (C-style) or
        column-major (Fortran-style) order in memory.

        .. versionadded:: 1.14.0
         Returns
    -------
    I : ndarray of shape (N,M)
      An array where all elements are equal to zero, except for the `k`-th
      diagonal, whose values are equal to one.

    See Also
    --------
    identity : (almost) equivalent function
    diag : diagonal 2-D array from a 1-D array specified by the user.

    Examples
    --------
    >>> np.eye(2, dtype=int)
    array([[1, 0],
           [0, 1]])
    >>> np.eye(3, k=1)
    array([[ 0.,  1.,  0.],
           [ 0.,  0.,  1.],
           [ 0.,  0.,  0.]])

    """
    if M is None:
        M = N
    m = zeros((N, M), dtype=dtype, order=order)
    if k >= M:
        return m
    if k >= 0:
        i = k
    else:
        i = (-k) * M
    m[:M-k].flat[i::M+1] = 1
    return m

# not returning function/ void functions
def least_difference(a, b, c):
    """Return the smallest difference between any two numbers
    among a, b and c.
    """
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    min(diff1, diff2, diff3)
    
print(
    least_difference(1, 10, 100),
    least_difference(1, 10, 10),
    least_difference(5, 6, 7),
)
# None None None

mystery = print()
print(mystery)

# None

# None is special void value, same as null in other languages

# default arguements
print(1,2,3,sep='<<<')
# 1<<<2<<<3

print(1,2,3,sep=')  (') # But if we don't specify a value, sep is treated as having a default value of ' ' (a single space).
# 1)  (2)  (3

# Adding optional arguments with default values to the functions we define turns out to be pretty easy
def greet(who="Colin"):
    print("Hello,", who)
greet()
greet(who="Kaggle")
# (In this case, we don't need to specify the name of the argument, because it's unambiguous.)
greet("world")
# Hello, Colin
# Hello, Kaggle
# Hello, world

# Functions Applied to Functions¶
# You can supply functions as arguments to other functions. 

def mult_by_five(x):
    return 5*x
def call(function, arguement):
    """
    call function on arguement
    """
    return function(arguement) # HIGHER ORDER FUNCTIONS Functions that operate on other functions are called "higher-order functions.
def squared_call(function, arguement):
    """
    call function on the result of calling function on arguement
    """
    return function(function(arguement))
print(call(mult_by_five,1), 
      squared_call(mult_by_five,1), 
      sep='\n', # '\n' is the newline character - it starts a new line
      )
# 5
# 25

# By default, max returns the largest of its arguments. But if we pass in a function using the optional key argument, it returns the argument x that maximizes key(x) (aka the 'argmax').
def mod_5(x):
    """Return the remainder of x after dividing by 5"""
    return x % 5

print(
    'Which number is biggest?',
    max(100, 51, 14), 
    # 100 > 51 > 14
    'Which number is the biggest modulo 5?',
    max(100, 51, 14, key=mod_5),
    # mod_5(100)  # 0
    # mod_5(51)   # 1
    # mod_5(14)   # 4
    sep='\n',
)
# Which number is biggest?
# 100
# Which number is the biggest modulo 5?
# 14

# pass
def round_to_two_places(num):
    """Return the given number rounded to two decimal places. 
    
    >>> round_to_two_places(3.14159)
    3.14
    """
    # Replace this body with your own code.
    # ("pass" is a keyword that does literally nothing. We used it as a placeholder
    # because after we begin a code block, Python requires at least one line of code)
    pass

def round_to_two_places(num):
    """Return the given number rounded to two decimal places. 
    
    >>> round_to_two_places(3.14159)
    3.14
    """
    # Replace this body with your own code.
    # ("pass" is a keyword that does literally nothing. We used it as a placeholder
    # because after we begin a code block, Python requires at least one line of code)
    # pass
    return round(num,2)


# round()
print(round(222.444,2))
print(round(222.444,-2))
print(round(2222.4444,-3))
# 222.44
# 200.0
# 2000.0



def to_smash(total_candies, x=3):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between x friends. x is optional (default is 3)
    
    >>> to_smash(91)
    1
    """
    return total_candies % x