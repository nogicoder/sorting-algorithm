#!/usr/bin/env python3
import argparse


# Bubble Sort Function
def bubble_sort_algo(lst):
    for t in range(len(lst)):
        for i in range(len(lst) - 1):
            count = 0
            if lst[i + 1] < lst[i]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                count += 1
            if count >= 1:
                print(" ".join(str(item) for item in lst))


# Insert Sort Function
def insert_sort_algo(lst):
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


# Partioning the list for the Quick Sort function
def partitioning(lst, start, end):
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


# Quick Sort main function
def quick_sort_algo(lst, start, end):
    if start < end:
        pIndex = partitioning(lst, start, end)
        quick_sort_algo(lst, start, pIndex - 1)
        quick_sort_algo(lst, pIndex + 1, end)


# Merging the list for the Merge Sort Function
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


# Merge sort main function
def merge_sort_algo(lst):
    if len(lst) > 1:
        s = int(len(lst)/2)
        lst1 = lst[:s]
        lst2 = lst[s:]
        merge_sort_algo(lst1)
        merge_sort_algo(lst2)
        merge(lst1, lst2, lst)
        print(" ".join(str(item) for item in lst))


# Main Function
def main():
    parser = argparse.ArgumentParser(prog="Sorting Deck",
                                     description="Implement & visualize \
                                     different sorting algorithm")
    parser.add_argument('N', nargs='+', help='an integer for the list to sort')
    parser.add_argument('--algo', default='bubble',
                        nargs='?',
                        choices=['bubble', 'insert', 'quick', 'merge'],
                        help="specify which algorithm to use for sorting \
                        among [bubble|insert|quick|merge], default bubble")
    parser.add_argument('--gui', action='store_true',
                        help='visualise the algorithm in GUI mode')
    args = parser.parse_args()
    lst = list(int(i) for i in args.N)
    if args.gui and len(lst) > 15:
        print('Input too large')
    elif not args.gui:
        if args.algo == 'bubble':
            bubble_sort_algo(lst)
        elif args.algo == 'insert':
            insert_sort_algo(lst)
        elif args.algo == 'quick':
            quick_sort_algo(lst, 0, len(lst) - 1)
        elif args.algo == 'merge':
            merge_sort_algo(lst)
    #  elif args.gui:


# Running the main function
if __name__ == "__main__":
    main()
