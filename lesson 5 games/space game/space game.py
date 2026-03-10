import random
import pgzrun
WIDTH=400
HEIGHT=400
satList=[]
locList=[]
i=0
loc1x=999
loc1y=999
loc2x=999
loc2y=999
for i in range(10):
    sat=Actor("satellite")
    x=random.randint(20,380)
    y=random.randint(20,380)
    sat.pos=(x,y)
    satList.append(sat)
def draw():
    x=1
    global loc1,loc2
    screen.blit("background",(0,0))
    for i in satList:
        i.draw()
        screen.draw.text(str(x),(i.x+15,i.y+15))
        x+=1
    for i in locList:
        screen.draw.line(i[0],i[1],"red")
def on_mouse_down(pos):
    global i,loc1x,loc1y,loc2x,loc2y,locList
    if satList[i].collidepoint(pos):
        if i>0:
            loc1x=satList[i-1].x
            loc1y=satList[i-1].y
            loc2x=satList[i].x
            loc2y=satList[i].y
            locList.append(((loc1x,loc1y),(loc2x,loc2y)))
        i+=1
    else:
        i=1
        locList=[]
pgzrun.go()