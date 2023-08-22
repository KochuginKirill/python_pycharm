def remove_every_other(my_list):
    return [i for i in my_list if my_list.index(i) / 2 == 0]


n = remove_every_other(["Keep", "Remove", 1, "Remove", "Keep"])
print(n)
