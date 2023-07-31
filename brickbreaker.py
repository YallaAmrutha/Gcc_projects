import pygame
import random

# Initialize pygame
pygame.init()

# Constants for the game
WIDTH, HEIGHT = 800, 600
PADDLE_WIDTH, PADDLE_HEIGHT = 150, 20
BALL_SIZE = 20
BRICK_WIDTH, BRICK_HEIGHT = 80, 30
PADDLE_SPEED = 8
BALL_SPEED_X, BALL_SPEED_Y = 6, 6
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the game window
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Brick Breaker")

# Paddle class
class Paddle:
    def __init__(self):
        self.rect = pygame.Rect((WIDTH - PADDLE_WIDTH) // 2, HEIGHT - PADDLE_HEIGHT, PADDLE_WIDTH, PADDLE_HEIGHT)
    
    def move_left(self):
        self.rect.x -= PADDLE_SPEED
        if self.rect.left < 0:
            self.rect.left = 0
    
    def move_right(self):
        self.rect.x += PADDLE_SPEED
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
    
    def draw(self, win):
        pygame.draw.rect(win, WHITE, self.rect)

# Ball class
class Ball:
    def __init__(self):
        self.rect = pygame.Rect((WIDTH - BALL_SIZE) // 2, HEIGHT - PADDLE_HEIGHT - BALL_SIZE, BALL_SIZE, BALL_SIZE)
        self.direction_x = random.choice([1, -1])
        self.direction_y = -1

    def move(self):
        self.rect.x += BALL_SPEED_X * self.direction_x
        self.rect.y += BALL_SPEED_Y * self.direction_y
    
    def bounce(self):
        self.direction_y *= -1
    
    def check_collisions(self, paddle, bricks):
        # Check paddle collision
        if self.rect.colliderect(paddle.rect) and self.direction_y == 1:
            self.bounce()

        # Check brick collision
        for brick in bricks:
            if self.rect.colliderect(brick):
                bricks.remove(brick)
                self.bounce()
                break

        # Check wall collision
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.direction_x *= -1
        if self.rect.top < 0:
            self.direction_y *= -1

    def draw(self, win):
        pygame.draw.circle(win, WHITE, self.rect.center, BALL_SIZE // 2)

# Brick class
class Brick:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, BRICK_WIDTH, BRICK_HEIGHT)

    def draw(self, win):
        pygame.draw.rect(win, WHITE, self.rect)

# Main game loop
def game_loop():
    paddle = Paddle()
    ball = Ball()
    bricks = [Brick(x, y) for x in range(0, WIDTH - BRICK_WIDTH, BRICK_WIDTH) for y in range(0, HEIGHT // 2, BRICK_HEIGHT)]

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            paddle.move_left()
        if keys[pygame.K_RIGHT]:
            paddle.move_right()

        ball.move()
        ball.check_collisions(paddle, bricks)

        if ball.rect.bottom >= HEIGHT:
            print("Game Over!")
            pygame.quit()
            quit()

        win.fill(BLACK)
        paddle.draw(win)
        ball.draw(win)

        for brick in bricks:
            brick.draw(win)

        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    game_loop()
