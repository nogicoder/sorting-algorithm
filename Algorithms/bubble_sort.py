n = [23, 9, -8, 7, 3]
n1 = [1, 2, 3, 6, 90]


def bubble_sort(lst):
    for t in range(len(lst)):
        for i in range(len(lst) - 1):
            count = 0
            if lst[i + 1] < lst[i]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                count += 1
            if count >= 1:
                print(" ".join(str(item) for item in lst))


bubble_sort(n)
