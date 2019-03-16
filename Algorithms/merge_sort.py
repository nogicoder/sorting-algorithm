n = [23, 4, 9, -8, 20, 7, 3]
n1 = [-6, -5, 1, 6, 8, 3, 7, -2, -7, 10, -10, 2, 4, -4, -3, 5,
      0, -1, 9, -9, -8]


# OLD
# def merge(lst1, lst2, lst):
#     i = 0
#     j = 0
#     k = 0
#     while i < len(lst1) and j < len(lst2):
#         if lst1[i] < lst2[j]:
#             lst[k] = lst1[i]
#             i += 1
#             k += 1
#         elif lst2[j] < lst1[i]:
#             lst[k] = lst2[j]
#             j += 1
#             k += 1
#     if i >= len(lst1):
#         while j < len(lst2):
#             lst[k] = lst2[j]
#             j += 1
#             k += 1
#     elif j >= len(lst2):
#         lst[k] = lst1[i]
#         i += 1
#         k += 1
#
#
# # Merge Sort Main Function
# def merge_sort_algo(lst):
#     if len(lst) > 1:
#         s = int(len(lst)/2)
#         lst1 = lst[:s]
#         lst2 = lst[s:]
#         merge_sort_algo(lst1)
#         merge_sort_algo(lst2)
#         merge(lst1, lst2, lst)
#         print(" ".join(str(item) for item in lst))


# NEW
def merge(lst1, lst2, lst):
    i = 0
    j = 0
    k = 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] <= lst2[j]:
            lst[k] = lst1[i]
            i += 1
        else:
            lst[k] = lst2[j]
            j += 1
        k += 1
    while i < len(lst1):
        lst[k] = lst1[i]
        i += 1
        k += 1
    while j < len(lst2):
        lst[k] = lst2[j]
        j += 1
        k += 1


def merge_sort(lst):
    if len(lst) > 1:
        s = int(len(lst)/2)
        lst1 = lst[:s]
        lst2 = lst[s:]
        merge_sort(lst1)
        merge_sort(lst2)
        merge(lst1, lst2, lst)
        print(" ".join(str(item) for item in lst))


merge_sort(n1)
