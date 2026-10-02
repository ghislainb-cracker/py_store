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