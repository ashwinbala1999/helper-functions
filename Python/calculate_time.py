import time

"""
Usage:

@calculate_time
def factorial(num):
    time.sleep(2)
    print(math.factorial(num))
    
factorial(10)

"""

def calculate_time(func):
    def inner(*args, **kwargs):
        begin = time.time()
        func(*args, **kwargs)
        end = time.time()
        print("Total time taken in : ", func.__name__, end - begin)
    return inner
