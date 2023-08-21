from random import randint
import time

def show_test(upper: int) -> str :
    print(randint(1,upper))
    print(time.time())
    return 1234


print(show_test(100))