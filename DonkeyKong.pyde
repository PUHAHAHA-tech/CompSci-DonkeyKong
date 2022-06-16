def setup():
    global start_s, rules_s, end_s, impact, walk1, walk11, Platform, ladder, donkey, counter, bar, princess, result, WorL, start
    start_s = loadImage("Start.PNG")
    rules_s = loadImage("Rules.PNG")
    end_s = loadImage("End.PNG")
    walk1 = loadImage("walk1.png")
    walk11 = loadImage("walk11.png")
    ladder = loadImage("ladder.jpg")
    donkey = loadImage("donkey.png")
    Platform = loadImage("Platform.PNG")
    bar = loadImage("bar.png")
    impact = createFont("impact.ttf", 64)
    counter = 0
    princess= loadImage("princess.png")
    textFont(impact)
    start = 0
    result = False
    #barrel1 variables
    global bx1, by1, bx_s1, by_s1
    bx1 = 160
    by1 = 145
    bx_s1 = 1
    WorL = 0
    by_s1 = 0
    #barrel2 variables
    global bx2, by2, bx_s2, by_s2
    bx2 = 200
    by2 = 145
    bx_s2 = 1
    by_s2 = 0
    size(800,600)
    
    start_s.resize(800,600)
    rules_s.resize(800,600)
    end_s.resize(800,600)
    walk1.resize(30,40)
    walk11.resize(30,40)
    donkey.resize(200,125)
    Platform.resize(800,15)
    ladder.resize(32,120)
    bar.resize(30,30)
    princess.resize(50,60)
    stroke(255)
    
    #player variables
    global xpos, ypos, Pxs, Pys, walk, face, down
    ypos = 580
    xpos = 40
    Pxs = 3
    Pys = 0
    walk = 0
    face = 1
    down = False
    
def draw():
    print(mouseX, mouseY)
    print(start)
    if start == 1:
        if result == True:
            if WorL == 1:
                textSize(64)
                fill(255,255,255)
                text("Congrats! You won!",150,300)
            elif WorL == 2:
                textSize(64)
                text("You lost!",300,300)
                textSize(20)
                text("Press [r] to restart the game", 300,400)
                fill(255,255,255)
        elif result == False:
            play()
    elif start == 0:
        image(start_s,0,0)
    elif start == 2:
        image(rules_s,0,0)
def mouseClicked():
    global start
        #start
    if mouseX > 320 and mouseX < 480 and mouseY > 340 and mouseY < 380:
        start = 1
    
    #rules
    if (mouseX > 350 and mouseX < 450 and mouseY > 440 and mouseY < 480 ):
        start = 2
    
    #return
    if (mouseX > 550 and mouseX < 660 and mouseY >500 and mouseY < 530):
        start = 0


def play():    
    game()
    Mario()
    gravity()
    wall()
    barrel()
    peach()

def peach():
    global result, WorL, ypos, xpos
    image(princess,308,113)
    if xpos <= 358 and ypos == 178:
        image(end_s,0,0)
        xpos = 40
        ypos = 580
        result = True
        WorL = 1 
        
def barrel():
    global bx1, by1, bx2, by2, bx_s1, bx_s2, WorL, result
    image(bar, bx1, by1)
    image(bar, bx2, by2)
    #first barrel
    if bx1 != 695:
        bx1+=bx_s1
    if bx1 == 695 and by1 <= 549:
        by1 += 7
    if by1 == 551:
        bx1 -= 2
    
    if (xpos ==bx1) and (ypos-10>= by1 >= ypos -49):
        WorL = 2
        result = True
    
    #second barrel 
    if bx2 != 500 and by2 == 145:
        bx2 += 1
    if bx2 == 500 and by2 <= 280:
        by2 += 7
    if by2 == 285:
        bx2 -= 1
    if bx2 == 300 and 415 >= by2 >= 285:
        by2 +=7
    if by2 == 418:
        bx2 +=1
    if bx2 == 580 and 545>= by2:
        by2 += 7
    if by2 == 551:
        bx2 -=1
    
    if by2 == 551 and bx2 == -30:
        bx2 = 200
        by2 = 145
    if by1 == 551 and bx1 == -30:
        bx1 = 160
        by1 = 145
        
    if (xpos ==bx2) and (ypos-10 >= by2 >= ypos-49):
        WorL = 2
        result = True
    
def game():
    global Platform, ladder, donkey
    fill(0)
    rect(0,0,800,600)
    image(Platform,0,580)
    image(ladder, 500, 460)
    image(Platform, -200, 445)
    image(ladder, 300, 325)
    image(Platform, 250, 310)
    image(Platform, -100, 175)
    image(ladder, 500,190)
    image(ladder, 700, 455)
    image(donkey, 0,50)

    
def wall():
    global xpos, ypos, Pxs, Pys
    if xpos >= 780:
        xpos = 780
    elif xpos <= 20:
        xpos = 20
    elif ypos >= 580:
        ypos = 580
        
def gravity():
    global xpos, ypos
    if 620 >= xpos >= 615 and 580>= ypos >= 444:
        ypos += 7
    if 240 <= xpos <= 245 and 440 >= ypos >= 308:
        ypos += 7
        if ypos == 441:
            ypos = 444
    if 720>= xpos >= 715 and 308 >= ypos >= 178:
        ypos += 7
        if ypos ==315:
            ypos = 308
        if ypos ==311:
            ypos = 308

def keyPressed():
    global Pys, Pxs, ypos, xpos, face, down, counter, bx1, bx2, by1, by2,result
    if counter == 0:
        if ypos == 444 or ypos == 308 or ypos == 178 or ypos == 580:
            if (key == ' '):
                ypos -= 45  
                counter = 3
    elif counter != 0:
        counter -=1
    if result == False:
        if (key == 'd'):
            if ypos == 580 or ypos == 444 or ypos == 308 or ypos == 178:
                xpos += Pxs
                image(walk1,xpos-20, ypos-40)
                face = 1
        if (key == 'a'):
            if ypos == 580 or ypos == 444 or ypos == 308 or ypos == 178:
                xpos -= Pxs 
                image(walk11,xpos-20, ypos-40)
                face = 0
        
        if (key == 'w'):
            #first ladder
            if 518 <= xpos <= 530 and 581 >= ypos >= 445:
                ypos -= 2
            #second ladder
            if 718 <= xpos <= 730 and 581>= ypos >= 310:
                ypos -= 2
            #third ladder
            if 319 <= xpos <= 328 and 446 >=ypos >= 310:
                ypos -= 2
            #fourth ladder
            if 520 <= xpos <= 526 and 310>= ypos >= 180:
                ypos -= 2
                
        if (key == 's'):
            #first ladder
            if 518 <= xpos <= 530 and 580 >= ypos >= 442:
                ypos += 2
            #second ladder
            if 718 <= xpos <= 730 and 580>= ypos >= 308:
                ypos += 2
            #third ladder
            if 319 <= xpos <= 328 and 444 >=ypos >= 308:
                ypos += 2
            #fourth ladder
            if 520 <= xpos <= 526 and 310>=ypos >= 178:
                ypos += 2
