#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    del my_list[idx]
    return my_list
lst = [1, 2, 3, 4, 5]
print(delete_at(lst, 3))
print(lst)              
