import random
import time

array = [random.randint(1, 1000) for i in range(1000)]


def bubble_sort(list):
    last_time = time.time()
    """
    I terminated this by:
        if any value is swapped any time during traversing the list swapped
        is set to True and after the list ends its again set to False
        And it is terminated is the Swapping hasn't occured any time during traversing
        Then, i check that if the swapping is False and The List has been traversed then it
        is terminated...
    """
    index = 0
    swapped = False
    while 1 and (len(list) != 0):
        if list[index] > list[index + 1]:
            list[index], list[index + 1] = list[index + 1], list[index]
            swapped = True
        index = (index + 1) % (len(array) - 1)
        if index == 0:
            swapped = False
        if (index == len(list) - 2) and not swapped:
            print(f'Bubble Sorting done in {time.time() - last_time} seconds')
            return list
        # print(swapped)
        # print(list)
    return -1


print(array)
print(bubble_sort(array))
