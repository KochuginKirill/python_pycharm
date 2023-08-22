<<<<<<< HEAD
from random import randint
import time

def show_test(upper: int) -> str :
    print(randint(1,upper))
    print(time.time())
    return 1234


print(show_test(100))
=======
def remove_every_other(my_list):
    return [i for i in my_list if my_list.index(i) / 2 == 0]


n = remove_every_other(["Keep", "Remove", 1, "Remove", "Keep"])
print(n)
>>>>>>> origin/master
