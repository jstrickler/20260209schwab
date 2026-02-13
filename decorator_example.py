from datetime import datetime
from functools import wraps

def timestamp(func):
    @wraps(func)
    def new_func(*args, **kwargs): # replacement function
        print(f"{func.__name__} called at {datetime.now().ctime()}")
        return func(*args, **kwargs)
    return new_func

@timestamp
def spam():
    print("Hello from spam()")

@timestamp
def ham(ham_count):
    print(" ".join(["HAM"] * ham_count))

spam()
ham(5)
print(f"{spam.__name__ = }")
