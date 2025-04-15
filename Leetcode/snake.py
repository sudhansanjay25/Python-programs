import pygame
import time
import random

# Initialize pygame
pygame.init()

# Window size
WIDTH = 600
HEIGHT = 400
BLOCK_SIZE = 10
SPEED = 15

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (213, 50, 80)

# Initialize game window
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Clock
clock = pygame.time.Clock()

# Font
font = pygame.font.SysFont("comicsans", 25)

def draw_snake(snake_body):
    for block in snake_body:
        pygame.draw.rect(win, GREEN, [block[0], block[1], BLOCK_SIZE, BLOCK_SIZE])

def game_loop():
    game_over = False
    game_close = False

    # Snake position and body
    x, y = WIDTH // 2, HEIGHT // 2
    x_change, y_change = 0, 0
    snake_body = [[x, y]]
    snake_length = 1

    # Food position
    food_x = random.randrange(0, WIDTH - BLOCK_SIZE, BLOCK_SIZE)
    food_y = random.randrange(0, HEIGHT - BLOCK_SIZE, BLOCK_SIZE)

    while not game_over:
        while game_close:
            win.fill(BLACK)
            msg = font.render("Game Over! Press Q-Quit or R-Restart", True, RED)
            win.blit(msg, [WIDTH // 6, HEIGHT // 3])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        game_loop()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x_change == 0:
                    x_change = -BLOCK_SIZE
                    y_change = 0
                elif event.key == pygame.K_RIGHT and x_change == 0:
                    x_change = BLOCK_SIZE
                    y_change = 0
                elif event.key == pygame.K_UP and y_change == 0:
                    y_change = -BLOCK_SIZE
                    x_change = 0
                elif event.key == pygame.K_DOWN and y_change == 0:
                    y_change = BLOCK_SIZE
                    x_change = 0

        # Update snake position
        x += x_change
        y += y_change

        # Check boundaries
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            game_close = True

        win.fill(BLACK)
        pygame.draw.rect(win, RED, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])
        snake_body.append([x, y])

        if len(snake_body) > snake_length:
            del snake_body[0]

        # Check for collision with itself
        for block in snake_body[:-1]:
            if block == [x, y]:
                game_close = True

        draw_snake(snake_body)
        pygame.display.update()

        # Check if snake eats food
        if x == food_x and y == food_y:
            food_x = random.randrange(0, WIDTH - BLOCK_SIZE, BLOCK_SIZE)
            food_y = random.randrange(0, HEIGHT - BLOCK_SIZE, BLOCK_SIZE)
            snake_length += 1

        clock.tick(SPEED)

    pygame.quit()
    quit()

game_loop()
