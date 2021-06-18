import pygame

pygame.init()


win = pygame.display.set_mode((0,0),pygame.FULLSCREEN)

width = win.get_width()
height = win.get_height()

pygame.display.set_caption("Turmite - Spiral Growth")

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
state = 0

def turnRight(direction):
    rv = (direction + 1) % 4
    return rv
def turnLeft(direction):
    rv = direction - 1
    if rv < UP:
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

    
    return x,y


black = (0,0,0)
white = (255,255,255)
gray = (20,20,20)


def redrawWindow():
    win.fill(black)

    for row in range(rows):
        y = row * resolution
        pygame.draw.line(win,gray,(0,y),(width,y))
    for col in range(cols):
        x = col * resolution
        pygame.draw.line(win,gray,(x,0),(x,height))
        
    pygame.display.flip()


def inBounds(x,y):
    if x < 0 or x >= rows or y < 0 or y >= cols:
        return False
    return True


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

    if(not(inBounds(currX,currY))):
        run = False

    cell = grid[currX][currY]
    
    if state == 0:
        if cell == 0:
            grid[currX][currY] = 1
            redrawChange(currX,currY,white,resolution)
            currX,currY = moveForward(currX,currY,direction)
            state = 1
        else:
            direction = turnLeft(direction)
            currX,currY = moveForward(currX,currY,direction)
            state = 0
    elif state == 1:
        if cell == 0:
            grid[currX][currY] = 1
            redrawChange(currX,currY,white,resolution)
            direction = turnRight(direction)
            currX,currY = moveForward(currX,currY,direction)
            state = 1
        else:
            grid[currX][currY] = 0
            redrawChange(currX,currY,black,resolution)
            currX,currY = moveForward(currX,currY,direction)
            state = 0

    pygame.time.delay(2)
            
pygame.quit()






    
