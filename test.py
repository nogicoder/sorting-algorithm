import pyglet
from pyglet import clock
from pyglet import window
import time


class Number:
    def __init__(self, value, i, len, color, velo):
        global window
        self.x = i*(window.width//len) + 50
        self.y = (window.height)//2
        self.color = color
        self.label = pyglet.text.Label(value, font_size = 30, x=self.x, y=self.y, color=self.color)
        self.velocity = velo*(window.width//len)


    def draw(self):
        self.label.draw()


    def move(self):
        self.x += self.velocity


    def delete(self):
        self.label.delete()

class SortingDeckWindow(window.Window):
    def __init__(self, numbers, move):
        window.Window.__init__(self, 1200, 900)
        self.set_mouse_visible(False)
        self.numlist = numbers
        self.move = move
        self.sorted = sorted
        self.dp_list = []
        self.key_held = []


    def on_draw(self):
        self.clear()
        print("this is draw")
        # self.moving_num(self.dp_list)
        for item in self.dp_list:
            item.draw()


    def delete(self, array):
        for num in array:
            num.delete()


    def moving_num(self, array):
        for num in array:
            num.move()


    def update(self, dt):
        print("this is update")
        global i
        if i < len(self.move):
            self.delete(self.dp_list)
            for j in range(len(self.numlist)):
                value = self.numlist[j]
                color = (255, 255, 255, 255)
                num = Number(str(value), j, len(self.numlist), color, 0)
                if value in self.move[i]:
                    color = (255, 0, 0, 255)
                    num = Number(str(value), j, len(self.numlist), color, 0)
                    if self.move[i] == 'y' and value == self.move[i][-2]:
                        num = Number(str(value), j, len(self.numlist), color, 1)
                    elif self.move[i] == 'y' and value == self.move[i][-1]:
                        num = Number(str(value), j, len(self.numlist), color, -1)
                self.dp_list.append(num)
            i += 1
        self.moving_num(self.dp_list)


'''--------------------------------GUI---------------------------------------'''
a = [0, 1, -3, 6, 2, 10]
i = 0


def bubble_sort_algo(lst):
    move = []
    for t in range(len(lst)):
        swap = False
        for i in range(len(lst) - 1):
            move.append(('n', lst[i], lst[i + 1]))
            if lst[i + 1] < lst[i]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                swap = True
                # print(lst)
                move.append(('y', lst[i], lst[i + 1]))
        if swap == False:
            break
    move.append(lst)
    return move


move = bubble_sort_algo(a)


b = [0, 1, -3, 6, 2, 10]


if __name__ == "__main__":
    window = SortingDeckWindow(b, move)
    pyglet.clock.schedule_interval(window.update, 0.2)
    pyglet.app.run()
