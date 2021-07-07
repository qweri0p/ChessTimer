import pygame as pg
import time
SetTime = 10
pg.init()
size = (1500, 700)
screen = pg.display.set_mode(size)
pg.display.set_caption('Timer')
activePlayer = 2       
clock = pg.time.Clock()
font = pg.font.SysFont('Consolas', 256)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
bg = WHITE
minute0=SetTime
minute1=SetTime
second0=00
second1=00
minutes = 69
seconds = 69

player0counter = 0
player1counter = 0
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
            if minutes == 0 and activePlayer != 2:
                bg = RED
            else:
                minutes-=1
                seconds = 59
        else:
            seconds-=1
    elif player1counter == 60:
        player1counter =0
        if seconds == 0:
            if minutes == 0 and activePlayer != 2:
                bg = RED
            else:
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



    screen.fill(bg)



    if second0 == 0:
        extra0 = 0
        extras0 = ""
    elif second0 < 10:
        extras0 = 0
    else:
        extra0 = ""
        extras0 = ""
    if second1 == 0:
        extra1 = 0
        extras1 = ""
    elif second1 < 10:
        extras1 = 0
    else:
        extra1 = ""
        extras1 = ""

        
    val0 = f'{str(minute0)}:{str(extras0)}{str(second0)}{extra0}'
    val1 = f'{str(minute1)}:{str(extras1)}{str(second1)}{extra1}'
    temp0 = font.render(str(val0), True, BLACK)
    temp1 = font.render(str(val1), True, BLACK) 
    screen.blit(temp0, (15, 450))
    screen.blit(temp1, (800, 450)) 



    pg.display.flip()
    pg.display.update()
    clock.tick(60)
