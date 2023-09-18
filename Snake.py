import pygame
import random
import sys

# Initialize Pygame
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Snake 3")
pygame.mixer.music.load('background.mp3')
pygame.mixer.music.play(-1)
# Set screen dimensions
def game_continue():
    pygame.mixer.music.play(-1)
    screen_width = 600
    screen_height = 600
    paused = False
    game_over = False
    # Set colors
    black = (0, 0, 0)
    blue = (0, 133, 166)
    white = (255, 255, 255)
    red = (255, 0, 0)
    green = (0, 255, 0)
    greent = (0, 180, 22)
    SCREEN_WIDTH1 = 600
    SCREEN_HEIGHT1 = 600
    BLOCK_SIZE = 10
    MIN_BORDER_LENGTH = 4
    MAX_BORDER_LENGTH = 8

    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    # Set width and height for each block of the snake and calculate number of blocks that fit within screen dimensions
    block_size = 10
    num_blocks_x = screen_width // 10
    num_blocks_y = screen_height // 10

    # Create font object for the score display
    font = pygame.font.Font('GUMDROP.ttf', 25)
    fonthi = pygame.font.Font('GUMDROP.ttf', 10)
    # Define function to display score on screen
    def display_score(score):
        if paused == False:
            hi = open("hi_score.txt", "r").read()
            text = font.render("Score " + str(score), True, black)
            hi_score = fonthi.render("High score  " + str(hi), True, (0, 162, 207))
            screen.blit(text, [0, 0])
            screen.blit(hi_score, [0, 20])

    # Define function to draw snake on screen
    def draw_snake(snake_list):
        if paused == False:
            for block in snake_list:
                pygame.draw.rect(screen, green, [block[0], block[1], block_size, block_size])
            pygame.draw.rect(screen, greent, [snake_head[0], snake_head[1], block_size, block_size])
        else:
            screen.fill(black)
            font = pygame.font.Font('GUMDROP.ttf', 30)
            img = font.render('Game paused', True, white)
            screen.blit(img, (220, 250))


    # Define function to display message on screen
    def display_message(msg, color):
        font = pygame.font.Font('GUMDROP.ttf', 25)
        text = font.render(msg, True, color)
        screen.blit(text, [230, 250])
    def display_message1(msg, color):
        font = pygame.font.Font('GUMDROP.ttf', 10)
        text = font.render(msg, True, color)
        screen.blit(text, [240, 270])

    # Set game clock
    clock = pygame.time.Clock()

    # Set initial position and direction of snake
    x = screen_width // 2
    y = screen_height // 2
    delta_x = 0
    delta_y = 0

    # Initialize snake list with head block
    snake_list = [[x, y]]

    # Initialize score and game over flag
    score = 0
    score1 = 0
    game_over = False

    def generate_random_borders():
        x_coordinates = []
        y_coordinates = []

        for _ in range(10):
            length = random.randint(MIN_BORDER_LENGTH, MAX_BORDER_LENGTH)
            if random.choice([True, False]):
                # Horizontal border
                x1 = random.randint(0, SCREEN_WIDTH1 // BLOCK_SIZE - length)
                y1 = random.randint(0, SCREEN_HEIGHT1 // BLOCK_SIZE - 1)
                x_coordinates.extend(range(x1, x1 + length))
                y_coordinates.extend([y1] * length)
            else:
                # Vertical border
                x1 = random.randint(0, SCREEN_WIDTH1 // BLOCK_SIZE - 1)
                y1 = random.randint(0, SCREEN_HEIGHT1 // BLOCK_SIZE - length)
                x_coordinates.extend([x1] * length)
                y_coordinates.extend(range(y1, y1 + length))

        return x_coordinates, y_coordinates
    
    x_coords, y_coords = generate_random_borders()
    
    # Set initial position of apple
    apple_x = round(random.randrange(0, num_blocks_x - 1) * 10)
    apple_y = round(random.randrange(0, num_blocks_y - 1) * 10)

    for i1, i2 in zip(x_coords, y_coords):
        while apple_x == i1 * 10 and apple_y == i2 * 10:
            apple_x = round(random.randrange(0, num_blocks_x - 1) * 10)
            apple_y = round(random.randrange(0, num_blocks_y - 1) * 10)


    def check_collision(moving_block_x, moving_block_y, border_x_coords, border_y_coords):
        for border_x, border_y in zip(border_x_coords, border_y_coords):
            if moving_block_x == border_x * 10 and moving_block_y == border_y * 10:
                return True
            if moving_block_x - 5 == border_x * 10 or moving_block_x + 5 == border_x * 10:
                if moving_block_y - 5 == border_y * 10 or moving_block_y + 5 == border_y * 10:
                    return True
        return False
    # Game loop
    while not game_over:
        collision = check_collision(x, y, x_coords, y_coords)
        if collision:
            mit = int(open("hi_score.txt", "r").read())
            if mit <= score1:
                open("hi_score.txt", "w").write(str(score1))
            display_message("Game Over", red)
            display_message1("Press Q to exit or C", blue)
            pygame.mixer.music.pause()
            pygame.display.update()
            game_over = True
            break
        # Event handling loop
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mit = int(open("hi_score.txt", "r").read())
                    if mit <= score1:
                        open("hi_score.txt", "w").write(str(score1))
                    game_over = True
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if x % 5 != 0:
                            if delta_x > 0:
                                x = x+(5-(x%5))
                            if delta_x < 0:
                                x = x-(x%5)
                        if delta_y == 0:
                            delta_x = 0
                            delta_y = -1
                    elif event.key == pygame.K_DOWN:
                        if x % 5 != 0:
                            if delta_x > 0:
                                x = x+(5-(x%5))
                            if delta_x < 0:
                                x = x-(x%5)
                        if delta_y == 0:
                            delta_x = 0
                            delta_y = 1
                    elif event.key == pygame.K_LEFT:
                        if y % 5 != 0:
                            if delta_y > 0:
                                y = y+(5-(y%5))
                            if delta_y < 0:
                                y = y-(y%5)
                        if delta_x == 0:
                            delta_x = -1
                            delta_y = 0
                    elif event.key == pygame.K_RIGHT:
                        if y % 5 != 0:
                            if delta_y > 0:
                                y = y+(5-(y%5))
                            if delta_y < 0:
                                y = y-(y%5)
                        if delta_x == 0:
                            delta_x = 1
                            delta_y = 0
                    elif event.key == pygame.K_ESCAPE:
                        paused = not paused
        # Move snake by adding new head block in direction of movement and removing tail block
        if paused == False:
            pygame.mixer.music.unpause()
            x += delta_x
            y += delta_y
            snake_head = [x, y]
            snake_list.append(snake_head)
            if len(snake_list) > score + 1:
                del snake_list[0]
        if paused == True:
            pygame.mixer.music.pause()
        # Check if snake has eaten apple
        if x == apple_x or x == apple_x - 5 or x == apple_x + 5:
            if y == apple_y or y == apple_y - 5 or y == apple_y + 5:
                score += 20
                score1 += 1
                apple_x = round(random.randrange(0, num_blocks_x - 1) * 10)
                apple_y = round(random.randrange(0, num_blocks_y - 1) * 10)
                for i1, i2 in zip(x_coords, y_coords):
                    while apple_x == i1 * 10 and apple_y == i2 * 10:
                        apple_x = round(random.randrange(0, num_blocks_x - 1) * 10)
                        apple_y = round(random.randrange(0, num_blocks_y - 1) * 10)

        # Draw screen
        
        screen.fill(white)
        pygame.draw.rect(screen, red, [apple_x, apple_y, 10, 10])
        draw_snake(snake_list)
        display_score(score1)
        font = pygame.font.Font('GUMDROP.ttf', 18)
        img = font.render('Press ESC to pause', True, black)
        screen.blit(img, (430, 0))
        

        for x1, y1 in zip(x_coords, y_coords):
            if paused == False:
                pygame.draw.rect(screen, BLACK, (x1 * BLOCK_SIZE, y1 * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
        pygame.display.flip()
        
        # Update screen and set FPS
        pygame.display.update()
        clock.tick(120)
        # Check if snake has hit border or its own tail
        
        if x < 0 or x >= screen_width or y < 0 or y >= screen_height or snake_head in snake_list[:-1]:
            display_message("Game Over", red)
            display_message1("Press Q to exit or C", blue)
            mit = int(open("hi_score.txt", "r").read())
            if mit <= score1:
                open("hi_score.txt", "w").write(str(score1))
            pygame.mixer.music.pause()
            pygame.display.update()
            game_over = True

# Display game over message and update screen
game_continue()

# Wait for user input to quit or restart game
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                good = False
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_c:
                game_continue()