import pygame
pygame.init()


win = pygame.display.set_mode((0,0),pygame.FULLSCREEN)

width = win.get_width()
height = win.get_height()

pygame.display.set_caption("Langton's Ant")

resolution = 2
rows = win.get_height() // resolution
cols = win.get_width() // resolution

grid = []
for row in range(rows):
    arr = []
    for col in range(cols):
        arr.append(0)
    grid.append(arr)


currX = rows // 2
currY = cols // 2

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

direction = UP

def turnRight(direction):
    rv = (direction + 1) % 4
    return rv
def turnLeft(direction):
    rv = direction - 1
    if(rv < UP):
        rv = LEFT
    return rv

def moveForward(x,y,direction):
    if direction == UP:
        x -= 1
    elif direction == RIGHT:
        y += 1
    elif direction == DOWN:
        x += 1
    else:
        y -= 1

    if x >= rows:
        x = 0
    elif x < 0:
        x = rows - 1

    if y >= cols:
        y = 0
    elif y < 0:
        y = cols - 1

    return x,y

black = (0,0,0)
white = (255,255,255)
gray = (20,20,20)
red = (255,0,0)

def redrawWindow():
    win.fill(black)

    pygame.draw.rect(win,red,(currY * resolution, currX * resolution, resolution,resolution))

    for row in range(rows):
        y = row * resolution
        pygame.draw.line(win,gray,(0,y),(width,y))
    for col in range(cols):
        x = col * resolution
        pygame.draw.line(win,gray,(x,0),(x,height))

    


    pygame.display.flip()

def redrawChange(currX,currY,color,resolution):
    x = currY * resolution
    y = currX * resolution
    
    pygame.draw.rect(win,color,(x,y, resolution,resolution))

    pygame.draw.line(win,gray,(0,y),(width,y))
    pygame.draw.line(win,gray,(x,0),(x,height))

    pygame.display.flip()


redrawWindow()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    state = grid[currX][currY]
    if state == 0:
        direction = turnRight(direction)
        grid[currX][currY] = 1
        redrawChange(currX,currY,white,resolution)
    else:
        direction = turnLeft(direction)
        grid[currX][currY] = 0
        redrawChange(currX,currY,black,resolution)
        
    currX,currY = moveForward(currX,currY,direction)
    redrawChange(currX,currY,red,resolution)
    
    

pygame.quit()
