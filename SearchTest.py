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


def interpolation_search(list, item):
    last_time = time.time()
    list = sorted(list)
    low, high = 0, len(list) - 1
    while 1:
        probe = int(low + ((high - low) / (list[high] - list[low])) * (item - list[low]))
        if 0 < probe < len(list) - 1:
            if list[probe] == item:
                print(f'Interpolation Search :- {time.time() - last_time}')
                return probe
            elif list[probe] > item:
                high = probe - 1
            elif list[probe] < item:
                low = probe + 1
        else:
            print(f'Interpolation Search :- {time.time() - last_time}')
            return -1


test = [i for i in range(10000000)]
print('Linear Search Vs Binary Search Vs Interpolation Search')
inp = input('Press enter to see the Results:  ')

print(binary_search(test, 9000000), linear_search(test, 9000000), interpolation_search(test, 9000000))
