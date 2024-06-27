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

 # 2. _______________________________________________________________ # 3.56

# Functions within functions

# add_two is declared inside the add_five_within function. 
def add_five_within(num):
  def add_two(inner_num): 
    return inner_num + 2
  
  # Call the inner function `add_two` with the argument `num` from the outer function.
  # Store the result to a variable. 
  num_plus_two = add_two(num) # `num` refers to the parameter of the add_five_within function.
  print(num_plus_two + 3) # 5

add_five_within(10) # 15
  
  
  