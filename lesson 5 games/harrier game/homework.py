import random
import pgzrun
WIDTH=400
HEIGHT=400
harrier=Actor("harrier side")
harrier.pos=(200,200)
harrier2=Actor("harrier top")
harrier2.pos=(9999,9999)
a4=Actor("a-4")
a4.pos=(999,999)
aim9=Actor("aim9x")
aim9.pos=(100,300)
ammo=0
phase2=False
score=0
gameover=False
clicked=False
def draw():
    screen.blit("ground",(0,0))
    harrier.draw()
    aim9.draw()
    harrier2.draw()
    a4.draw()
    screen.draw.text("Ammo="+str(ammo),(0,380))
    if phase2:
        harrier.x=999999999
        harrier.y=999999999
    if gameover:
        harrier2.x=999999
        harrier2.y=999999
        a4.x=99999
        a4.y=-99999
        aim9.x=9999999
        aim9.y=9999999
        screen.fill("black")
        screen.draw.text("End of game, score="+str(score),(0,0))
def update():
    global clicked,gameover,ammo
    if keyboard.space:
        if phase2:
            if ammo!=0:
                aim9.x=harrier2.x
                aim9.y=300
                clicked=True
            else:
                gameover=True
    if keyboard.w:
        if phase2:
            1
        else:
            harrier.y-=1
    if keyboard.s:
        if phase2:
            1
        else:
            harrier.y+=1
    if keyboard.d:
        if phase2:
            harrier2.image="harrier right"
            harrier2.x+=1
        else:
            harrier.image="harrier side"
            harrier.x+=1
    elif not keyboard.a and not keyboard.d:
        harrier2.image="harrier top"
    if keyboard.a:
        if phase2:
            harrier2.image="harrier left"
            harrier2.x-=1
        else:
            harrier.image="harrier side_mirror"
            harrier.x-=1
    elif not keyboard.a and not keyboard.d:
        harrier2.image="harrier top"
    if harrier.colliderect(aim9):
        x=random.randint(0,336)
        y=random.randint(0,336)
        aim9.y=y
        aim9.x=x
        ammo+=1
def movement():
    global clicked,ammo,score,gameover
    if clicked:
        aim9.y-=15
        if aim9.colliderect(a4):
            aim9.x=999
            aim9.y=999
            score+=1
            x=random.randint(0,336)
            a4.y=-20
            a4.x=x
            clicked=False
            ammo-=1
        if aim9.y<=-30:
            clicked=False
            ammo-=1
    if phase2:
        a4.y+=2.5
        if a4.colliderect(harrier2):
            gameover=True
        if a4.y>=400:
            gameover=True
def timer():
    global phase2
    phase2=True
    harrier2.x=200
    harrier2.y=300
    aim9.x=99999
    aim9.y=99999
    a4.x=100
    a4.y=-20
def gameover1():
    global gameover
    gameover=True
clock.schedule(timer,15.0)
clock.schedule(gameover1,60.0)
clock.schedule_interval(movement,0.05)
pgzrun.go()