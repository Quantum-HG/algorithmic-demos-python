import copy
import random
import time


def insertion_sort(list):
    last_time = time.time()
    index = 1
    while index <= len(list) - 1:
        current = list[index]
        i = copy.deepcopy(index)
        while 1:
            if 0 <= i - 1 <= len(list) - 1:
                if list[i - 1] > current:
                    list[i] = list[i - 1]
                    i -= 1
                else:
                    list[i] = current
                    break
            else:
                list[i] = current
                break

        index += 1

    else:
        print(f'Insertion Sorting done in {time.time() - last_time} seconds')
        return list


array = [random.randint(1, 1000) for i in range(2000)]

print(insertion_sort(array))
# l = [0, 1]
# g = copy.deepcopy(l)
# g.append(5)
# print(g)
# print(l)
