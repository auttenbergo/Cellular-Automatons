import pygame
pygame.init()

width = 700
height = 700

win = pygame.display.set_mode((width,height))
pygame.display.set_caption("Langton's Ant")


clock = pygame.time.Clock()

resolution = 5
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

    for row in range(rows):
        y = row * resolution
        for col in range(cols):
            x = col * resolution
            
        
            color = black
            if grid[row][col] == 1:
                color = white
                
            if row == currX and col == currY:
                color = red
            pygame.draw.rect(win,color,(x,y,resolution,resolution))

            pygame.draw.line(win,gray,(x,y),(x,height))
            pygame.draw.line(win,gray,(x,y),(width,y))


    pygame.display.flip()


step = 0
drawLoop = 1000

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    state = grid[currX][currY]
    if state == 0:
        direction = turnRight(direction)
        grid[currX][currY] = 1
    else:
        direction = turnLeft(direction)
        grid[currX][currY] = 0
    currX,currY = moveForward(currX,currY,direction)

    step += 1
    if(step >= drawLoop):
        step = 0
        redrawWindow()
    
    

pygame.quit()
