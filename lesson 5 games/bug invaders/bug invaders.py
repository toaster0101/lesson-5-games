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
for i in range(3):
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
def update():
    global down
    down=False
    if ship.x<560:
        if keyboard.d:
            ship.x+=2
    if ship.x>40:
        if keyboard.a:
            ship.x-=2
    for i in bulletList:
        i.y-=2
        if i.y<0:
            bulletList.remove(i)
    if bugList[-1].x<720:
        for i in bugList:
            i.x+=2
    elif bugList[-1].x>710:
        down=True
def on_key_down(key):
    if key==keys.SPACE:
        bullet=Actor("bullet")
        bullet.pos=(ship.x-1,ship.y-35)
        if len(bulletList)<10:
            bulletList.append(bullet)
        else:
            bulletList.pop(0)
            bulletList.append(bullet)
pgzrun.go()