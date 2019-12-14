import pygame
import random

pygame.init()

screen_width = 900
screen_height = 600
game_window = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption('Snake Game :)')
pygame.display.update()

#Game variables
exit_game = False
game_over = False
snake_x = 45
snake_y = 55
size = 30
fps = 30
velocity_x = 0
velocity_y = 0

food_x = random.randint(10, screen_width-20)
food_y = random.randint(10, screen_height-20)

score = 0

snake_list = []
snake_lenght = 1

#colors
white = (255,255,255)
red = (200,0,0)
black = (0,0,0)

clock = pygame.time.Clock()
#game loop
while not exit_game:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:#press any key
            if event.key == pygame.K_RIGHT:
                velocity_x = 10
                velocity_y = 0

            if event.key == pygame.K_LEFT:
                velocity_x = -10
                velocity_y = 0

            if event.key == pygame.K_DOWN:
                velocity_y = 10
                velocity_x = 0

            if event.key == pygame.K_UP:
                velocity_y = -10
                velocity_x = 0

    snake_x += velocity_x
    snake_y += velocity_y

    if abs(snake_x - food_x) < 10 and abs(snake_y - food_y) < 10:
        score += 1
        print('Score: ' + str(score))
        food_x = random.randint(10, screen_width-20)
        food_y = random.randint(10, screen_height-20)
        snake_lenght += 5 


    game_window.fill(white)
    pygame.draw.circle(game_window, red, (food_x,food_y), 15)

    head = []
    head.append(snake_x)
    head.append(snake_y)
    snake_list.append(head)

    pygame.draw.rect(game_window, black, [snake_x, snake_y, size, size])
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()