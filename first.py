import pygame
import random

pygame.init()

# Colors
red = (255, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 255)
darkgreen = (0, 155, 50)
black = (0, 0, 0)

# Resolution
display_width = 800
display_height = 600

# declaration
FPS = 10
applethickness = 30
direction = "right"
block_size = 20

#fonts
smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)

# images
img = pygame.image.load('snakehead.png')
aimg = pygame.image.load('apple.png')

# fps and window
clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Anaconda")


# functions

def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        gameDisplay.fill(black)
        message_to_screen("paused",
                          white,
                          -100,
                          size="large")

        message_to_screen("Press C to continue or Q to quit",
                          red,
                          50,
                          size="medium")
        pygame.display.update()
        clock.tick(60)
def score(score):
    text = smallfont.render("Score: " + str(score), True, white)
    gameDisplay.blit(text, (0, 0))


def randapplegen():
    randappleX = round(random.randrange(0, display_width - applethickness))
    randappleY = round(random.randrange(0, display_height - applethickness))
    return randappleX, randappleY


def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        gameDisplay.fill(black)
        message_to_screen("Welcome to Anaconda",
                          red,
                          -200,
                          "large")
        message_to_screen("Just Eat Apples also p = pause",
                          blue,
                          100,
                          "medium")

        message_to_screen("Press C to Play or Q to quit",
                          white,
                          200,
                          "medium")
        pygame.display.update()
        clock.tick(60)


def snake(block_size, snakelist):
    if direction == "right":
        head = pygame.transform.rotate(img, 270)
    if direction == "left":
        head = pygame.transform.rotate(img, 90)
    if direction == "up":
        head = img
    if direction == "down":
        head = pygame.transform.rotate(img, 180)
    gameDisplay.blit(head, (snakelist[-1][0], snakelist[-1][1]))
    for xny in snakelist[:-1]:
        gameDisplay.fill(green, rect=(xny[0], xny[1], block_size, block_size))


def text_objects(text, color, size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)

    return textSurface, textSurface.get_rect()


def message_to_screen(msg, color, y_displace=0, size="small"):
    textsurf, textRect = text_objects(msg, color, size)
    textRect.center = (display_width / 2, (display_height / 2) + y_displace)
    gameDisplay.blit(textsurf, textRect)


def gameloop():
    global direction
    gameExit = False
    gameOver = False

    lead_x = display_width / 2
    lead_y = display_width / 2
    lead_x_change = 0
    lead_y_change = 0

    snakelist = []
    snakelength = 1

    randappleX, randappleY = randapplegen()
    while not gameExit:
        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game Over",
                              red,
                              -50,
                              size="large")
            message_to_screen("Press C to play again or Q to quit",
                              black,
                              50,
                              size="small")
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameOver = False
                        gameExit = True
                    if event.key == pygame.K_c:
                        gameloop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                    direction = "right"
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                    direction = "left"
                if event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                    direction = "up"
                if event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0
                    direction = "down"
                if event.key == pygame.K_p:
                    pause()

            if lead_x >= display_width or lead_x <= 0 or lead_y <= 0 or lead_y >= display_height:
                gameOver = True

        lead_x += lead_x_change
        lead_y += lead_y_change

        gameDisplay.fill(darkgreen)

        gameDisplay.blit(aimg, (randappleX, randappleY))

        snakehead = []
        snakehead.append(lead_x)
        snakehead.append(lead_y)
        snakelist.append(snakehead)
        if len(snakelist) > snakelength:
            del snakelist[0]

        for each in snakelist[:-1]:
            if each == snakehead:
                gameOver = True

        snake(block_size, snakelist)

        score(snakelength - 1)
        pygame.display.update()
        if ( randappleX + applethickness > lead_x > randappleX) or lead_x + block_size > randappleX and lead_x + block_size < randappleX + applethickness:
            if lead_y > randappleY and lead_y < randappleY + applethickness or lead_y + block_size > randappleY and lead_y + block_size < randappleY + applethickness:
                randappleX, randappleY = randapplegen()
                snakelength += 1

        clock.tick(FPS)

    pygame.quit()
    quit()


game_intro()
gameloop()
