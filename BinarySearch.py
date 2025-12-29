import time


def binary_search(list, item):
    last_time = time.time()
    list = sorted(list)
    lower_index = 0
    upper_index = len(list)
    while 1:
        index = (lower_index + upper_index) // 2
        if list[index] == item:
            print(f'Binary Search :- {time.time() - last_time}')
            return index
        elif list[index] > item:
            upper_index = index
        elif list[index] < item:
            lower_index = index
        if lower_index == upper_index - 1:
            print(f'Binary Search :- {time.time() - last_time}')
            return -1


test = [i for i in range(100000)]

print(binary_search(test, 90000))
