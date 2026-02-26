# creating a game window
import pygame

pygame.init() # initializing pygame
screen = pygame.display.set_mode((800, 600)) # creating display window
pygame.display.set_caption("My first game") # setting window title
running = True # running variable
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit() # quit game

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("event handling")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN: # runs when key is pressed and KEYUP runs when key is released
            if event.key == pygame.K_LEFT:
                print("left arrow key pressed")
            elif event.key == pygame.K_RIGHT:
                print("right arrow key pressed")
pygame.quit()


#drawing shapes
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("drawing shapes")
RED = (255, 0, 0)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, RED, (100, 100, 200, 150))
    pygame.display.update()
pygame.quit()


# rendering text
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("text rendering")
# set font for rendering text
font = pygame.font.Font(None, 36) # font name and size
text = font.render("Hello PyGame", True, (255, 255, 255))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    screen.blit(text, (100, 100))
    pygame.display.update()
pygame.quit()

print("======================================================================")
###############################################################################
###############################################################################

'''
Task 1: Custom Game Window
Create a Pygame window with:
•	Size: 1000 x 700
•	Title: "Intern Game Window"
•	Background color: Any color except black
'''
pygame.init()
screen = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Intern Game Window")
bg = (50, 150, 200)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(bg)
    pygame.display.update()
pygame.quit()

'''
Task 2: Shape Playground
Create a window with white background and draw:
•	Rectangle
•	Circle
•	Square
Requirements:
•	Each shape must have a different color.
•	Shapes must be visible clearly on white background.
'''
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Task 2: Shape Playground")
bg = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, RED, (50, 50, 200, 150))
    pygame.draw.circle(screen, GREEN, (375, 125), 75)
    pygame.draw.rect(screen, BLUE, (200, 300, 150, 150))
    pygame.display.update()
pygame.quit()

'''
Task 3: Detect Multiple Keys
Modify the program so that:
•	LEFT key → Print "Moving Backward"
•	RIGHT key → Print "Moving Forward"
•	UP key → Print "Jump"
•	DOWN key → Print "Crouch"
'''
pygame.init()
screen = pygame.display.set_mode((200, 200))
pygame.display.set_caption("Task 3: Detect Multiple Keys")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("Moving Backward")
            elif event.key == pygame.K_RIGHT:
                print("Moving Forward")
            elif event.key == pygame.K_UP:
                print("Jump")
            elif event.key == pygame.K_DOWN:
                print("Crouch")
pygame.quit()

'''
Task 4: Sound Player with Text
Create a Pygame program with:
•	Window title → "Sound Player"
•	Background color → Gray
•	Display text → "Playing..."
•	Play a .wav sound file properly
'''
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Sound Player")
GRAY = (150, 150, 150)
BLACK = (0, 0, 0)
sound = pygame.mixer.Sound("game_over.wav")
sound.play()
font = pygame.font.Font(None, 36)
text = font.render("Playing...", True, (0, 0, 0))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(GRAY)
    screen.blit(text, (100, 100))
    pygame.display.update()
pygame.quit()

'''
 Task 5: Display Custom Text
Using text rendering, display:
•	Your Name
•	Your Course Name
Requirements:
•	Text color → Green
•	Position → (200, 250)
'''
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Task 5: Display Custom Text")
GRAY = (150, 150, 150)
font = pygame.font.Font(None, 36)
text1 = font.render("My name is Abdul", True, (0, 255, 0))
text2 = font.render("My course AIML", True, (0, 255, 0))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(GRAY)
    screen.blit(text1, (150, 100))
    screen.blit(text2, (150, 200))
    pygame.display.update()
pygame.quit()

'''
Task 6: Multi Audio Player
Create a window titled "Multi Sound Player" with:
•	White background
•	Red circle (radius = 60)
Audio Requirements:
•	.mp3 audio1 → Play 5 times
•	.mp3 audio → Play forever
Use your own audio
•	game_over.wav → Play once
'''
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Multi Sound Player")
BLACK = (0, 0, 0)
own = pygame.mixer.Sound("game_over.wav")
own.play()
aud1 = pygame.mixer.Sound("glass_breaking.mp3")
aud1.play(loops = 4)
aud2 = pygame.mixer.Sound("subway_surfers.mp3")
aud2.play(loops = -1)
font = pygame.font.Font(None, 36)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (150, 150), 60)
    pygame.display.update()
pygame.quit()


'''
 Task 7: Create Your Own Mini Game
(using:Window creation,Shapes,Colors,Text rendering,Key handling,Audio)
'''
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Task 7: Create Your Own Mini Gam")

player_size = 50
player_x = 225
player_y = 225
speed = 5

score = 0
font = pygame.font.Font(None, 36)
sound = pygame.mixer.Sound("glass_breaking.mp3")
clock = pygame.time.Clock()
running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_x -= speed
        score += 1
    if keys[pygame.K_RIGHT]:
        player_x += speed
        score += 1
    if keys[pygame.K_UP]:
        player_y -= speed
        score += 1
    if keys[pygame.K_DOWN]:
        player_y += speed
        score += 1

    if player_x <= 0 or player_x + player_size >= 500:
        sound.play()
    if player_y <= 0 or player_y + player_size >= 500:
        sound.play()

    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, (0, 0, 255), (player_x, player_y, player_size, player_size))

    score_text = font.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.update()

pygame.quit()
