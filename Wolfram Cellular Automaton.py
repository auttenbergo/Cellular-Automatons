import pygame
pygame.init()

width = 1200
height = 600

win = pygame.display.set_mode((width,height))
pygame.display.set_caption("Wolfram Cellular Automata")

resolution = 3

generationsCount = height // resolution
generationLength = width // resolution


generations = []

for i in range(generationsCount):
    currGen = []
    for j in range(generationLength):
        currGen.append(0)
    generations.append(currGen)

generations[0][generationLength//2] = 1

white = (255,255,255)
black = (0,0,0)

#https://mathworld.wolfram.com/ElementaryCellularAutomaton.html

#rule 30 [0,0,0,1,1,1,1,0]
#rule 222 [1,1,0,1,1,1,1,0]
#rule 90 [0,1,0,1,1,0,1,0]
#rule 250 [1,1,1,1,1,0,1,0]
#rule 54 [0,0,1,1,0,1,1,0]


rule = [0,0,0,1,1,1,1,0]

run = True


def drawWindow():
    win.fill((255,255,255))

    for i in range(generationsCount):
        y = i*resolution
        for j in range(generationLength):
            currColor = black
            
            if generations[i][j] == 0:
                currColor = white
                
            x = j*resolution

            pygame.draw.rect(win,currColor,(x,y,resolution,resolution))
                
            
    pygame.display.update()

def ruleResult(first, second, third):
    index = (2**0)*third + (2**1)*second + (2**2)*first
    return rule[-(index+1)]
    

for i in range(generationsCount):
    currGen = generations[i]
    nextGen = []
    for j in range(generationLength):
        if j-1 < 0:
            left = 0
        else:
            left = currGen[j-1]
        curr = currGen[j]

        if j+1 >= generationLength:
            right = 0
        else:
            right = currGen[j+1]
        nextGen.append(ruleResult(left,curr,right))
    if i == generationsCount-1:
        continue
    generations[i+1] = nextGen

drawWindow()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
pygame.quit()
