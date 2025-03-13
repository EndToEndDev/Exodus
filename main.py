import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 640, 480
TILE_SIZE = 32  # Grid-based movement reference
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)

# Setup window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Top-Down RPG")

# Load assets
player_img = pygame.image.load("assets/player.png")  # Use a 32x32 sprite
enemy_img = pygame.image.load("assets/enemy.png")  # Use a 32x32 enemy sprite
wall_img = pygame.image.load("assets/wall.png")  # 32x32 obstacle

# Scale images (if needed)
player_img = pygame.transform.scale(player_img, (TILE_SIZE, TILE_SIZE))
enemy_img = pygame.transform.scale(enemy_img, (TILE_SIZE, TILE_SIZE))
wall_img = pygame.transform.scale(wall_img, (TILE_SIZE, TILE_SIZE))

# Font for game over message
font = pygame.font.Font(None, 48)

# Player settings
player_speed = 2

class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)

    def move(self, dx, dy, walls):
        # Predict movement
        new_rect = self.rect.move(dx, dy)
        if not any(new_rect.colliderect(wall.rect) for wall in walls):
            self.rect = new_rect

    def draw(self, surface):
        surface.blit(player_img, self.rect)

class Enemy:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
        self.speed = 1
        self.direction = random.choice(["left", "right", "up", "down"])
        self.timer = random.randint(30, 90)

    def update(self, walls):
        if self.timer <= 0:
            self.direction = random.choice(["left", "right", "up", "down"])
            self.timer = random.randint(30, 90)
        self.timer -= 1

        dx, dy = 0, 0
        if self.direction == "left":
            dx = -self.speed
        elif self.direction == "right":
            dx = self.speed
        elif self.direction == "up":
            dy = -self.speed
        elif self.direction == "down":
            dy = self.speed

        # Predict movement & check collision
        new_rect = self.rect.move(dx, dy)
        if not any(new_rect.colliderect(wall.rect) for wall in walls):
            self.rect = new_rect

    def draw(self, surface):
        surface.blit(enemy_img, self.rect)

class Wall:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)

    def draw(self, surface):
        surface.blit(wall_img, self.rect)

# Map layout (1 = wall, 0 = floor, 2 = enemy spawn)
MAP = [
    "11111111111111111111",
    "10000000011111111111",
    "10001000011111111111",
    "10000100011111111111",
    "10000000200000000001",
    "10000000000200000001",
    "10000000020000000001",
    "10000200000000000001",
    "10200000000020000001",
    "10000000000020000001",
    "10000000000000000001",
    "10000000200000000001",
    "10000000000020000001",
    "10000000002000000001",
    "10000000002000000001"
]

# Convert map to objects
walls = []
enemies = []
for row_idx, row in enumerate(MAP):
    for col_idx, tile in enumerate(row):
        x, y = col_idx * TILE_SIZE, row_idx * TILE_SIZE
        if tile == "1":
            walls.append(Wall(x, y))
        elif tile == "2":
            enemies.append(Enemy(x, y))

# Initialize player
player = Player(64, 64)

# Game loop
clock = pygame.time.Clock()
running = True

while running:
    screen.fill(BLACK)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    dx = (keys[pygame.K_RIGHT] or keys[pygame.K_d]) - (keys[pygame.K_LEFT] or keys[pygame.K_a])
    dy = (keys[pygame.K_DOWN] or keys[pygame.K_s]) - (keys[pygame.K_UP] or keys[pygame.K_w])
    player.move(dx * player_speed, dy * player_speed, walls)

    # Update enemies
    for enemy in enemies:
        enemy.update(walls)

    # Check for collision with enemies
    for enemy in enemies:
        if player.rect.colliderect(enemy.rect):
            # Display "Game Over" message
            text = font.render("Game Over", True, RED)
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
            pygame.display.flip()
            pygame.time.delay(2000)  # Show message for 2 seconds
            running = False

    # Draw everything
    for wall in walls:
        wall.draw(screen)
    player.draw(screen)
    for enemy in enemies:
        enemy.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
