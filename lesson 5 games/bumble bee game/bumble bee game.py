import random
import pgzrun
WIDTH=400
HEIGHT=400
bee=Actor("bee")
bee.pos=(50,50)
flower=Actor("flower")
flower.pos=(200,300)
score=0
gameover=False
def draw():
    screen.blit("background",(0,0))
    bee.draw()
    flower.draw()
    screen.draw.text("Score="+str(score),(0,0))
    if gameover:
        screen.fill("black")
        screen.draw.text("Gameover, Score="+str(score),center=(200,100),fontsize=50)
        bee.x=999999999999999999999999
        bee.y=999999999999999999999999
def update():
    global score,bee
    if keyboard.w:
        bee.y-=1
    if keyboard.s:
        bee.y+=1
    if keyboard.d:
        bee.image="bee"
        bee.x+=1
    if keyboard.a:
        bee.image="bee_mirror"
        bee.x-=1
    if bee.colliderect(flower):
        x=random.randint(0,336)
        y=random.randint(0,336)
        flower.y=y
        flower.x=x
        score+=1
def timer():
    global gameover
    gameover=True
clock.schedule(timer,30.0)
pgzrun.go()