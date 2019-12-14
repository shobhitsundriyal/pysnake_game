import pygame
import random

pygame.init()

screen_width = 900
screen_height = 600
game_window = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption('Snake Game :)')
pygame.display.update()

#Game variables
font = pygame.font.SysFont(None, 55)
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

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    game_window.blit(screen_text, [x,y])

def plot_snake(game_window, color, snake_list, size):
    for x,y in snake_list:
        pygame.draw.rect(game_window, color, [x,y,size,size])


#game loop
def game_loop():
    #Game variables
    font = pygame.font.SysFont(None, 55)
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

    while not exit_game:
        if game_over:
            game_window.fill(white)
            text_screen("Game 0ver", red, screen_width/2 - 95, screen_height/2 - 10)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game_loop()


        else:
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

            if len(snake_list) > snake_lenght:
                del snake_list[0]

            #WOW lines
            if head in snake_list[:-1]:
                game_over = True

            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                game_over = True

            #pygame.draw.rect(game_window, black, [snake_x, snake_y, size, size])
            plot_snake(game_window, black, snake_list, size)
        pygame.display.update()
        clock.tick(fps)

game_loop()
pygame.quit()
quit()