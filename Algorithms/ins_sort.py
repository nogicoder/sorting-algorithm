n = [1, 3, 8, -7, 10, 4, 2]
n1 = [-6, -5, 1, 6, 8, 3, 7, -2, -7, 10, -10, 2, 4, -4, -3, 5, 0,
      -1, 9, -9, -8]

# OLD:
# def insert_sort_algo(lst):
#     for i in range(1, len(lst)):
#         num = lst[i]
#         temp = lst[:i]
#         temp = temp[::-1]
#         count = 0
#         for j in temp:
#             t = lst.index(j)
#             f = lst.index(num)
#             if j > num:
#                 lst[f], lst[t] = lst[t], lst[f]
#                 count += 1
#         if count > 1:
#             print(" ".join(str(item) for item in lst))


"""NEW"""


def insert_sort(lst):
    for i in range(1, len(lst)):
        num = lst[i]
        slot = i
        count = 0
        while slot > 0 and lst[slot - 1] > num:
            lst[slot] = lst[slot - 1]
            slot = slot - 1
        lst[slot] = num
        if slot != i:
            print(" ".join(str(item) for item in lst))


insert_sort(n1)
