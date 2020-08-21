# decorators and generators vs lists
from datetime import datetime

num = 1000

def get_elapsed_time(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        print(datetime.now() - start)
        return result
    return wrapper

@get_elapsed_time
def even(n):
    l = []
    for i in range(n):
        if i % 2 == 0:
            l.append(i)
    return l

@get_elapsed_time
def gen_even(n):
    l = [x for x in range(n) if x % 2 == 0]
    return l


l1 = even(num)
l2 = gen_even(num)

print(l2)
print("Done")