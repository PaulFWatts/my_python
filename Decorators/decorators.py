import logging

# Functions are first class objects
def say_hello(name, logger):
    logger(f"Hello {name}")
    
def reversed_print(text):
    print(text[::-1].capitalize())
    
def hello(func):
    print(f"Hello {func.__name__}")
    return func

def wrapper(func):
    def _wrapper():
        print(f"Before {func.__name__}")
        func()
        print(f"After {func.__name__}")
    return _wrapper
    
    
say_hello("world", logger=print) # passing the print function object as a parameter, don't use print()

say_hello("logs", logger=logging.warning)

with open("say_hello.txt", mode ="w") as file:
    say_hello("files", logger=file.write)
    
reversed_print("Hi there")

say_hello("nocyp", logger=reversed_print)

# Inner functions

def outer():
    print("Hi from the outer function")
    pycon = 2022
    def inner():
        print("Hi from the inner function")
        print(f"Pycon is {pycon}")
    inner()
    return inner
    
outer()
inside = outer()
inside()

# Manipulate functions

hello(outer)
hello(inside) # Displays the orginal function name, inner
hello(outer)()
new_outer = hello(outer)
new_outer()

wrapper(outer)

new_outer= wrapper(outer)
new_outer()

print()
outer()
print()
outer = wrapper(outer) # this "decorates" the outer function and changes its behaviour: same as @wrapper
outer()
print()

# A decorator is any function that takes another function as an argument and returns a new function
