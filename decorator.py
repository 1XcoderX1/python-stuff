def my_decorator(func):
    def wrapper():
        print("Line Number 1")
        func()
        print("Line Number 2")
    return wrapper

@my_decorator
def say_hello():
    print("Hello I am line Number 2")

print(say_hello())
