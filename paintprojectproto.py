#Paint Program .py
from pygame import *
import pygame.font
from glob import *
from random import *


#======================Surfaces===================================
res = maxx,maxy = 1024,768 #Window resolution
screen = display.set_mode(res) #Sets window

#=====================Loading Assets==========================

#Grabs paint background and blits it.
bg = image.load("assets/background.png")
screen.blit(bg,(0,0))

pygame.font.init() #initializes font module
arialFont = pygame.font.SysFont("Arial", 19) #chooses font
    
mixer.init() #Initializes music mixer
mixer.music.load("assets/theme.mp3") #Loads theme song
mixer.music.play() #Plays theme song.

#Loading tool images.
penblank = image.load("assets/pencilblank.png")
penselect= image.load("assets/pencilhighlight.png")
penclick = image.load("assets/pencilselect.png")
sprayblank = image.load("assets/sprayblank.png")
sprayselect= image.load("assets/sprayhighlight.png")
sprayclick= image.load("assets/sprayselect.png")
eraserblank = image.load("assets/eraserblank.png")
eraserselect = image.load("assets/eraserhighlight.png")
eraserclick = image.load("assets/eraserselect.png")
dropblank = image.load("assets/dropperblank.png")
dropselect = image.load("assets/dropperhighlight.png")
dropclick = image.load("assets/dropperselect.png")
rectblank = image.load("assets/rectblank.png")
rectselect = image.load("assets/recthighlight.png")
rectclick = image.load("assets/rectselect.png")
textblank = image.load("assets/textblank.png")
textselect = image.load("assets/texthighlight.png")
textclick = image.load("assets/textselect.png")
ellipblank = image.load("assets/ellipseblank.png")
ellipselect = image.load("assets/ellipsehighlight.png")
ellipclick = image.load("assets/ellipseselect.png")
lineblank = image.load("assets/lineblank.png")
lineselect = image.load("assets/linehighlight.png")
lineclick = image.load("assets/lineselect.png")

#Load stamps and selection images
marioblit=image.load("assets/marioblit.png")
marioblank=image.load("assets/marioblank.png")
marioselect=image.load("assets/mariohighlight.png")
marioclick=image.load("assets/marioselect.png")
luigiblit=image.load("assets/luigiblit.png")
luigiblank=image.load("assets/luigiblank.png")
luigiselect=image.load("assets/luigihighlight.png")
luigiclick=image.load("assets/luigiselect.png")
mushroomblit=image.load("assets/mushroomblit.png")
mushroomblank=image.load("assets/mushroomblank.png")
mushroomselect=image.load("assets/mushroomhighlight.png")
mushroomclick=image.load("assets/mushroomselect.png")
fireflowerblit=image.load("assets/fireflowerblit.png")
fireflowerblank=image.load("assets/fireflowerblank.png")
fireflowerselect=image.load("assets/fireflowerhighlight.png")
fireflowerclick=image.load("assets/fireflowerselect.png")
upblit=image.load("assets/1upblit.png")
upblank=image.load("assets/1upblank.png")
upselect=image.load("assets/1uphighlight.png")
upclick=image.load("assets/1upselect.png")
starmanblit=image.load("assets/starmanblit.png")
starmanblank=image.load("assets/starmanblank.png")
starmanselect=image.load("assets/starmanhighlight.png")
starmanclick=image.load("assets/starmanselect.png")

#Loads backgrounds
blank=image.load("assets/blank.png")
sm64=image.load("assets/sm64.png")
sms=image.load("assets/sms.png")
smg=image.load("assets/smg.png")

#Loads images for volume.
volon = image.load("assets/volon.png")
voloff = image.load("assets/voloff.png")

#Loads images for open/save.
saveblank=image.load("assets/saveblank.png")
saveselect=image.load("assets/savehighlight.png")
saveclick=image.load("assets/saveselect.png")
openblank=image.load("assets/openblank.png")
openselect=image.load("assets/openhighlight.png")
openclick=image.load("assets/openselect.png")

#================Program Start Defaults=========================

size = 10 #Size for most tools
spraysize = 5 #Size for spray tool
tool = "" #No tools on at start
col = (0,0,0) #Default start color is black
blk=(0,0,0)#Black color for text
copy = screen.copy() #Grabs screen
textrun =True #Flag for text tool
vol = True #Flag for sound
canvasRect = Rect(172,112,701,484) #Rect for drawing canvas.
    
#=====================MAIN LOOP=============================

running = True
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False
        if evt.type==MOUSEBUTTONDOWN:
            ox,oy=mx,my #Gets mouse coords at time of click
            copy=screen.copy() #Grabs image of screen
            if evt.button==4: #Scroll up
                size+=5
                spraysize+=5
            if evt.button==5: #Scroll down
                size-=5     
                spraysize-=5
                
    mx, my = mouse.get_pos() #mouse coordinates and
    mb = mouse.get_pressed() #buttons pressed

    if tool == "": #startup caption
        display.set_caption("Left click speakers to pause/play music, and scroll mouse wheel to change tool size.") #opening instructions
    
    #Sizes for tools and spraycan    
    if size >= 100:
        size = 100
    if size <= 1:
        size = 1
    if spraysize >= 100:
        spraysize = 100
    if spraysize <= 1:
        spraysize = 1
    
#===================Rectangular Hitboxes====================

    #Creates Rectangular hitboxes for collidepoint and opening/saving.
    saveRect=Rect(0,0,93,27)
    openRect=Rect(97,0,95,27)
    
    #Creates Rectangular hitboxes for collidepoint and using tools.
    volRect = Rect(995,0,27,27)
    penRect= Rect(6,121,72,99)
    sprayRect= Rect(93,121,72,99)
    eraserRect = Rect(6,245,72,99)
    dropRect=Rect(92,245,72,99)
    rectRect = Rect(6,367,72,99)
    textRect = Rect(93,367,72,99)
    ellipRect = Rect(7,491,72,99)
    lineRect = Rect(93,491,72,99)

    #Creates Rectangular hitboxes for collidepoint and using stamps.
    marioRect=Rect(276,624,106,106)
    luigiRect=Rect(396,624,106,106)
    mushroomRect=Rect(517,624,106,106)
    fireflowerRect=Rect(638,624,106,106)
    starmanRect=Rect(759,624,106,106)
    upRect=Rect(881,624,106,106)

    #Creates Rectangular hitboxes for collidepoint and choosing backgrounds.
    blankRect=Rect(875,112,147,117)
    sm64Rect=Rect(875,232,147,117)
    smsRect=Rect(875,353,147,117)
    smgRect=Rect(875,474,147,117)    

#=====================Tool/Stamp Parameters=====================

    #If tools are hovered over, gray image is blitted,
    #and on click orange selection image is blitted.
    if penRect.collidepoint(mx,my) and tool!= "pencil":
        screen.blit(penselect,(6,121))
    if penRect.collidepoint(mx,my) and mb[0]==1 and tool!="pencil":
        tool = "pencil"
        screen.blit(penclick,(6,121))
        
    if sprayRect.collidepoint(mx,my) and tool != "spraycan":
        screen.blit(sprayselect,(93,121))
    if sprayRect.collidepoint(mx,my) and mb[0]==1 and tool != "spraycan":
        tool = "spraycan"
        screen.blit(sprayclick,(93,121))
        
    if eraserRect.collidepoint(mx,my) and tool!= "eraser":
        screen.blit(eraserselect,(6,245))
    if eraserRect.collidepoint(mx,my) and mb[0]==1 and tool != "eraser":
        tool = "eraser"
        screen.blit(eraserclick,(6,245))

    if dropRect.collidepoint(mx,my) and tool != "drop":
        screen.blit(dropselect,(92,245))
    if dropRect.collidepoint(mx,my) and mb[0]==1 and tool != "drop":
        tool="drop"
        screen.blit(dropclick,(92,245))
    
    if rectRect.collidepoint(mx,my) and tool!= "rect":
        screen.blit(rectselect,(6,367))
    if rectRect.collidepoint(mx,my) and mb[0]==1 and tool != "rect":
        tool = "rect"
        screen.blit(rectclick,(6,367))

    if textRect.collidepoint(mx,my) and tool != "text":
        screen.blit(textselect,(93,367))
    if textRect.collidepoint(mx,my) and mb[0]==1 and tool != "text":
        tool="text"
        screen.blit(textclick,(93,367))

    if ellipRect.collidepoint(mx,my) and tool!="ellip":
        screen.blit(ellipselect,(7,491))
    if ellipRect.collidepoint(mx,my) and mb[0]==1 and tool != "ellip":
        tool="ellip"
        screen.blit(ellipclick,(7,491))

    if lineRect.collidepoint(mx,my) and tool!= "line":
        screen.blit(lineselect,(93,491))
    if lineRect.collidepoint(mx,my) and mb[0]==1 and tool != "line":
        tool = "line"
        screen.blit(lineclick,(93,491))

    if marioRect.collidepoint(mx,my) and tool!= "mario":
        screen.blit(marioselect,(276,624))
    if marioRect.collidepoint(mx,my) and mb[0]==1 and tool!= "mario" :
        tool = "mario"
        screen.blit(marioclick,(276,624))

    if luigiRect.collidepoint(mx,my) and tool!= "luigi":
        screen.blit(luigiselect,(396,624))
    if luigiRect.collidepoint(mx,my) and mb[0]==1 and tool!= "luigi" :
        tool = "luigi"
        screen.blit(luigiclick,(396,624))

    if mushroomRect.collidepoint(mx,my) and tool!= "mushroom":
        screen.blit(mushroomselect,(517,624))
    if mushroomRect.collidepoint(mx,my) and mb[0]==1 and tool!= "mushroom" :
        tool = "mushroom"
        screen.blit(mushroomclick,(517,624))

    if fireflowerRect.collidepoint(mx,my) and tool!= "fireflower":
        screen.blit(fireflowerselect,(638,624))
    if fireflowerRect.collidepoint(mx,my) and mb[0]==1 and tool!= "fireflower" :
        tool = "fireflower"
        screen.blit(fireflowerclick,(638,624))

    if starmanRect.collidepoint(mx,my) and tool!= "starman":
        screen.blit(starmanselect,(759,624))
    if starmanRect.collidepoint(mx,my) and mb[0]==1 and tool!= "starman" :
        tool = "starman"
        screen.blit(starmanclick,(759,624))
        
    if upRect.collidepoint(mx,my) and tool!= "1up":
        screen.blit(upselect,(881,624))
    if upRect.collidepoint(mx,my) and mb[0]==1 and tool!= "1up" :
        tool = "1up"
        screen.blit(upclick,(881,624))

#=====================Show tool selection======================

    #Checks which tools are not hovered over or selected to display that they are off.
    if penRect.collidepoint(mx,my)==False and sprayRect.collidepoint(mx,my)== False and eraserRect.collidepoint(mx,my)==False and dropRect.collidepoint(mx,my)==False and rectRect.collidepoint(mx,my)==False and textRect.collidepoint(mx,my)==False and ellipRect.collidepoint(mx,my)==False and lineRect.collidepoint(mx,my)==False and marioRect.collidepoint(mx,my)==False and luigiRect.collidepoint(mx,my)==False and mushroomRect.collidepoint(mx,my)==False and fireflowerRect.collidepoint(mx,my)==False and starmanRect.collidepoint(mx,my)==False and upRect.collidepoint(mx,my)==False:
        if tool=="pencil":
            screen.blit(sprayblank,(93,121))
            screen.blit(eraserblank,(6,245))
            screen.blit(dropblank,(92,245))
            screen.blit(rectblank,(6,367))
            screen.blit(textblank,(93,367))
            screen.blit(ellipblank,(7,491))
            screen.blit(lineblank,(93,491))
            screen.blit(marioblank,(276,624))
            screen.blit(luigiblank,(396,624))
            screen.blit(mushroomblank,(517,624))
            screen.blit(fireflowerblank,(638,624))
            screen.blit(starmanblank,(759,624))
            screen.blit(upblank,(881,624))
        elif tool=="spraycan":
            screen.blit(penblank,(6,121))
            screen.blit(eraserblank,(6,245))
            screen.blit(dropblank,(92,245))
            screen.blit(rectblank,(6,367))
            screen.blit(textblank,(93,367))
            screen.blit(ellipblank,(7,491))
            screen.blit(lineblank,(93,491))
            screen.blit(marioblank,(276,624))
            screen.blit(luigiblank,(396,624))
            screen.blit(mushroomblank,(517,624))
            screen.blit(fireflowerblank,(638,624))
            screen.blit(starmanblank,(759,624))
            screen.blit(upblank,(881,624))
        elif tool=="eraser":
            screen.blit(penblank,(6,121))
            screen.blit(sprayblank,(93,121))
            screen.blit(dropblank,(92,245))
            screen.blit(rectblank,(6,367))
            screen.blit(textblank,(93,367))
            screen.blit(ellipblank,(7,491))
            screen.blit(lineblank,(93,491))
            screen.blit(marioblank,(276,624))
            screen.blit(luigiblank,(396,624))
            screen.blit(mushroomblank,(517,624))
            screen.blit(fireflowerblank,(638,624))
            screen.blit(starmanblank,(759,624))
            screen.blit(upblank,(881,624))
        elif tool=="drop":
            screen.blit(penblank,(6,121))
            screen.blit(sprayblank,(93,121))
            screen.blit(eraserblank,(6,245))
            screen.blit(rectblank,(6,367))
            screen.blit(textblank,(93,367))
            screen.blit(ellipblank,(7,491))
            screen.blit(lineblank,(93,491))
            screen.blit(marioblank,(276,624))
            screen.blit(luigiblank,(396,624))
            screen.blit(mushroomblank,(517,624))
            screen.blit(fireflowerblank,(638,624))
            screen.blit(starmanblank,(759,624))
            screen.blit(upblank,(881,624))
        elif tool=="rect":
            screen.blit(penblank,(6,121))
            screen.blit(sprayblank,(93,121))
            screen.blit(eraserblank,(6,245))
            screen.blit(dropblank,(92,245))
            screen.blit(textblank,(93,367))
            screen.blit(ellipblank,(7,491))
            screen.blit(lineblank,(93,491))
            screen.blit(marioblank,(276,624))
            screen.blit(luigiblank,(396,624))
            screen.blit(mushroomblank,(517,624))
            screen.blit(fireflowerblank,(638,624))
            screen.blit(starmanblank,(759,624))
            screen.blit(upblank,(881,624))
        elif tool=="text":
            screen.blit(penblank,(6,121))
            screen.blit(sprayblank,(93,121))
            screen.blit(eraserblank,(6,245))
            screen.blit(dropblank,(92,245))
            screen.blit(rectblank,(6,367))
            screen.blit(ellipblank,(7,491))
            screen.blit(lineblank,(93,491))
            screen.blit(marioblank,(276,624))
            screen.blit(luigiblank,(396,624))
            screen.blit(mushroomblank,(517,624))
            screen.blit(fireflowerblank,(638,624))
            screen.blit(starmanblank,(759,624))
            screen.blit(upblank,(881,624))
        elif tool=="ellip":
            screen.blit(penblank,(6,121))
            screen.blit(sprayblank,(93,121))
            screen.blit(eraserblank,(6,245))
            screen.blit(dropblank,(92,245))
            screen.blit(rectblank,(6,367))
            screen.blit(textblank,(93,367))
            screen.blit(lineblank,(93,491))
            screen.blit(marioblank,(276,624))
            screen.blit(luigiblank,(396,624))
            screen.blit(mushroomblank,(517,624))
            screen.blit(fireflowerblank,(638,624))
            screen.blit(starmanblank,(759,624))
            screen.blit(upblank,(881,624))
        elif tool=="line":
            screen.blit(penblank,(6,121))
            screen.blit(sprayblank,(93,121))
            screen.blit(eraserblank,(6,245))
            screen.blit(dropblank,(92,245))
            screen.blit(rectblank,(6,367))
            screen.blit(textblank,(93,367))
            screen.blit(ellipblank,(7,491))
            screen.blit(marioblank,(276,624))
            screen.blit(luigiblank,(396,624))
            screen.blit(mushroomblank,(517,624))
            screen.blit(fireflowerblank,(638,624))
            screen.blit(starmanblank,(759,624))
            screen.blit(upblank,(881,624))
        elif tool=="mario":
            screen.blit(penblank,(6,121))
            screen.blit(sprayblank,(93,121))
            screen.blit(eraserblank,(6,245))
            screen.blit(dropblank,(92,245))
            screen.blit(rectblank,(6,367))
            screen.blit(textblank,(93,367))
            screen.blit(ellipblank,(7,491))
            screen.blit(lineblank,(93,491))
            screen.blit(luigiblank,(396,624))
            screen.blit(mushroomblank,(517,624))
            screen.blit(fireflowerblank,(638,624))
            screen.blit(starmanblank,(759,624))
            screen.blit(upblank,(881,624))
        elif tool=="luigi":
            screen.blit(penblank,(6,121))
            screen.blit(sprayblank,(93,121))
            screen.blit(eraserblank,(6,245))
            screen.blit(dropblank,(92,245))
            screen.blit(rectblank,(6,367))
            screen.blit(textblank,(93,367))
            screen.blit(ellipblank,(7,491))
            screen.blit(lineblank,(93,491))
            screen.blit(marioblank,(276,624))
            screen.blit(mushroomblank,(517,624))
            screen.blit(fireflowerblank,(638,624))
            screen.blit(starmanblank,(759,624))
            screen.blit(upblank,(881,624))
        elif tool=="mushroom":
            screen.blit(penblank,(6,121))
            screen.blit(sprayblank,(93,121))
            screen.blit(eraserblank,(6,245))
            screen.blit(dropblank,(92,245))
            screen.blit(rectblank,(6,367))
            screen.blit(textblank,(93,367))
            screen.blit(ellipblank,(7,491))
            screen.blit(lineblank,(93,491))
            screen.blit(marioblank,(276,624))
            screen.blit(luigiblank,(396,624))
            screen.blit(fireflowerblank,(638,624))
            screen.blit(starmanblank,(759,624))
            screen.blit(upblank,(881,624))
        elif tool=="fireflower":
            screen.blit(penblank,(6,121))
            screen.blit(sprayblank,(93,121))
            screen.blit(eraserblank,(6,245))
            screen.blit(dropblank,(92,245))
            screen.blit(rectblank,(6,367))
            screen.blit(textblank,(93,367))
            screen.blit(ellipblank,(7,491))
            screen.blit(lineblank,(93,491))
            screen.blit(marioblank,(276,624))
            screen.blit(luigiblank,(396,624))
            screen.blit(mushroomblank,(517,624))
            screen.blit(starmanblank,(759,624))
            screen.blit(upblank,(881,624))
        elif tool=="starman":
            screen.blit(penblank,(6,121))
            screen.blit(sprayblank,(93,121))
            screen.blit(eraserblank,(6,245))
            screen.blit(dropblank,(92,245))
            screen.blit(rectblank,(6,367))
            screen.blit(textblank,(93,367))
            screen.blit(ellipblank,(7,491))
            screen.blit(lineblank,(93,491))
            screen.blit(marioblank,(276,624))
            screen.blit(luigiblank,(396,624))
            screen.blit(mushroomblank,(517,624))
            screen.blit(fireflowerblank,(638,624))
            screen.blit(upblank,(881,624))
        elif tool=="1up":
            screen.blit(penblank,(6,121))
            screen.blit(sprayblank,(93,121))
            screen.blit(eraserblank,(6,245))
            screen.blit(dropblank,(92,245))
            screen.blit(rectblank,(6,367))
            screen.blit(textblank,(93,367))
            screen.blit(ellipblank,(7,491))
            screen.blit(lineblank,(93,491))
            screen.blit(marioblank,(276,624))
            screen.blit(luigiblank,(396,624))
            screen.blit(mushroomblank,(517,624))
            screen.blit(fireflowerblank,(638,624))
            screen.blit(starmanblank,(759,624))
        else:
            screen.blit(penblank,(6,121))
            screen.blit(sprayblank,(93,121))
            screen.blit(eraserblank,(6,245))
            screen.blit(dropblank,(92,245))
            screen.blit(rectblank,(6,367))
            screen.blit(textblank,(93,367))
            screen.blit(ellipblank,(7,491))
            screen.blit(lineblank,(93,491))
            screen.blit(marioblank,(276,624))
            screen.blit(luigiblank,(396,624))
            screen.blit(mushroomblank,(517,624))
            screen.blit(fireflowerblank,(638,624))
            screen.blit(starmanblank,(759,624))
            screen.blit(upblank,(881,624))

    #Check to see if open/save buttons are used.
    if saveRect.collidepoint(mx,my)==False:
        screen.blit(saveblank,(0,0))
    elif saveRect.collidepoint(mx,my):
        screen.blit(saveselect,(0,0))
    elif saveRect.collidepoint(mx,my) and mb[0]==1:
        screen.blit(saveclick,(0,0))
        
    if openRect.collidepoint(mx,my)==False:
        screen.blit(openblank,(97,0))
    elif openRect.collidepoint(mx,my):
        screen.blit(openselect,(97,0))
    elif openRect.collidepoint(mx,my) and mb[0]==1:
        screen.blit(openclick,(97,0))
    

#======================Color Wheel=======================                

    #Gets color from clicking within the circle of the colorwheel image.
    if mb[0]==1 and (((mx-78)**2+(my-682)**2)**0.5)<78 :
        col = screen.get_at((mx,my))
        
#=====================Backgrounds==========================

    #Clicking on each of the four backgrounds blits them to the canvas.
    if blankRect.collidepoint(mx,my) and mb[0]==1:
        screen.blit(blank,(172,112))
    elif sm64Rect.collidepoint(mx,my) and mb[0]==1:
        screen.blit(sm64,(172,112))
    elif smsRect.collidepoint(mx,my) and mb[0]==1:
        screen.blit(sms,(172,112))
    elif smgRect.collidepoint(mx,my) and mb[0]==1:
        screen.blit(smg,(172,112))
        
#=====================Volume Control=======================

    #Clicking on speaker icon in top right turns music on and off.    
    if vol == True and volRect.collidepoint(mx,my) and mb[0]==1: #checks for click and if on
        mixer.music.pause() #pauses
        screen.blit(voloff,(995,0))
        vol = False #set flag for off
        time.wait(350)
        
    elif vol == False and volRect.collidepoint(mx,my) and mb[0] ==1: #checks for click and if music is off
        mixer.music.play() #plays
        screen.blit(volon,(995,0))
        vol=True #set flag on
        time.wait(350)
        
#============================Tools===============================
        
    #Pencil
    if tool=="pencil": #check for tool, and if canvas is clicked
        display.set_caption("Pencil - Left click to draw with selected color.")
        if canvasRect.collidepoint(mx,my) and mb[0]==1:
            screen.set_clip(canvasRect) #clips to canvas
            draw.line(screen,col,(ox,oy),(mx,my),size) #draws line
            screen.set_clip(None) #clip finishes
            ox,oy=mx,my #sets line start again

    #Spraycan
    if tool=="spraycan":
        display.set_caption("Spraycan - Left click to spray with selected color.")
        if canvasRect.collidepoint(mx,my) and mb[0]==1:
            screen.set_clip(canvasRect)
            x = randint(mx-spraysize,mx+spraysize) #creates random x-coordinate and
            y = randint(my-spraysize,my+spraysize) #random y-coordinate 
            x2 = randint(mx-spraysize,mx+spraysize) 
            y2 = randint(my-spraysize,my+spraysize) 
            x3 = randint(mx-spraysize,mx+spraysize) 
            y3 = randint(my-spraysize,my+spraysize)
            x4 = randint(mx-spraysize,mx+spraysize) 
            y4 = randint(my-spraysize,my+spraysize)
            x5 = randint(mx-spraysize,mx+spraysize) 
            y5 = randint(my-spraysize,my+spraysize)#there are this many so the spray can distinctly sprays a circle 
            if ((mx-x)**2+(my-y)**2)**0.5 < spraysize and ((mx-x2)**2+(my-y2)**2)**0.5 < spraysize and ((mx-x3)**2+(my-y3)**2)**0.5 < spraysize and ((mx-x4)**2+(my-y4)**2)**0.5 < spraysize and ((mx-x5)**2+(my-y5)**2)**0.5 < spraysize: #checks for radius of spray so it is a circle
                draw.circle(screen,col,(x,y),0) #each sprays a speck as part of whole circle
                draw.circle(screen,col,(x2,y2),0)
                draw.circle(screen,col,(x3,y3),0)
                draw.circle(screen,col,(x4,y4),0)
                draw.circle(screen,col,(x5,y5),0)
            screen.set_clip(None)

    #Eraser
    if tool=="eraser":
        display.set_caption("Eraser - Left click to erase the canvas.")
        if canvasRect.collidepoint(mx,my) and mb[0]==1:
            screen.set_clip(canvasRect)
            draw.circle(screen,(255,255,255),(mx,my),size) #draws white eraser
            screen.set_clip(None)
        
    #Color Dropper
    if tool=="drop":
        display.set_caption("Color Dropper - Left click to select any color on canvas.")
        if canvasRect.collidepoint(mx,my) and mb[0]==1:
            screen.set_clip(canvasRect)
            col = screen.get_at((mx,my)) #grabs color in canvas
            screen.set_clip(None)

    #Rectangle
    if tool=="rect":
        display.set_caption("Rectangle - Left clicked for unfilled rectangle, right click for filled rectangle.")
        if mb[0]==1 and canvasRect.collidepoint(mx,my):
            screen.blit(copy ,(0,0)) #blits screen at press of mouse button to see where shape is made
            rectsize = Rect(ox,oy,mx-ox,my-oy) #top left coordinates, height and width from mouse
            screen.set_clip(canvasRect)
            draw.rect(screen,col,rectsize,size) #draws rectangle as per rectsize
            screen.set_clip(None)
        if mb[2]==1 and canvasRect.collidepoint(mx,my):
            screen.blit(copy ,(0,0)) 
            rectsize = Rect(ox,oy,mx-ox,my-oy)
            screen.set_clip(canvasRect)
            draw.rect(screen,col,rectsize)
            screen.set_clip(None)

    #Text
    def typetext(): #Function to write text to a picture
            bg = screen.copy() #grabs current screen
            text = "" #string for output
            
            textArea = Rect(172,112,200,25) #typing area
            pics = glob("*.bmp")+glob("*.jpg")+glob("*.png")
            area = len(pics)
            
            typeArea = Rect(textArea.x,textArea.y+textArea.height,textArea.width,area*textArea.height) #area for typing

            typing = True
            while typing:
                for etxt in event.get():
                    if etxt.type == QUIT:
                        event.post(e.txt) #quits main loop
                        return ""
                    if etxt.type == KEYDOWN:
                        if etxt.key == K_BACKSPACE: #for backspacing
                            if len(text)>0:
                                text = text[:-1]
                        elif etxt.key == K_KP_ENTER or etxt.key == K_RETURN : 
                            typing = False
                        elif etxt.key < 256:
                            text += etxt.unicode #add text to be displayed
                        
                txtPic = arialFont.render(text,True,col) #renders font as picture
                draw.rect(screen,(204,211,255),textArea)
                draw.rect(screen,(0,0,0),textArea,2)
                screen.blit(txtPic,(textArea.x+3,textArea.y+2))
            
                display.flip()
            
            screen.blit(bg,(0,0)) #blits background to remove typing area
            return text

    if tool =="text" and canvasRect.collidepoint(mx,my):
        pygame.font.init()
        message = ""

        #textrun to set captions for user instruction
        if textrun==True:
            display.set_caption("Text - Right Click to open type box.")

        if textrun==False:
            display.set_caption("Left Click to display text, Right Click to open type box again.")
        
        if canvasRect.collidepoint(mx,my) and mb[2]==1:
            display.set_caption("Press Enter when finished")
            txt = typetext() #call text function
            txtPic = arialFont.render(txt, True, col) #makes picture of text
            w,h = (txtPic.get_width()//2, txtPic.get_height()//2) #gets center of txtPic
            textrun=False
        
        if canvasRect.collidepoint(mx,my) and mb[0]==1 and textrun==False:
            screen.blit(copy ,(0,0))
            screen.set_clip(canvasRect)
            screen.blit(txtPic,(mx-w,my-h)) #blits txtPic at mouse
            screen.set_clip(None)
        
    #Line
    if tool =="line":
        display.set_caption("Line - Right Click to draw line from two points.")
        if canvasRect.collidepoint(mx,my) and mb[0]==1:
            screen.blit(copy,(0,0)) #blits screen at press of mouse button to see where shape is made
            screen.set_clip(canvasRect)
            draw.line(screen,col,(ox,oy),(mx,my),size) #draws line
            screen.set_clip(None)
    
    #Ellipse
    if tool == "ellip":
        display.set_caption("Ellipse - Left clicked for unfilled ellipse, right click for filled ellipse.")
        if canvasRect.collidepoint(mx,my) and mb[0]==1:
            screen.blit(copy,(0,0))
            screen.set_clip(canvasRect)
            if abs(mx-ox)>=4 and abs(my-oy)>=4: #checks for radius so it has a circular shape
                draw.ellipse(screen,col,(min(ox,mx),min(oy,my),abs(mx-ox),abs(my-oy)),1) #checks minimum of the x-coordinates, y-coordiantes, and checks width and height for draw.ellipse.
            screen.set_clip(None)
        if canvasRect.collidepoint(mx,my) and mb[2]==1:
            screen.blit(copy,(0,0))
            screen.set_clip(canvasRect)
            if abs(mx-ox)>=4 and abs(my-oy)>=4: #checks for radius so it has a circular shape
                draw.ellipse(screen,col,(min(ox,mx),min(oy,my),abs(mx-ox),abs(my-oy))) #checks minimum of the x-coordinates, y-coordiantes, and checks width and height for draw.ellipse.
            screen.set_clip(None)

#============================Stamps===============================
        
    #Mario Stamp
    if tool == "mario":
        display.set_caption("Mario - Left click to stamp Mario on canvas.")
        if canvasRect.collidepoint(mx,my) and mb[0]==1:
            screen.blit(copy,(0,0))
            screen.set_clip(canvasRect)
            screen.blit(marioblit,(mx-40,my-54)) #blits image at center
            screen.set_clip(None)

    #Luigi Stamp
    if tool == "luigi":
        display.set_caption("Luigi - Left click to stamp Luigi on canvas.")
        if canvasRect.collidepoint(mx,my) and mb[0]==1:
            screen.blit(copy,(0,0))
            screen.set_clip(canvasRect)
            screen.blit(luigiblit,(mx-48,my-56))
            screen.set_clip(None)
        
    #Mushroom Stamp
    if tool == "mushroom":
        display.set_caption("Mushroom - Left click to stamp a mushroom on canvas.")
        if canvasRect.collidepoint(mx,my) and mb[0]==1:
            screen.blit(copy,(0,0))
            screen.set_clip(canvasRect)
            screen.blit(mushroomblit,(mx-54,my-53))
            screen.set_clip(None)

    #FireFlower Stamp
    if tool == "fireflower":
        display.set_caption("Fireflower - Left click to stamp a fire flower on canvas.")
        if canvasRect.collidepoint(mx,my) and mb[0]==1:
            screen.blit(copy,(0,0))
            screen.set_clip(canvasRect)
            screen.blit(fireflowerblit,(mx-51,my-54))
            screen.set_clip(None)
        
    #Starman Stamp
    if tool == "starman":
        display.set_caption("Starman - Left click to stamp a starman on canvas.")
        if canvasRect.collidepoint(mx,my) and mb[0]==1:
            screen.blit(copy,(0,0))
            screen.set_clip(canvasRect)
            screen.blit(starmanblit,(mx-52,my-50))
            screen.set_clip(None)

    #1up Mushroom Stamp
    if tool == "1up" and canvasRect.collidepoint(mx,my) and mb[0]==1:
        display.set_caption("1up Mushroom - Left click to stamp a 1up on canvas.")
        if canvasRect.collidepoint(mx,my) and mb[0]==1:
            screen.blit(copy,(0,0))
            screen.set_clip(canvasRect)
            screen.blit(upblit,(mx-53,my-51))
            screen.set_clip(None)

#================Saving and Opening=================

    import tkinter.filedialog #tkinter is the most common Python GUI module for I/O

    root = tkinter.Tk() #these two lines delete the extra window tk creates
    root.withdraw()
    
    fileext=[("Windows Bitmap","*.bmp"), #usable file extensions
             ("Portable Network Graphics","*.png"),
             ("JPEG","*.jpg"),
             ("All files","*.*")]

    if saveRect.collidepoint(mx,my) and mb[0]==1: #click on save button
        tkintsave = tkinter.filedialog.asksaveasfilename(defaultextension="*.bmp",filetypes=fileext,title="Save image as...",) #tkinter makes a file name in any directory
        if len(tkintsave)>0:
            screen.set_clip(canvasRect) #clips canvas
            pygamesave = screen.copy() #copies screen, but only canvas
            screen.set_clip(None)
            pygame.image.save(pygamesave,tkintsave) #pygame saves the copy with tkinters chosen file name
            
    if openRect.collidepoint(mx,my) and mb[0]==1: #opens image from windows explorer dialog box
        fileopen = tkinter.filedialog.askopenfilename(filetypes=fileext,title='Choose an image...') #opens file from paint file directory
        if len(fileopen) > 0: #if opened
            fileopen = pygame.image.load(fileopen) #loads image as surface
            filesize = transform.scale(fileopen,(701,484)) #resizes surface to canvas size
            screen.set_clip(canvasRect) #ensures clip to canvas
            screen.blit(filesize,(172,112)) #blits opened image
            screen.set_clip(None)
        
#=======================Extras======================

    #Generates coordinates and prints them as a surface in a box.    
    coordbox = Rect(167,617,76,22) #box for coordinates in background  
    xcoord = arialFont.render(str(mx), True,blk)#makes x coordinate a picture
    comma = arialFont.render(",", True,blk) #makes coordinate comma a picture
    ycoord = arialFont.render(str(my), True,blk) #makes y coordinate a picture  
    screen.fill((255,255,255),coordbox) #fills box to add new coordinates
    screen.blit(comma,(203,618)) #blits in comma
    screen.blit(xcoord,(168,618)) #blits in x coordinate
    screen.blit(ycoord,(207,618)) #blits in y coordinate

    #Fills box with current selected color.
    draw.rect(screen,col,(167,672,78,78))
    
#=========================================================================

    display.update() #refreshes screen
    
pygame.font.quit() #quits pygame font module
del arialFont #deletes font
quit()# ends
