def new_decorator(func):

    def wrapper():
        print("code here before excecution")
        func()
        print("func has been called")

    return wrapper
"""
def needs_decorator():
    print("this function needs to be decorated")


x = new_decorator
print(f"\nthis is the wrapper function:\n- - - - - - - - - - - - - - - - - - - - - - - ")
print(x(new_decorator))


y = new_decorator(needs_decorator)
print("\nthis is the decorated function: \n- - - - - - - - - - - - - - - - - - - - - - -")
y()
print("\n- - - - - - - - - - - - - - - - - -\n    TESTING COMPLETE    \n")
"""


@new_decorator
def needs_decorator():
    print("this function needs to be decorated")

needs_decorator()
