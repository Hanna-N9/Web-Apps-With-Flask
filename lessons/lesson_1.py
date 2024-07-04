# Reference from the video, https://www.youtube.com/watch?v=WOHsHaaJ8VQ based on Decorators in Python

# Decorators allow programmers to wrap a function with another function) without modifying its source code. Decorators can be applied using
# the @ symbol followed by the decorator name before the function definition. This is to make code cleaner and readable.

# Six different steps/ways to use functions and then finally, in the end, to use decorators: 

 # 1. _______________________________________________________________

# All functions are objects
  # As functions are objects, they can be used the same way as data types are used. Functions can be assigned to variables, passed as 
  # arguments to other functions, returned as values from other functions, and so on.
   
def add_five(num):
  print(num + 5)
  
add_five(3) # 7

 # 2. _______________________________________________________________ 

# Functions within functions

# add_two is declared inside the scope of add_five_within function.
def add_five_within(num):
  def add_two(inner_num): 
    return inner_num + 2
  
  # Call the inner function add_two with the argument `num` from the outer function
    # When add_two (ivoked) is called with num as its argument, the value of num from add_five_within is passed to add_two (invoked). 
    # At this moment, add_two (invoked) does not yet know what num is; it just knows it is receiving an argument from the outer function. 
    # Then, inside add_two (function name), inner_num gets the value of num.
  # Store the result to a variable. 
  num_plus_two = add_two(num) # `num` refers to the parameter of the add_five_within function. 
  print(num_plus_two + 3) # 5

add_five_within(10) # 15

 # 3. _______________________________________________________________ 

# Returning functions from functions

# This function is going to return a function that adds or substracts a number
def get_math_function(operation): # + or -
  def add(n1, n2):
    return n1 + n2
  def sub(n1, n2):
    return n1 - n2
  
  # Returning a function and not number
  if operation == "+":
    return add 
  elif operation == "-":
    return sub

add_function = get_math_function("+")
sub_function = get_math_function("-")

print( add_function(4,6) ) # 10
print( sub_function(4,6) ) # -2

 # 4. _______________________________________________________________ 
 
# Decorating a function

# title_decorator takes print_a_name function and print a name as well as printing out a title
# Define a nested function called wrapper inside the decorator to print a title and a name
# Return the wrapper function
def title_decorator(print_name_function):
  def wrapper(): 
    print("Professor:")
    print_name_function()
  return wrapper

# Define a function to print a name.
def print_a_name():
  print("Samantha")

# Call title_decorator function, pass in print_a_name function, that passes us back a wrapper function
# The result is a new function (decorated_function) that, when called, will first print "Professor:" and then call print_a_name().
decorated_function = title_decorator(print_a_name)

# Trigger the execution of the wrapper function defined within title_decorator
decorated_function()
 
# 16:35
 



  
  