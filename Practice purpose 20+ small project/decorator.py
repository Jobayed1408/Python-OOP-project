import math 
import time

def timer(func):
    def inner(*args, **kwargs):
        print('time started')
        start = time.time()
        func(*args, **kwargs) 
        print('time sesh')
        end = time.time() 
        print(f'total time = {end - start }')
    return inner

@timer
def get_factorial(n):
    print('factorial starting')
    result =  math.factorial(n) 
    print(f'factorial of {n}: {result}')
# timer()()

get_factorial(n=5)
