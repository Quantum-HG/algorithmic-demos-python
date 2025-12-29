import random
import time

array = [random.randint(1, 1000) for i in range(1000)]


def selection_sort(list):
    last_time = time.time()
    lowest_value = []
    lower_index = 0
    upper_index = len(list) - 1
    index = 0
    while 1 and (len(list) != 0):
        if not lowest_value:
            lowest_value = [list[index], index]
        if list[index] < lowest_value[0]:
            lowest_value = [list[index], index]
        if index == upper_index:
            list[lower_index], list[lowest_value[1]] = list[lowest_value[1]], list[lower_index]
            lower_index += 1
            lowest_value = []
        # upper_index - lower_index  + 1 gives the length of list between low and upper indices
        try:
            index = ((index + 1) % (upper_index - lower_index + 1)) + lower_index  # (to increase the lower pointer)
        except:
            print(f'Selection Sorting done in {time.time() - last_time} seconds')
            return list
        """whenever the lower index will move towards the upper index and such that upper index tends to lowest
        a ZeroDivisionError will be raised"""
        # print(list, lower_index)
    return -1


print(selection_sort(array))
