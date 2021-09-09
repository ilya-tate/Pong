import pygame

pygame.init()

color = {
    'white': (255, 255, 255),
    'black': (0, 0, 0)
}

# Display window
display_dim = {
    'width': 800,
    'height': 600
}
display = pygame.display.set_mode((display_dim['width'], display_dim['height']))
display.fill(color['black'])
# Icon
icon = pygame.image.load('./assets/game-icon.png')
pygame.display.set_icon(icon)
# Name
pygame.display.set_caption("Pong")

paddles = {
    # How much the paddle moves per keystroke
    'vel': 10,
    # Paddle dimensions
    'width': display_dim['width'] / 24,
    'height': display_dim['height'] / 4,
    # Paddle positions on display
    'pos_left': {
        'x': display_dim['width'] / 8,
        'y': display_dim['height'] / 3
    },
    'pos_right': {
        'x': display_dim['width'] / 1.25,
        'y': display_dim['height'] / 3
    },
}

# Paddle starting positions
paddles['left'] = pygame.draw.rect(display, color['white'], (paddles['pos_left']['x'], paddles['pos_left']['y'], paddles['width'], paddles['height']))
paddles['right'] = pygame.draw.rect(display, color['white'], (paddles['pos_right']['x'], paddles['pos_right']['y'], paddles['width'], paddles['height']))

ball = {
    # How much the ball moves per frame
    'vel': 10,
    # Direction of balls movement in degrees
    'direction': 'left',
    # Ball starting position
    'x': (display_dim['width'] / 2) - (display_dim['width'] / 24),
    'y': (display_dim['height'] / 2) - (display_dim['width'] / 24),
    # Ball dimensions
    'width': display_dim['width'] / 24,
    'height': display_dim['width'] / 24
}

ball_pos = pygame.draw.rect(display, color['white'], pygame.Rect(
    (ball['x'], ball['y']),
    (ball['width'], ball['height'])
))

def move_ball():
    '''
    Moves ball every frame
    '''

    # Hits left paddle and changes direction
    if ball['x'] <= paddles['pos_left']['x'] + paddles['width'] and ball['y'] >= paddles['pos_left']['y'] and ball['y'] <= paddles['pos_left']['y'] + paddles['height']:
        ball['direction'] = 'right'

    if ball['x'] + ball['width'] >= paddles['pos_right']['x'] and ball['y'] >= paddles['pos_right']['y'] and ball['y'] <= paddles['pos_right']['y'] + paddles['height']:
        ball['direction'] = 'left'
    
    if ball['direction'] == 'right':
        ball_pos = pygame.draw.rect(display, color['black'], pygame.Rect(
            (ball['x'], ball['y']),
            (ball['width'], ball['height'])
        ))
        ball['x'] += ball['vel']
        pygame.draw.rect(display, color['white'], (ball['x'], ball['y'], ball['width'], ball['height']))
    if ball['direction'] == 'left':
        ball_pos = pygame.draw.rect(display, color['black'], pygame.Rect(
            (ball['x'], ball['y']),
            (ball['width'], ball['height'])
        ))
        ball['x'] -= ball['vel']
        pygame.draw.rect(display, color['white'], (ball['x'], ball['y'], ball['width'], ball['height']))
    
    pygame.draw.rect(display, color['white'], (paddles['pos_left']['x'], paddles['pos_left']['y'], paddles['width'], paddles['height']))
    pygame.draw.rect(display, color['white'], (paddles['pos_right']['x'], paddles['pos_right']['y'], paddles['width'], paddles['height']))

def key_strokes():
    '''
    What happens on each key stroke
    '''

    keys = pygame.key.get_pressed()

    # Left paddle positioning
    if keys[pygame.K_w] and paddles['pos_left']['y'] > 0:
        paddles['left'] = pygame.draw.rect(display, color['black'], (paddles['pos_left']['x'], paddles['pos_left']['y'], paddles['width'], paddles['height']))
        paddles['pos_left']['y'] -= paddles['vel']
        pygame.draw.rect(display, color['white'], (paddles['pos_left']['x'], paddles['pos_left']['y'], paddles['width'], paddles['height']))
    if keys[pygame.K_s] and paddles['pos_left']['y'] + paddles['height'] < display_dim['height']:
        paddles['left'] = pygame.draw.rect(display, color['black'], (paddles['pos_left']['x'], paddles['pos_left']['y'], paddles['width'], paddles['height']))
        paddles['pos_left']['y'] += paddles['vel']
        pygame.draw.rect(display, color['white'], (paddles['pos_left']['x'], paddles['pos_left']['y'], paddles['width'], paddles['height']))
    
    # Right paddle positioning
    if keys[pygame.K_UP] and paddles['pos_right']['y'] > 0:
        paddles['right'] = pygame.draw.rect(display, color['black'], (paddles['pos_right']['x'], paddles['pos_right']['y'], paddles['width'], paddles['height']))
        paddles['pos_right']['y'] -= paddles['vel']
        pygame.draw.rect(display, color['white'], (paddles['pos_right']['x'], paddles['pos_right']['y'], paddles['width'], paddles['height']))
    if keys[pygame.K_DOWN] and paddles['pos_right']['y'] + paddles['height'] < display_dim['height']:
        paddles['right'] = pygame.draw.rect(display, color['black'], (paddles['pos_right']['x'], paddles['pos_right']['y'], paddles['width'], paddles['height']))
        paddles['pos_right']['y'] += paddles['vel']
        pygame.draw.rect(display, color['white'], (paddles['pos_right']['x'], paddles['pos_right']['y'], paddles['width'], paddles['height']))

def run_game():
    running = True
    frame_time = 50
    while running:
        pygame.time.delay(frame_time)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        key_strokes()
        move_ball()
        pygame.display.update()

run_game()
