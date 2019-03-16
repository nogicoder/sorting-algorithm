n = [23, 10, 9, -8, 20, 7, 3]


def parting(lst, start, end):
    pIndex = start
    pivot = lst[end]
    for i in range(start, end):
        if lst[i] <= pivot:
            lst[i], lst[pIndex] = lst[pIndex], lst[i]
            pIndex += 1
    lst[pIndex], lst[end] = lst[end], lst[pIndex]
    print("P: " + str(pivot))
    print(" ".join(str(item) for item in lst))
    return pIndex


def quick_sort(lst, start, end):
    if start < end:
        pIndex = parting(lst, start, end)
        quick_sort(lst, start, pIndex - 1)
        quick_sort(lst, pIndex + 1, end)


quick_sort(n, 0, len(n) - 1)
