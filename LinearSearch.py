import time


def linear_search(list, item):
    last_time = time.time()
    index = 0
    while index < len(list):
        if list[index] == item:
            print(f'Linear Search :- {time.time() - last_time}')
            return index
        index += 1
    else:
        print(f'Linear Search :- {time.time() - last_time}')
        return -1


test = [i for i in range(100000)]
print(linear_search(test, 90000))
