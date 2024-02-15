# Snake Game (Using Python)
import pygame
import random
import os

# Initialization
pygame.mixer.init()
pygame.init()

# Colors
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
snakegreen = (35, 45, 40)

#Game Backgrounds
gameimg = pygame.image.load("gameimg.jpg")
intro = pygame.image.load("Intro1.png")
outro = pygame.image.load("outro.png")

# Creating window
screen_width = 900
screen_height = 600
gamewindow = pygame.display.set_mode((screen_width, screen_height))

# img = pygame.image.load("")
# img = pygame.transform.scale(img, (screen_width, screen_height)).convert_alpha()

#Variables For The Game
clock = pygame.time.Clock()
font = pygame.font.SysFont('Harrington', 55)
# Title
pygame.display.set_caption("Snake Game")
pygame.display.update()

#Music
pygame.mixer.music.load('game song 2.mp3')
pygame.mixer.music.play(100)
pygame.mixer.music.set_volume(.6)

def text_screen(text,color,x,y):
    screen_text = font.render(text, True,color)
    gamewindow.blit(screen_text,[x,y])

def plot_snake(gamewindow,color,snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gamewindow, black, [x, y, snake_size, snake_size])

def welcome():
    exit_game = False
    while not exit_game:
        gamewindow.blit(intro, (0, 0))
        # gamewindow.fill(233,210,229)
        text_screen("Welcome to Snakes", black,220,210)
        text_screen("Press Enter to play the game", black,130,280)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game == True
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pygame.mixer.music.fadeout(200)
                    pygame.mixer.music.load('game welcome song 3.mp3')
                    pygame.mixer.music.play(100)
                    pygame.mixer.music.set_volume(.6)
                    game_loop()
        pygame.display.update()
        clock.tick(60)

# game loop
def game_loop():
    # Game specific variabls
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    food_x = random.randint(0, screen_width / 2)
    food_y = random.randint(0, screen_height / 2)
    score = 0
    snake_size = 10
    velocity_x = 0
    velocity_y = 0
    init_velocity = 5
    fps = 60
    if (not os.path.exists("highscore.txt")):
        with open("highscore.txt","w") as f:
            f.write("0")

    with open("highscore.txt","r") as f:
        highscore = f.read()
    snk_list = []
    snk_lenght = 1

    while not exit_game:
        if game_over:
            with open("highscore.txt", "w") as f:
                f.write(str(highscore))

            gamewindow.blit(outro, (0, 0))
            text_screen("Score: " + str(score ), snakegreen, 340, 350)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()

        else:

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game_loop()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

                    # if event.key == pygame.K_q:
                    #     score += 10


            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x) <6 and abs(snake_y - food_y)<6:
                score += 10
                # print("Score",score * 10)

                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_height / 2)
                snk_lenght += 5
                if score > int(highscore):
                    highscore = score

            # gamewindow.fill(white)
            gamewindow.blit(gameimg,(0,0))
            text_screen("Score: " + str(score) + "  Highscore: " + str(highscore), snakegreen, 5, 5)
            pygame.draw.rect(gamewindow, red, [food_x, food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_lenght:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over =True
                pygame.mixer.music.load('explosion.mp3')
                pygame.mixer.music.play(1)
                pygame.mixer.music.set_volume(.6)

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
                pygame.mixer.music.load('explosion.mp3')
                pygame.mixer.music.play(1)
                pygame.mixer.music.set_volume(.6)
                print("Game over")

            # pygame.draw.rect(gamewindow, black, [snake_x, snake_y, snake_size, snake_size])
            plot_snake(gamewindow,black,snk_list,snake_size)

        pygame.display.update()
        clock.tick(fps)


    pygame.quit()
    quit()
welcome()
