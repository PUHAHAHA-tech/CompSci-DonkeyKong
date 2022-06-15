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
