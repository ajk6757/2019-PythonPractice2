# -*- coding: utf-8 -*-
import sys
import pygame
import random
from pygame.locals import QUIT

pygame.init()
SURFACE = pygame.display.set_mode((800,600))
pygame.display.set_caption("JUST WINDOW")
FPSCLOCK = pygame.time.Clock()

def main():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        SURFACE.fill((255,255,255))
        start_pos = (0,0)
        end_pos = (100,600)
        pointlist = []
        
        pygame.draw.rect(SURFACE,(155,55,180),(360,360,200,240))
        pygame.draw.rect(SURFACE,(255,0,0),(360,140,260,280))
        pygame.draw.circle(SURFACE,(100,250,200),(280,400),180)
        pygame.draw.rect(SURFACE,(0,255,255),(480,0,200,140))
        
        pygame.draw.rect(SURFACE,(0,255,0),(320,60,200,180))
        pygame.draw.rect(SURFACE,(255,255,0),(60,140,260,260))
        
        
        pygame.draw.rect(SURFACE,(100,150,0),(0,0,160,140))
        pygame.draw.rect(SURFACE,(0,25,50),(160,0,160,200))
        pygame.draw.rect(SURFACE,(80,0,80),(320,0,160,60))
        pygame.draw.rect(SURFACE,(50,0,188),(680,0,120,180))
        pygame.draw.rect(SURFACE,(255,55,100),(620,180,200,180))
        pygame.draw.rect(SURFACE,(255,180,80),(0,200,60,280))
        pygame.draw.rect(SURFACE,(55,55,100),(620,360,140,180))
        pygame.draw.rect(SURFACE,(115,125,100),(560,540,336,120))
        pygame.draw.rect(SURFACE,(155,255,100),(760,380,140,260))
        
       
        
        
        pygame.draw.circle(SURFACE,(38,150,200),(550,470),100)
        pygame.draw.circle(SURFACE,(255,150,200),(720,500),70)
        pygame.draw.circle(SURFACE,(255,200,0),(200,400),30,20)
        pygame.draw.circle(SURFACE,(255,200,0),(360,400),30,20)
        
        pygame.draw.circle(SURFACE,(255,255,255),(498,450),22,12)
        pygame.draw.circle(SURFACE,(255,255,255),(600,450),22,12)
        pygame.draw.circle(SURFACE,(0,250,0),(688,480),16,8)
        pygame.draw.circle(SURFACE,(0,250,0),(750,480),16,8)
        
        pygame.draw.ellipse(SURFACE,(0,0,0),(246,400,70,50))
        pygame.draw.ellipse(SURFACE,(0,0,0),(524,462,50,32))
        pygame.draw.ellipse(SURFACE,(0,0,0),(698,494,44,26))
        
        pygame.draw.line(SURFACE,(0,0,255),start_pos, end_pos,10)
        pygame.draw.line(SURFACE,(0,0,255),(0,640), (800,200),10)
        
        for _ in range(10):
            xpos = random.randint(600,800)
            ypos = random.randint(0,360)
            pointlist.append((xpos,ypos))
            
        pygame.draw.lines(SURFACE, (0,0,0),True, pointlist,5)
        
        
     
        pygame.display.update()
        FPSCLOCK.tick(3)

if __name__ == '__main__':
    main()