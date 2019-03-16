import pyglet

a = [0, 1, -3, 6, 2, 10]
numbers = [[str(item) for item in a]]

def bubble_sort_algo(lst):
    move = []
    for t in range(len(lst)):
        swap = False
        for i in range(len(lst) - 1):
            move.append(('n', lst[i], lst[i + 1]))
            if lst[i + 1] < lst[i]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                swap = True
                print(lst)
                move.append(('y', lst[i], lst[i + 1]))
        if swap == False:
            break
    return move


move = bubble_sort_algo(a)


# for lst in list:
#     num_obj_list = []
#     for number in lst:
#         num_obj_list.append(number)
#     numbers.append(num_obj_list)

for item in move:
    print(item)
