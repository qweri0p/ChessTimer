import pygame as pg
import time
pg.init()
size = (1500, 700)
screen = pg.display.set_mode(size)
pg.display.set_caption('Timer')
activePlayer = 2       
clock = pg.time.Clock()
font = pg.font.Font('font.ttf', 128)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
minute0=15
minute1=15
second0=00
second1=00
player0counter = 0
player1counter = 0

def DrawTimer(minute0, second0, minute1, second1):
    if second0 == 0:
        extra0 = 0
    else:
        extra0 = ""
    if second1 == 0:
        extra1 = 0
    else:
        extra1 = ""
    val0 = f'{str(minute0)}:{str(second0)}{extra0}'
    val1 = f'{str(minute1)}:{str(second1)}{extra1}'
    temp0 = font.render(str(val0), True, BLACK)
    temp1 = font.render(str(val1), True, BLACK) 
    screen.blit(temp0, (100, 350))
    screen.blit(temp1, (1100, 350))                            

done = False
while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                if activePlayer == 1:
                    activePlayer = 0
                elif activePlayer == 0:
                    activePlayer = 1
            elif event.key == pg.K_ESCAPE:
                done = True
            elif event.key == pg.K_RETURN:
                activePlayer = 1
    if activePlayer == 0:
        seconds = second0
        minutes = minute0
        player0counter +=1
        print(player0counter)
    elif activePlayer == 1:
        seconds = second1
        minutes = minute1
        player1counter +=1
        print(player1counter)
    else:
        print('no')
    
    if player0counter == 60:
        player0counter =0
        if seconds == 0:
            minutes-=1
            seconds = 59
        else:
            seconds-=1
    elif player1counter == 60:
        player1counter =0
        if seconds == 0:
            minutes-=1
            seconds = 59
        else:
            seconds-=1
    
    
    if activePlayer == 0:
        minute0 = minutes
        second0 = seconds
    elif activePlayer == 1:
        minute1 = minutes
        second1 = seconds



    screen.fill(WHITE)
    DrawTimer(minute0, second0, minute1, second1)
    pg.display.flip()
    pg.display.update()
    clock.tick(60)
