import random
import pgzrun
import time
strtTime=time.time()
WIDTH=400
HEIGHT=400
flowerList=[]
locList=[]
spriteList=["bigflower","smallflower","medflower"]
nextflower=0
loc1x=999
loc1y=999
loc2x=999
loc2y=999
end=False
for i in range(10):
    flower=Actor(random.choice(spriteList))
    x=random.randint(20,380)
    y=random.randint(20,380)
    flower.pos=(x,y)
    flowerList.append(flower)
def end1():
    global end
    end=True
def update():
    pass
def draw():
    x=1
    global loc1,loc2,strtTime,endTime
    screen.blit("grass",(0,0))
    for i in flowerList:
        i.draw()
        screen.draw.text(str(x),(i.x+15,i.y+15))
        x+=1
    for i in locList:
        screen.draw.line(i[0],i[1],"red")
    if nextflower<10:
        endTime=time.time()
        x=endTime-strtTime
        screen.draw.text(str(round(x,2)),(0,0))
    else:
        screen.draw.text(str(round(x,2)),(0,0))
        screen.draw.text("You Win",center=(200,200),fontsize=50,color="white")
        clock.unschedule(end1)
    if end:
        screen.fill("black")
        screen.draw.text("Gameover",center=(200,200),fontsize=50,color="white")
def on_mouse_down(pos):
    global nextflower,loc1x,loc1y,loc2x,loc2y,locList
    if flowerList[nextflower].collidepoint(pos):
        if nextflower>0:
            loc1x=flowerList[nextflower-1].x
            loc1y=flowerList[nextflower-1].y
            loc2x=flowerList[nextflower].x
            loc2y=flowerList[nextflower].y
            locList.append(((loc1x,loc1y),(loc2x,loc2y)))
        nextflower+=1
    else:
        nextflower=1
        locList=[]
clock.schedule(end1,15.0)
pgzrun.go()