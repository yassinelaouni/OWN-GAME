import pygame
import random

# Window size
frame_size_x = 720
frame_size_y = 480

# Colors (R, G, B)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)

# Difficulty settings
# Easy      ->  10
# Medium    ->  25
# Hard      ->  40
# Harder    ->  60
# Impossible->  120
difficulty = 20

# Initialize Pygame
pygame.init()

# Initialize game window
pygame.display.set_caption('Snake')
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))

# FPS (frames per second) controller
fps_controller = pygame.time.Clock()

# Snake and food positions
snake_pos = [100, 50]
snake_body = [[100, 50], [100-10, 50], [100-(2*10), 50]]

food_pos = [random.randrange(1, (frame_size_x // 10)) * 10, random.randrange(1, (frame_size_y // 10)) * 10]
food_spawn = True

direction = 'RIGHT'
change_to = direction

score = 0

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == ord('w'):
                change_to = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                change_to = 'RIGHT'

    # Update snake's direction if it's not the opposite direction
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Update snake's position
    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10

    # Snake body growing mechanism
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    # Spawn food if needed
    if not food_spawn:
        food_pos = [random.randrange(1, (frame_size_x // 10)) * 10, random.randrange(1, (frame_size_y // 10)) * 10]
        food_spawn = True

    # Refresh game window
    game_window.fill(black)

    # Draw snake
    for pos in snake_body:
        pygame.draw.rect(game_window, red, pygame.Rect(pos[0], pos[1], 10, 10))

    # Draw food
    pygame.draw.rect(game_window, green, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # Check if snake is out of bounds or collides with its own body
    if snake_pos[0] < 0 or snake_pos[0] > frame_size_x-10:
        pygame.quit()
        quit()
    if snake_pos[1] < 0 or snake_pos[1] > frame_size_y-10:
        pygame.quit()
        quit()
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            pygame.quit()
            quit()

    # Display score
    font = pygame.font.SysFont('Arial', 20)
    score_surface = font.render('Score: ' + str(score), True, white)
    score_rect = score_surface.get_rect()
    score_rect.midtop = (frame_size_x // 2, 10)
    game_window.blit(score_surface, score_rect)

    # Update game display
    pygame.display.update()

    # Control game speed
    fps_controller.tick