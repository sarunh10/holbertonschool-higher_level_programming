#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            if i < x - 1:
                print(my_list[i], end=" ")
            else:
                print(my_list[i], end="")
            count += 1
    except IndexError:
        print()
        return count
    print()
    return count
