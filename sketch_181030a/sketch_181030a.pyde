x=0
def setup():
    size(1350,700)
    global sat_img
    sat_img = loadImage("free.jpg")
    global tide_pod
    tide_pod = loadImage("tidepod.jpeg")
    global roblox
    roblox = loadImage("roblox.png")
    global e
    e = loadImage("e.jpg")
def draw():
    global x
    background(0,200,255)
    noStroke()
    RGB
    x+=1
    background(0,0,0)
    noStroke()
    #ground
    fill(50,100,0)
    rect(0,625,1350,75)
    fill(100,100,100)
    rect(570,625,210,140)
    #tombstones
    fill(211,211,211)
    rect(100,475,150,150)
    ellipse(175,470,150,150)
    rect(400,475,150,150)
    ellipse(475,470,150,150)
    rect(800,475,150,150)
    ellipse(875,470,150,150)
    rect(1100,475,150,150)
    ellipse(1175,470,150,150)
    #moon
    fill(255,255,255)
    ellipse(200,125,200,200)
    fill(0,0,0)
    ellipse(250,125,200,200)
    #sign
    fill(139,69,19)
    rect(1015,240,20,400)
    rect(850,80,350,300)

    noStroke()
    RGB
    
    #tide pod
    image(tide_pod, 120, 475, 110, 100)
    
    #roblox
    image(roblox, 800, 450, 150, 150)
    
    #e
    image(e, 1105, 450, 140, 140)
    
    #Body and legs
    fill(255,0,0)
    ellipse(500,400,300,300)
    
        
        
    
    
    fill(225,225,0)   
    rect(575,610,20,10) 
    fill(0,175,0)
    rect(575,600,20,10)
    fill(255,0,0)
    rect(575,500,20,100)
    fill(255,0,0)
    ellipse(585,620,20,10)
    rect(575,620,20,10)
    fill(0,0,0)
    rect(575,630,20,5)
    
    
    #Torso stuff
    fill(0,0,0)
    rect(300,225,350,100)
    fill(255,255,255)
    ellipse(500,425,200,100)
    fill(255,0,0)
    ellipse(500,400,200,100)
    #hair
    fill(255,0,0)
    stroke(0,0,0)
    triangle(421,300,401,300,401,400)
    triangle(431,300,411,300,411,400)
    triangle(568,300,588,300,588,400)
    triangle(578,300,598,300,598,400)
    #minus 32
    noStroke()

    #head
    fill(255,0,0)
    ellipse(500,310,200,200)
    #arms
    fill(255,0,0)
    rect(300,325,100,20)
    rect(600,325,100,20)
    rect(680,325,20,80)
    #hands
    fill(255,255,255)
    rect(675,405,30,10)
    ellipse(690,425,25,25)
    rect(696,420,5,35)
    rect(676,435,25,5)
    rect(673,425,5,15)
    #mouth
    fill(255,173,96)
    rect(425,300,150,20)
    ellipse(500,310,70,70)
    triangle(423,320,500,310,500,345)
    triangle(575,320,500,310,500,345)
    fill(255,0,0)
    fill(0,0,0)
    ellipse(500,300,10,10)
    #eyes
    fill(255,255,255)
    ellipse(445,270,50,50)
    ellipse(555,270,50,50)
    fill(0,0,0)
    ellipse(445,270,35,35)
    ellipse(555,270,35,35)
    fill(255,255,255)
    ellipse(458,260,10,10)
    ellipse(568,260,10,10)
    #lips
    stroke(0,0,0,40)
    line(520,320,480,320)
    line(520,320,530,315)
    line(480,320,470,315)
    line(530,315,545,315)
    line(470,315,455,315)
    textSize(40)
    text("Dead Meme", 900,120)
    text("Graveyard", 900,170)
    image(sat_img, 870, 178, 310, 190)

    if x%2==0:
        noStroke
        fill(255,0,0)
        rect(400,500,20,100)
        #Ankles
        fill(255,0,0)
        ellipse(410,600,20,10)
        ellipse(585,600,20,10)
        #Shoes
        fill(0,175,0)
        rect(400,600,20,10)
        fill(225,225,0)
        rect(400,610,20,10)
        fill(255,0,0)
        ellipse(410,620,20,10)
        rect(400,620,20,10)
        fill(0,0,0)
        rect(400,630,20,5)
        #arms
        fill(255,0,0)
        rect(300,265,20,80)
        fill(255,255,255)
        rect(295,255,30,10)
        ellipse(310,245,25,25)
        rect(296,220,5,35)
        rect(296,230,26,5)
        rect(322,230,5,15)
        
        
        
    elif x%2==1:
        noStroke
        fill(255,0,0)
        
        rect(300,325,20,80)
        
        rect(400,500,20,70)
        rect(350,570,70,20)
        fill(0,175,0)
        rect(340,570,10,20)
        fill(225,225,0)
        rect(330,570,10,20)
        fill(255,0,0)
        ellipse(330,580,10,20)
        rect(320,570,10,20)
        fill(0,0,0)
        rect(315,570,5,20)
        fill(255,255,255)
        rect(295,405,30,10)
        ellipse(310,425,25,25)
        rect(296,420,5,35)
        rect(296,435,26,5)
        rect(322,425,5,15)
    else:
        rect(400,500,20,70)
    ellipse (600,200,30,30)
    ellipse(570,230,20,20)
    ellipse(700,150,200,100)
    fill(0,0,0)
    textSize(18)
    text("Im not a dead meme!",603,150)
    delay(300)
