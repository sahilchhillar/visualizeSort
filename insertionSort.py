import os, sys, pygame, random, time
from pygame.locals import *

pygame.init()
pygame.font.init()

myfont = pygame.font.SysFont('OpenType', 40)

window = pygame.display.set_mode((900,600))
pygame.display.set_caption("Insertion Sort")

array = [0]*80
arrayColor = [(0,204,102)]*80
color =[(0, 204, 102), (255, 0, 0), (0, 0, 153), (255, 102, 0)]
run = True

pygame.draw.line(window, (0,0,0), (0,100),(900,100), 1)

#generate a random array
def genArr():
    for i in range(0,80):
        arrayColor = color[0]
        array[i] = random.randrange(0,80)
genArr()

#clear screen and place the bars at the correct position
def refill():
    window.fill((255,255,255))
    drawBar()
    pygame.display.update()
    pygame.time.delay(5)

#draw bars
def drawBar():
    text = myfont.render("Press Enter to start the sorting", False, (0,0,0))
    text2 = myfont.render("Press R to create different arrays", False, (0,0,0))

    window.blit(text, (10,10))
    window.blit(text2, (10,50))

    horPad = window.get_width()/150
    verPad = window.get_height()/100
    for i in range(1,80):
        pygame.draw.line(window, (224,224,224), (0,horPad*i+100), (900,horPad*i+100),1)

    #drawing bars
        for i in range(0,80):
            pygame.draw.line(window, arrayColor[i], (verPad*i,100), (verPad*i, array[i]*horPad+100), 6)
            

#insertion sort
def insertionSort(array, length):
    start_time = time.time()
    for i in range(1,length):
        ele = array[i]
        j = i-1
        while j >= 0 and ele < array[j]:
            pygame.event.pump()
            arrayColor[j] = color[0]
            arrayColor[i] = color[0]
            refill()
        	
            array[j+1] = array[j]
            j -= 1
        	
            array[j+1] = ele
                
            arrayColor[j] = color[0]
            arrayColor[i] = color[0]

            refill()
        
    end_time = time.time()
    return end_time-start_time

while run:
    window.fill((255,255,255))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                genArr()
            if event.key == pygame.K_RETURN:
                exeTime = insertionSort(array, len(array))
                print(exeTime)
            if event.key == pygame.K_ESCAPE:
                sys.exit()
                
    drawBar()
    pygame.display.update()
