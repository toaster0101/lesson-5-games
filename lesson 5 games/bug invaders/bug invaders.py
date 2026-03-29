import pgzrun
WIDTH=800
HEIGHT=500
bulletList=[]
posList=[]
ship=Actor("galaga")
ship.pos=(400,420)
bugList=[]
y=40
x=40
down=False
direction=1
bugRemoveList=[]
bulletRemoveList=[]
g=0
gameover=False
win=False
for i  in range(3):
    for j in range(6):
        bug=Actor("bug")
        bug.pos=(x,y)
        bugList.append(bug)
        x+=60
    y+=50
    x=40
def draw():
    screen.fill("black")
    ship.draw()
    for i in bugList:
        i.draw()
    for i in bulletList:
        i.draw()
    if gameover:
        screen.draw.text("Gameover",(0,0),color="white",fontsize=50)
        for i in bugList:
            i.pos=(99999,99999)
        ship.pos=(-9999,-9999)
    if win:
        screen.draw.text("You Win",(0,0),color="white",fontsize=50)
def update():
    global direction, g, gameover, win
    for i in bugRemoveList:
        if i in bugList:
            bugList.remove(i)
    for i in bulletRemoveList:
        if i in bulletList:
            bulletList.remove(i)
    if win==False:
        if ship.x<760:
            if keyboard.d:
                ship.x+=2
        if ship.x>40:
            if keyboard.a:
                ship.x-=2
        for i in bulletList:
            i.y-=4
            if i.y<0:
                bulletList.remove(i)
            for j in bugList:
                if i.colliderect(j):
                    bugRemoveList.append(j)
                    bulletRemoveList.append(i)
    if len(bugList)>0:
        for i in bugList:
            i.x+=1*direction
        for j in bugList:
            if bugList[g].x>760:
                direction=-1
                for i in bugList:
                    i.y+=10
            if bugList[g].x<40:
                direction=1
                for i in bugList:
                    i.y+=10
            g+=1
            if g>=len(bugList):
                g=0
    else:
        win=True
    for i in bugList:
        if ship.colliderect(i):
            gameover=True
def on_key_down(key):
    if win==False:
        if key==keys.SPACE:
            bullet=Actor("bullet")
            bullet.pos=(ship.x-1,ship.y-35)
            if len(bulletList)<5:
                bulletList.append(bullet)
            else:
                bulletList.pop(0)
                bulletList.append(bullet)
pgzrun.go()