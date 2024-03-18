# let's make some functions to use in our main program:

# Function to get the user's name

#def greet_user():
#   print("Hello! Welcome to the program.")

#greet_user()

def sqaure(number):
    return number * number

# print(sqaure(10))

def fictorial(number):
    if number == 1 or number == 0:
        return 1
    else:
        return number * fictorial(number - 1) 
       
print(fictorial(5))

#lambda function:

x = lambda a: a.upper()    
print(x("Faizan"))

#lambda function with multiple arguments:
multiply = lambda a, b: a * b
print(multiply(5, 6))