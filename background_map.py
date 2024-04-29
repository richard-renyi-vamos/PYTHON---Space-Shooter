# background_map.py

import pygame

# Define colors
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)

# Define obstacle class
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(GRAY)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Define function to create obstacles
def create_obstacles():
    obstacles = pygame.sprite.Group()
    # Add your obstacle positions here
    obstacle_positions = [
        (100, 200, 100, 20),
        (300, 400, 150, 20),
        (500, 100, 120, 20)
    ]
    for pos in obstacle_positions:
        obstacle = Obstacle(*pos)
        obstacles.add(obstacle)
    return obstacles
