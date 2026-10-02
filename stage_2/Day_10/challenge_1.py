# parameters
def add(a, b):
    return a + b

# arguments
add(2,3)

# return values
def multiply(a, b):
    # gives the result back to the caller
    return a * b

def multiply(a, b):
    # it displays the result one
    print (a * b)


# local scope
def greet():
    name = "ghislain"
    print(name)
    
# global scope
name = "ghislain"

def greet():
    print(name)

greet()


#default arguments
def greet_name(name="ghislain"):
    print(f"hello my friend, {name}!")

# *args: is a turple containing all positional arguments
# handles extra positional arguments

def args(*args):
    print(args)

def add_args(*args):
    total = 0

    for num in args:
        total += num

    return total

# **kwargs: handles extra keyword arguments

def create_user(**kwargs):
    print(kwargs)

create_user(
    name="ghislain",
    age = 20,
    country = "Rwanda" 
)

#*args + **kwargs
def example(*args, **kwargs):
    print((args))
    print(kwargs)

example(
    10,
    20,
    30,
    name = "ghislain",
    role = "developer"
)

# OUTPUT:

# args = (10, 20, 30)

# kwargs = {
#     "name": "Ghislain",
#     "role": "Developer"
# }



# function calling other function

def add(a, b):
    return a+b

def double(number):
    return number * 2

result = double(add(10, 20))