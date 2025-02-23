import pygame
import random
import sys
import time

pygame.init()

player=0
bot=0
turn=0
ending=0
endroot=0
bp=0

standing=0
appear=0

end=0

game=0

count=0
bcount=0
rival=0

wincount=0
bwincount=0

card=[]
botcard=[]
card_image={}
choiced=[]
deck=[]


screen=pygame.display.set_mode((1440,810))
pygame.display.set_caption("Black jack")

font = pygame.font.SysFont("malgungothic",100)
losefont = pygame.font.SysFont("malgungothic",200)
expl= pygame.font.SysFont("malgungothic",50)
blackj= pygame.font.SysFont("malgungothic",300)


x_pos = 0
y_pos = 0

screen.fill((0,49,0))

for i in range(1,14):
    for j in ["s","c","h","d"]:
        card.append(j+str(i))
        img = pygame.image.load(j + str(i) + ".png")
        img = pygame.transform.scale(img, (200, 300))  # 카드 크기 조정
        card_image[j + str(i)] = img

deck+=card

back=pygame.image.load("back.png")
back2=pygame.image.load("back.png")
back2=pygame.transform.scale(back2, (280, 300))

class Button:
    def __init__(self,x,y,image,scale):
        width = image.get_width()
        height = image.get_height()
        self.image=pygame.transform.scale(image,(int(width*scale), int(height*scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

    def draw(self):

        screen.blit(self.image,(self.rect.x,self.rect.y))   

choice_button=Button(1300,405,back,0.6)

class sbutton:
    def __init__(self, x, y, width, height, text, color, text_color, font_size, action=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.text_color = text_color
        self.font = pygame.font.Font(None, font_size)
        self.action = action

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        text_surf = self.font.render(self.text, True, self.text_color)
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

button = sbutton(1200, 650, 200, 100, "stand", (0,0,0), (255,255,255), 36)


while True:
    
   
    text = font.render(str(player), True, (255,255,255),(0,49,0)) #(Text,anti-alias, color)
    dtext = font.render(str(bot), True, (255,255,255),(0,49,0))
 
    winc = expl.render(f"승리{str(wincount)}", True, (255,255,255),(0,49,0))
    bwinc = expl.render(f"패배{str(bwincount)}", True, (255,255,255),(0,49,0))


    losetext = losefont.render("BURST", True, (0,0,0),(255,255,255))
    blacktext = losefont.render("Black Jack", True, (255,255,255),(0,0,0))
    same  = losefont.render("PUSH", True, (0,0,0),(255,255,255))
    win = losefont.render("WIN", True, (0,0,0),(255,255,255))
    lose = losefont.render("LOSE", True, (0,0,0),(255,255,255))


    

    choice_button.draw()

    button.draw(screen)
    
      
    

    for event in pygame.event.get():
        
        if game==0 and event.type == pygame.MOUSEBUTTONDOWN:


            if choice_button.rect.collidepoint(event.pos):



                if turn==0:
                    for i in range(2):
                        choice=random.choice(card)
                
                        choiced.append(choice)
    
                        card.remove(choice)
                        player+=int(choice[1:len(choice)+1])
   
                        if int(choice[1:len(choice)+1])>10:
                            player-=(int(choice[1:len(choice)+1])-10)  

                        if int(choice[1:len(choice)+1])==1:
                            if player+10<=21:
                                player+=10
                                count=1
                        
                    #bot        
                    for i in range(2):
                        bchoice=random.choice(card)
                
                        botcard.append(bchoice)
    
                        card.remove(bchoice)
                        bot+=int(bchoice[1:len(bchoice)+1])
   
                        if int(bchoice[1:len(bchoice)+1])>10:
                            bot-=(int(bchoice[1:len(bchoice)+1])-10)

                        if i==0 and int(bchoice[1:len(bchoice)+1])==1:
                            bot+=10
                            bcount=1

                        if i==1:
                            bot-=int(botcard[1][1:len(botcard[1])+1])

                            if int(botcard[1][1:len(botcard[1])+1])==1:
                                bot-=10
                            if int(bchoice[1:len(bchoice)+1])>10:
                                bot+=(int(bchoice[1:len(bchoice)+1])-10)
                            if  int(bchoice[1:len(bchoice)+1])==1:
                                if bot+10<=21:
                                    bot+=10
                                    bcount=1
                    standing=1

                    turn+=1

                else:
                    choice=random.choice(card)

                
                    choiced.append(choice)
    
                    card.remove(choice)
                    player+=int(choice[1:len(choice)+1])
  
                    if int(choice[1:len(choice)+1])>10:
                        player-=(int(choice[1:len(choice)+1])-10)

                    if int(choice[1:len(choice)+1])==1:
                            if player+10<=21:
                                player+=10
                                count=1

                    turn+=1
                    if count==1 and player >21:
                        player-=10
                        count=0

            if button.rect.collidepoint(event.pos) and standing==1:
                bot+=int(botcard[1][1:len(botcard[1])+1])
                
                if int(botcard[1][1:len(botcard[1])+1])>10:
                    bot-=(int(botcard[1][1:len(botcard[1])+1])-10)
                if bcount==1 and bot+10<=21:
                    bot+=10
                    bcount=0           
                
                ending=1
    

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



  
    if turn>0 and game==0:
        screen.blit(card_image[choiced[0]],[200,600])
    if turn>0 and game==0:screen.blit(card_image[choiced[1]],[440,600])

    if turn>1 and game==0:screen.blit(card_image[choiced[2]],[680,600])

    if turn>2 and game==0:screen.blit(card_image[choiced[3]],[920,600])

    if turn>3 and game==0:screen.blit(card_image[choiced[4]],[200,675])

    if turn>4 and game==0:screen.blit(card_image[choiced[5]],[440,675])

    if turn>5 and game==0:screen.blit(card_image[choiced[5]],[680,675])



        

    if turn>0 and game==0:
        screen.blit(card_image[botcard[0]],[200,-100])

        screen.blit(back2,[400,-100])
    
    if ending==1 and game==0:

        screen.blit(card_image[botcard[1]],[440,-100])
        endroot=1



        #time.sleep(1)
        if bot<player and bot<17:

            
            bchoice=random.choice(card)
                
            botcard.append(bchoice)
    
            card.remove(bchoice)
            bot+=int(bchoice[1:len(bchoice)+1])
   
            if int(bchoice[1:len(bchoice)+1])>10:
                bot-=(int(bchoice[1:len(bchoice)+1])-10)

            if  int(bchoice[1:len(bchoice)+1])==1:
                if bot+10<=21:
                    bot+=10
                    bcount=1 
            screen.blit(dtext, (50,50))

            if bcount==1 and bot >21:
                    bot-=10
                    bcount=0
            

            if len(botcard)>=3 and appear==1:
                screen.blit(dtext, (50,50))
                screen.blit(card_image[botcard[2]],[680,-100])
                
            if len(botcard)==4:
                screen.blit(dtext, (50,50))
                screen.blit(card_image[botcard[3]],[920,-100])

            if len(botcard)>=5:
                screen.blit(dtext, (50,50))
                screen.blit(card_image[botcard[4]],[200,-175])

            if len(botcard)>=6:
                screen.blit(dtext, (50,50))
                screen.blit(card_image[botcard[4]],[440,-175])

            if len(botcard)>=7:
                screen.blit(dtext, (50,50))
                screen.blit(card_image[botcard[4]],[680,-175])
            time.sleep(1)
            appear=1

        if bot>=17:bp=1
    
     
            
               
        

    if player>21:
        screen.blit(card_image[botcard[1]],[440,-100])
        

        pygame.draw.rect(screen, (0,0,0),[-50,200,1500,400])
        pygame.draw.rect(screen, (255,255,255),[-50,222.5,1500,350])
        screen.blit(losetext, (450,250))
        if end==0:
            bot+=int(bchoice[1:len(bchoice)+1])
   
            if int(bchoice[1:len(bchoice)+1])>10:
                bot-=(int(bchoice[1:len(bchoice)+1])-10)

            if bcount==1 and bot >21:
                bot-=10
                bcount=0
            if bcount==1 and bot+10<=21:
                bot+=10
                bcount=0

            end=1
        if rival==0:
            bwincount+=1
            rival=1
        #screen.blit(expltext, (50,50))
        game=1


    if player==21:
        screen.blit(card_image[botcard[1]],[440,-100])

        pygame.draw.rect(screen, (255,255,255),[-50,200,1500,400])
        pygame.draw.rect(screen, (0,0,0),[-50,222.5,1500,350])
        screen.blit(blacktext, (300,250))
        #screen.blit(expltext, (50,50))
        if end==0:
            bot+=int(bchoice[1:len(bchoice)+1])
   
            if int(bchoice[1:len(bchoice)+1])>10:
                bot-=(int(bchoice[1:len(bchoice)+1])-10)

            if bcount==1 and bot >21:
                bot-=10
                bcount=0
            if bcount==1 and bot+10<=21:
                bot+=10
                bcount=0
            end=1
        if rival==0:
            wincount+=1
            rival=1
        game=1


    if ending==1 and player==bot:
        if len(botcard)>=3:
            screen.blit(dtext, (50,50))
            screen.blit(card_image[botcard[2]],[680,-100])
                
        if len(botcard)==4:
            screen.blit(dtext, (50,50))
            screen.blit(card_image[botcard[3]],[920,-100])

        if len(botcard)>=5:
            screen.blit(dtext, (50,50))
            screen.blit(card_image[botcard[4]],[200,-175])

        if len(botcard)>=6:
            screen.blit(dtext, (50,50))
            screen.blit(card_image[botcard[4]],[440,-175])

        if len(botcard)>=7:
            screen.blit(dtext, (50,50))
            screen.blit(card_image[botcard[4]],[680,-175])

 
                            
        pygame.draw.rect(screen, (0,0,0),[-50,200,1500,400])
        pygame.draw.rect(screen, (255,255,255),[-50,222.5,1500,350])
        screen.blit(same, (475,250))
        #screen.blit(expltext, (50,50))
        game=1

    if ending==1 and bot<player and bp==1 and player <= 21:
        if len(botcard)>=3:
            screen.blit(dtext, (50,50))
            screen.blit(card_image[botcard[2]],[680,-100])
                
        if len(botcard)==4:
            screen.blit(dtext, (50,50))
            screen.blit(card_image[botcard[3]],[920,-100])

        if len(botcard)>=5:
            screen.blit(dtext, (50,50))
            screen.blit(card_image[botcard[4]],[200,-175])

        if len(botcard)>=6:
            screen.blit(dtext, (50,50))
            screen.blit(card_image[botcard[4]],[440,-175])

        if len(botcard)>=7:
            screen.blit(dtext, (50,50))
            screen.blit(card_image[botcard[4]],[680,-175])
 


        pygame.draw.rect(screen, (0,0,0),[-50,200,1500,400])
        pygame.draw.rect(screen, (255,255,255),[-50,222.5,1500,350])
        screen.blit(win, (525,250))

        #screen.blit(expltext, (50,50))
        if rival==0:
            wincount+=1
            rival=1
        game=1



    if bot>21 and player <= 21:
        if len(botcard)>=3:
            screen.blit(dtext, (50,50))
            screen.blit(card_image[botcard[2]],[680,-100])
                
        if len(botcard)==4:
            screen.blit(dtext, (50,50))
            screen.blit(card_image[botcard[3]],[920,-100])

        if len(botcard)>=5:
            screen.blit(dtext, (50,50))
            screen.blit(card_image[botcard[4]],[200,-175])

        if len(botcard)>=6:
            screen.blit(dtext, (50,50))
            screen.blit(card_image[botcard[4]],[440,-175])

        if len(botcard)>=7:
            screen.blit(dtext, (50,50))
            screen.blit(card_image[botcard[4]],[680,-175])

 

        pygame.draw.rect(screen, (0,0,0),[-50,200,1500,400])
        pygame.draw.rect(screen, (255,255,255),[-50,222.5,1500,350])
        screen.blit(win, (525,250))

        #screen.blit(expltext, (50,50))
        if rival==0:
            wincount+=1
            rival=1
        game=1



    if ending==1 and bot>player and bot<=21:
        if len(botcard)>=3:
            screen.blit(dtext, (50,50))
            screen.blit(card_image[botcard[2]],[680,-100])
                
        if len(botcard)==4:
            screen.blit(dtext, (50,50))
            screen.blit(card_image[botcard[3]],[920,-100])

        if len(botcard)>=5:
            screen.blit(dtext, (50,50))
            screen.blit(card_image[botcard[4]],[200,-175])

        if len(botcard)>=6:
            screen.blit(dtext, (50,50))
            screen.blit(card_image[botcard[4]],[440,-175])

        if len(botcard)>=7:
            screen.blit(dtext, (50,50))
            screen.blit(card_image[botcard[4]],[680,-175])


        pygame.draw.rect(screen, (0,0,0),[-50,200,1500,400])
        pygame.draw.rect(screen, (255,255,255),[-50,222.5,1500,350])
        screen.blit(lose, (475,250))
        if rival==0:
            bwincount+=1
            rival=1  
        game=1


  

    
    screen.blit(text, (50,650)) #(글자변수, 위치)
    screen.blit(dtext, (50,50))
    screen.blit(winc, (30,600))
    screen.blit(bwinc, (30,0))
    


    if game==1 and event.type == pygame.KEYUP:
        if event.key == pygame.K_SPACE:
            screen.fill((0,49,0))
            choice_button.draw()
            button.draw(screen)
            player=0
            bot=0
            card=[]
            botcard=[]
            choice=[]
            bchoice=[]
            choiced=[]
            card+=deck
            turn=0
            end=0
            ending=0
            rival=0
            game=0
            endroot=0
            endroot=0
            count=0
            bcount=0
            bp=0
            appear=0
            standing=0

        


    pygame.display.update()

#값하나 더 추가한뒤 0,1로 키클릭하면...


