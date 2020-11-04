import pygame, sys
from pygame.locals import *
#intialization of modules
pygame.init()
#font
font=pygame.font.Font("freesansbold.ttf",20)
#setting screen size for the game
screen=pygame.display.set_mode((700,500))
#(width,height)
pygame.display.set_caption("Doremon Jump")
#color
white = (135,206,235)
black=(0,0,0)
#doremon images
doremon=pygame.image.load("obj1.png")
doremon=pygame.transform.scale(doremon,(85,98))
doremon2=pygame.image.load("obj2.png")
doremon2=pygame.transform.scale(doremon2,(85,98))
doremon3=pygame.image.load("obj3.png")
doremon3=pygame.transform.scale(doremon3,(85,98))
doremon4=pygame.image.load("obj4.png")
doremon4=pygame.transform.scale(doremon4,(85,98))
doremon5=pygame.image.load("obj5.png")
doremon5=pygame.transform.scale(doremon5,(85,98))
doremon6=pygame.image.load("obj6.png")
doremon6=pygame.transform.scale(doremon6,(85,98))
#array of doremon images
walk=[doremon,doremon,doremon,doremon,doremon2,doremon2,doremon2,doremon2,doremon3,doremon3,doremon3,doremon3,doremon3,doremon3,doremon3,doremon4,doremon4,doremon4,doremon5,doremon5,doremon5,doremon5,doremon6,doremon6,doremon6,doremon6]
#background image clouds and ground
background=pygame.image.load("background.png")
#obstacle/wall image
wall1=pygame.image.load("wall1.png")
wall1=pygame.transform.scale(wall1,(50,130))
wall2=pygame.image.load("wall2.png")
wall2=pygame.transform.scale(wall2,(75,130))
wall3=pygame.image.load("wall3.png")
wall3=pygame.transform.scale(wall3,(100,130))
#sound intialization
mute=pygame.image.load("mute.png")
unmute=pygame.image.load("unmute.png")
jumpSound=pygame.mixer.Sound("jumpSound.wav")
gameoverSound=pygame.mixer.Sound("gameoverSound.wav")
#music=pygame.mixer.music.load("music.mp3")
#variables to send as arguement
volume=True
highscore=0

def gameLoop(highscore,volume):
    #pygame.mixer.music.play(-1)
    backx=0
    backy=0
    backvelocity= 0
    wallx=200
    wally=395
    doremonx=50
    doremony=395
    walkpoint=0
    jump=False
    score=0
    gravity=7
    game=False
    gameover=False
    FRAMERATE=60
    clock=pygame.time.Clock()
    while True:
        clock.tick(FRAMERATE)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()         
            if event.type==KEYDOWN:
                if event.key==K_UP:
                    if doremony== 395:
                        jumpSound.play()
                        jump=True
                        game=True
                        backvelocity=5     
                if event.key == pygame.K_m:
                    jumpSound.set_volume(0)
                    gameoverSound.set_volume(0)
                    volume=False
                   
                if event.key == pygame.K_n:
                    jumpSound.set_volume(50)
                    gameoverSound.set_volume(50)
                    volume=True                 
                if event.key==K_SPACE:
                    if game==False:
                        gameoverSound.stop()
                        gameLoop(highscore,volume)
        if backx < -700:
            backx = 0 
        if wallx < -3200:
            wallx=750
    #when jump
        if 396>doremony>200:
            if jump==True:
                doremony-=7
        else:
                jump=False    
        if doremony<395:
            if jump==False:
                doremony+=gravity  
    #colllision
        if wallx<doremonx+100<wallx+75 and wally<doremony+50<wally+130:
            backvelocity=0   
            walkpoint=0
            game=False
            gameover=True
        if wallx+600<doremonx+100<wallx+650 and wally<doremony+50<wally+130:
            backvelocity=0   
            walkpoint=0 
            game=False
            gameover=True
        if wallx+1200<doremonx+100<wallx+1300 and wally<doremony+50<wally+130:
            backvelocity=0   
            walkpoint=0 
            game=False
            gameover=True
        if wallx+1800<doremonx+100<wallx+1875 and wally<doremony+50<wally+130:
            backvelocity=0   
            walkpoint=0 
            game=False
            gameover=True
        if game==True:
            score+=1
            if 0<score<=500:
                backvelocity =5
            elif 500<score<=1000:
                backvelocity =6
            elif 1000<score<=1500:
                backvelocity=7
            elif 1500<score<=3000:
                backvelocity=9
            elif 3000<score<=5000:
                backvelocity=10
            elif 5000<score<=7000:
                backvelocity=11
            elif score>700:
                backvelocity=12      
            if(highscore<score):
                highscore=score

        text=font.render("SCORE: "+str(score),True,black)  
        end_text=font.render("Game Over. Press space to continue",True,black)
        high_text=font.render("HIGH SCORE: "+str(highscore),True,black)

        screen.fill(white)
        screen.blit(text,[400,10])
        screen.blit(high_text,[10,10])
        screen.blit(background,[backx,backy])
        screen.blit(background,[backx + 700,backy])

        if gameover==True:
            gameoverSound.play()
            screen.blit(end_text,[200,250])
        screen.blit(walk[walkpoint],[doremonx,doremony])        
        backx-=backvelocity
        wallx-=backvelocity
        if game==True:
            walkpoint+=1
        if walkpoint>24:
            walkpoint=0

        screen.blit(wall2,[wallx,wally])
        screen.blit(wall1,[wallx+600,wally])
        screen.blit(wall3,[wallx+1200,wally])
        screen.blit(wall2,[wallx+1800,wally])

        if volume==True:
            screen.blit(unmute,[650,10])
        elif volume==False:
             screen.blit(mute,[650,10])   
        pygame.display.update()
gameLoop(highscore,volume)       