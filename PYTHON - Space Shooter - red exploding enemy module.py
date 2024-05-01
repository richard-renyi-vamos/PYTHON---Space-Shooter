import pygame
import random

class EnemyShip:
    def __init__(self, screen_width, screen_height):
        self.image = pygame.image.load("enemy_ship.png")  # Load enemy ship image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen_width - self.rect.width)  # Random initial x position
        self.rect.y = random.randint(-screen_height, -self.rect.height)  # Random initial y position above screen
        self.speed = random.randint(3, 5)  # Random speed
        self.explosion_radius = 30  # Radius of explosion
        self.explosion_sound = pygame.mixer.Sound("explosion_sound.wav")  # Load explosion sound

    def move(self):
        self.rect.y += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def explode(self):
        self.explosion_sound.play()
        # Code to create explosion effect around the enemy ship


# Example usage:
if __name__ == "__main__":
    pygame.init()
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()

    enemy_ship = EnemyShip(screen_width, screen_height)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        enemy_ship.move()
        screen.fill((0, 0, 0))  # Clear screen
        enemy_ship.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
