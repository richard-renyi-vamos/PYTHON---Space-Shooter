# main_game.py

import pygame
import random
from background_map import create_obstacles

# Initialize Pygame
pygame.init()

# Set up the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Shooter")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Load images
player_img = pygame.image.load("player_ship.png")  # Replace with actual image file
enemy_img = pygame.image.load("enemy_ship.png")    # Replace with actual image file
laser_img = pygame.Surface((10, 20))
laser_img.fill(RED)

# Set up player
player_rect = player_img.get_rect()
player_rect.centerx = SCREEN_WIDTH // 2
player_rect.bottom = SCREEN_HEIGHT - 10
player_speed = 5

# Set up enemy
enemy_rect = enemy_img.get_rect()
enemy_rect.centerx = random.randint(0, SCREEN_WIDTH)
enemy_rect.bottom = 0
enemy_speed = 3

# Set up lasers
laser_rect = laser_img.get_rect()
laser_speed = 7
laser_list = []

# Set up obstacles
obstacles = create_obstacles()

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_rect.left > 0:
        player_rect.x -= player_speed
    if keys[pygame.K_RIGHT] and player_rect.right < SCREEN_WIDTH:
        player_rect.x += player_speed
    
    # Move enemy
    enemy_rect.y += enemy_speed
    
    # Enemy shoots lasers
    if random.randint(1, 100) == 1:
        laser = laser_rect.copy()
        laser.centerx = enemy_rect.centerx
        laser.bottom = enemy_rect.bottom
        laser_list.append(laser)
    
    # Move lasers
    for laser in laser_list:
        laser.y += laser_speed
        if laser.bottom < 0:
            laser_list.remove(laser)
    
    # Draw everything
    screen.blit(player_img, player_rect)
    screen.blit(enemy_img, enemy_rect)
    for laser in laser_list:
        screen.blit(laser_img, laser)
    obstacles.draw(screen)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
