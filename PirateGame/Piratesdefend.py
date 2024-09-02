import pgzrun
import random
import time
WIDTH = 600
HEIGHT = 400
#variables
running = True
speed = 14
bullets = []
enemies = []
score = 0
GameOver = False
YouWin = False
direction = 1
#actors
MarineShip = Actor("marineship.png")
AllSunny = Actor("allsunny.png")
for i in range(5):
    enemies.append(Actor("marineship.png"))
    enemies[-1].x = 100+90 * i
    enemies[-1].y = 5
def on_key_down(key):
    if key == keys.SPACE:
        bullets.append(Actor("bullet.png"))
        bullets[-1].x = AllSunny.x
        bullets[-1].y = AllSunny.y-50
def Win():
    global YouWin
    YouWin = True

def draw():
    screen.blit("sea.jpeg",(0,0))
    screen.draw.text("score:"+str(score), color = "White", topleft = (420,20))
    AllSunny.draw()
    AllSunny.y = (335)
    for i in enemies:
        i.draw()
    for g in bullets:
        g.draw()
    if YouWin == True:
        screen.fill("white")
        screen.draw.text("Congratulations, you win!", midtop = (300,200), color = "green", fontsize = 50)
def update():
    if keyboard.left:
        AllSunny.x = AllSunny.x-2
    if keyboard.right:
        AllSunny.x = AllSunny.x+2
    for g in bullets:
        if g.y <= 0:
            bullets.remove(g)
        else:
            g.y -= 15
    global score, direction
    movedown = False
    if len(enemies) > 0 and (enemies[-1].x > WIDTH-80 or enemies[0].x < 80):
        movedown = True
        direction = direction * -1
    for i in enemies:
        i.x += 5 * direction
        if movedown == True:
            i.y += 30
        for g in bullets:
            if g.colliderect(i):
                bullets.remove(g)
                enemies.remove(i)
                score += 1
                if score == 5:
                    Win()

pgzrun.go()