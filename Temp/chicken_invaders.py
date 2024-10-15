import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
PLAYER_SPEED = 5
ENEMY_SPEED = 3
BULLET_SPEED = 7

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Chicken Invaders")

# Load images
player_img = pygame.Surface((50, 30))
player_img.fill(WHITE)
enemy_img = pygame.Surface((50, 30))
enemy_img.fill(RED)
bullet_img = pygame.Surface((5, 10))
bullet_img.fill(WHITE)

# Player class
class Player:
    def __init__(self):
        self.rect = player_img.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50))

    def move(self, dx):
        self.rect.x += dx
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > SCREEN_WIDTH - self.rect.width:
            self.rect.x = SCREEN_WIDTH - self.rect.width

    def draw(self):
        screen.blit(player_img, self.rect)

# Enemy class
class Enemy:
    def __init__(self):
        self.rect = enemy_img.get_rect(center=(random.randint(50, SCREEN_WIDTH - 50), random.randint(50, 150)))

    def move(self):
        self.rect.y += ENEMY_SPEED
        if self.rect.y > SCREEN_HEIGHT:
            self.rect.y = random.randint(-100, -40)
            self.rect.x = random.randint(50, SCREEN_WIDTH - 50)

    def draw(self):
        screen.blit(enemy_img, self.rect)

# Bullet class
class Bullet:
    def __init__(self, x, y):
        self.rect = bullet_img.get_rect(center=(x, y))

    def move(self):
        self.rect.y -= BULLET_SPEED

    def draw(self):
        screen.blit(bullet_img, self.rect)

    def check_collision(self, enemies):
        for enemy in enemies:
            if self.rect.colliderect(enemy.rect):
                enemies.remove(enemy)
                return True
        return False


# Game loop
def main():
    clock = pygame.time.Clock()
    player = Player()
    enemies = [Enemy() for _ in range(5)]
    bullets = []

    running = True
    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.move(-PLAYER_SPEED)
        if keys[pygame.K_RIGHT]:
            player.move(PLAYER_SPEED)
        if keys[pygame.K_SPACE]:
            if len(bullets) < 5:  # Limit number of bullets on screen
                bullets.append(Bullet(player.rect.centerx, player.rect.top))

        # Update bullets
        for bullet in bullets[:]:
            bullet.move()
            if bullet.rect.bottom < 0:
                bullets.remove(bullet)

        # Check for bullet collisions
        for bullet in bullets[:]:
            bullet.move()
            if bullet.rect.bottom < 0 or bullet.check_collision(enemies):
                bullets.remove(bullet)

        # Update enemies
        for enemy in enemies:
            enemy.move()
            if enemy.rect.top > SCREEN_HEIGHT:
                enemy.rect.y = random.randint(-100, -40)
                enemy.rect.x = random.randint(50, SCREEN_WIDTH - 50)

        # Draw everything
        player.draw()
        for enemy in enemies:
            enemy.draw()
        for bullet in bullets:
            bullet.draw()

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
