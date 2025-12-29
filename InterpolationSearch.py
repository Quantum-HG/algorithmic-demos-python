import time

"""mid = Lo + ((Hi - Lo) / (A[Hi] - A[Lo])) * (X - A[Lo])

where −
   A    = list
   Lo   = Lowest index of the list
   Hi   = Highest index of the list
   A[n] = Value stored at index n in the list"""


# Needs Sorted Array!
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


print(interpolation_search([1, 2, 3, 4, 5, 6, 7, 8, 65, 68, 85, 438, 468], 0))
