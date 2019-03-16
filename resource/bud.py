import pyglet
import math
import random
import os
from pyglet import clock
from random import randint
from pyglet.window import key


def getpath(folder):
    res = os.getcwd().replace('version1','resources') + '/' + folder
    return res

path1 = getpath('positive')
path2 = getpath('negative')
space = 0
height = 768
width = 1024
lives = 3
score = 0
change = 0

game_window = pyglet.window.Window(width, height)


pyglet.resource.path = [getpath('')]
pyglet.resource.reindex()

image_f = pyglet.resource.image('m.png')
image_f1 = pyglet.resource.image('m1.png')
image_f2 = pyglet.resource.image('m2.png')
bg = pyglet.resource.image("bg.jpg")

music = pyglet.resource.media('music.mp3')


sound1 = pyglet.resource.media('explosion.wav', streaming=False)
sound2 = pyglet.resource.media('suss.wav', streaming=False)


main_batch = pyglet.graphics.Batch()

smile_f = pyglet.sprite.Sprite(image_f, x=0, batch=main_batch)



animation = pyglet.resource.animation('storm.gif')
sprite = pyglet.sprite.Sprite(animation,batch=None)



score_label = pyglet.text.Label(text="Score: %s" % score, x=0,
                                y=height - 50, color = (1,2,3,255),
                                font_size = 24,batch=main_batch)
live_label = pyglet.text.Label(text="Lives: %s" % lives, x=width - 130,
                                y=height - 50, color = (1,2,3,255),
                                font_size = 24,batch=main_batch)
level_label = pyglet.text.Label(text="How to lead a buddhist life",
                                x=0, y=height - 100, color = (1,2,3,255),
                                font_size = 24,batch=main_batch)
gameover = pyglet.text.Label(text="GAMEOVER", x=width / 2 - 40 * 4,
                                y=height / 2, color = (1,2,3,255),
                                font_size = 40,batch=None)


def getSprite(path, speed):
    res = []
    listname = os.listdir(path)
    pyglet.resource.path = [path]
    pyglet.resource.reindex()
    for i in listname:
        image = pyglet.resource.image(i)
        sprite = pyglet.sprite.Sprite(image,x = randint(0, width), y=height)
        sprite.velocity_x = speed
        sprite.velocity_y = randint(1,speed)
        sprite.rotation = random.choice([1,-1])
        res.append(sprite)
    return res

def callback(_):
    sprite.batch=None

def changeSpeed(mainlist):
    for i in mainlist:
        i.velocity_y += 0.5

def update(_):
    global score, lives, space, change
    print(score)
    if score == 0 and change == 0:
        smile_f.image = image_f
        getRandomDict(5)
        change = 1
    if score == 5 and change == 1:
        smile_f.image = image_f1
        changeSpeed(maindict['positive'] + maindict['negative'])
        getRandomDict(10)
        change = 2
    if score == 20 and change == 2:
        smile_f.image = image_f2
        changeSpeed(maindict['positive'] + maindict['negative'])
        getRandomDict(10)
        change = 0
    angle_radians = -math.radians(randint(200,201))
    force_x = math.sin(angle_radians)
    ok = sprite
    if space > 0 and lives > 0:
        for i in maindict['positive'] + maindict['negative']:
            temp = (i.x + i.x + i.width)/2
            left = smile_f.position[0]
            right = smile_f.position[0] + smile_f.width
            if i.y >= smile_f.height:
                if temp < -30:
                    i.x == width
                elif temp > height + 30:
                    i.x == 0
                i.x += force_x * i.rotation
                i.y -= i.velocity_y
            elif i.y < smile_f.height and i.y > -10:
                if temp > left and temp < right:
                        if i in maindict['positive']:
                            score += 1
                            sound2.play()
                            score_label.text="Score: %s" % score
                            i.y = height
                            clock.schedule_interval(callback, 3)
                            i.x = randint(0, width) + 30
                            if i.velocity_y < i.velocity_x:
                                i.velocity_y += randint(0,1)
                            elif i.velocity_y >= i.velocity_x:
                                i.velocity_y -= randint(0,1)
                        else:
                            if lives > 0:
                                lives -= 1
                            sound1.play()
                            live_label.text="Lives: %s" % lives
                            ok.x = 0
                            ok.y = 0
                            ok.batch = main_batch
                            i.y = height
                            clock.schedule_interval(callback, 5)
                            i.x = randint(0, width) + 30
                            if i.velocity_y < i.velocity_x:
                                i.velocity_y += randint(0,1)
                            elif i.velocity_y >= i.velocity_x:
                                i.velocity_y -= randint(0,1)
                else:
                    i.y -= i.velocity_y
            else:
                if lives == 0:
                    i.y = -100
                else:
                    i.y = height
                    i.x = randint(0, width) + 30
                    if i.velocity_y < i.velocity_x:
                        i.velocity_y += randint(0,1)
                    elif i.velocity_y >= i.velocity_x:
                        i.velocity_y -= randint(0,1)
                        i.rotation = random.choice([1,-1])

def getRandomSprite(listsprite, number):
    res = []
    for i in range(number):
        res.append(random.choice(listsprite))
    return res

positive = getSprite(path1, 3)
negative = getSprite(path2, 3)
maindict = {}

def getRandomDict(number):
    global maindict
    maindict['positive'] = getRandomSprite(positive,number)
    maindict['negative'] = getRandomSprite(negative,number)

getRandomDict(5)

@game_window.event
def on_key_press(symbol, modifiers):
    global right, left, space, lives, score
    if symbol == key.SPACE:
        space += 1
        lives = 3
        score = 0
        score_label.text="Score: %s" % score
        live_label.text="Lives: %s" % lives
    if smile_f.x <= width - 100 and smile_f.x > -1:
        if symbol == key.RIGHT:
            smile_f.x += 50
        if symbol == key.LEFT:
            smile_f.x -= 50
    elif smile_f.x > width - 100:
        smile_f.x = width - 100
    else:
        smile_f.x = 0


@game_window.event
def on_draw():
    global lives, space
    game_window.clear()
    bg.blit(0, 0)
    smile_f.draw()
    main_batch.draw()
    if lives == 0:
        space = 0
        game_window.clear()
        bg.blit(0, 0)
        smile_f.draw()
        gameover.batch = main_batch
        main_batch.draw()
    elif space > 0:
        gameover.batch = None
        bg.blit(0, 0)
        smile_f.draw()
        main_batch.draw()
        for i in maindict['positive'] + maindict['negative']:
            i.draw()

pyglet.clock.schedule_interval(update,1/60)
player = pyglet.media.Player()
player.queue(music)
player.eos_action = pyglet.media.SourceGroup.loop
player.play()

if __name__ == '__main__':
    pyglet.app.run()
