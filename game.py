import pygame
import sys
import random
import math

# Initialize pygame
pygame.init()

# Game constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRAVITY = 0.5
BLOCK_SPEED = 5
BASE_WIDTH = 200
BASE_HEIGHT = 20
BLOCK_WIDTH_MIN = 40
BLOCK_WIDTH_MAX = 120
BLOCK_HEIGHT = 20
BLOCK_COLORS = [
    (255, 0, 0),    # Red
    (0, 255, 0),    # Green
    (0, 0, 255),    # Blue
    (255, 255, 0),  # Yellow
    (255, 0, 255),  # Magenta
    (0, 255, 255),  # Cyan
    (255, 165, 0),  # Orange
    (128, 0, 128)   # Purple
]

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Piling Stack Game")
clock = pygame.time.Clock()

# Game state
class Block:
    def __init__(self, x, y, width, height, color, speed=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed
        self.falling = True

    def update(self):
        if self.falling:
            self.speed += GRAVITY
            self.y += self.speed

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
    
    def destroy(self):
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0

    def check_collision(self, other_block):
        # Check if this block collides with another block
        return (
            self.x <= other_block.x + other_block.width and
            self.x + self.width >= other_block.x and
            self.y <= other_block.y + other_block.height and
            self.y + self.height >= other_block.y
        )

    def land_on(self, other_block):
        # Land this block on top of another block
        self.y = other_block.y - self.height
        self.falling = False
        self.speed = 0

class Game:
    def __init__(self):
        self.reset()

    def reset(self):
        # Create the base
        base_x = (SCREEN_WIDTH - BASE_WIDTH) // 2
        base_y = SCREEN_HEIGHT - 200
        self.base = Block(base_x, base_y, BASE_WIDTH, BASE_HEIGHT, (150, 150, 150))
        self.base.falling = False

        # Initialize game state
        self.blocks = [self.base]
        self.current_block = self.create_new_block()
        self.score = 0
        self.game_over = False
        self.win = False

    def create_new_block(self):
        # Create a new falling block
        width = random.randint(BLOCK_WIDTH_MIN, BLOCK_WIDTH_MAX)
        color = random.choice(BLOCK_COLORS)
        
        pos = random.randint(1, 10)
        # Start position in the air, centered
        x = (SCREEN_WIDTH - width) // pos
        y = 50
        
        return Block(x, y, width, BLOCK_HEIGHT, color, 0)

    def update(self):
        if self.game_over:
            return
        
        if self.win:
            return
        
        # Update current block
        self.current_block.update()

        # Check for collisions with existing blocks
        for block in self.blocks:
            if self.current_block.check_collision(block) and self.current_block.falling:
                self.current_block.land_on(block)
                self.current_block.destroy()
                # Calculate overhang
                overhang_left = max(0, block.x - self.current_block.x)
                overhang_right = max(0, (self.current_block.x + self.current_block.width) - (block.x + block.width))
                total_overhang = overhang_left + overhang_right
                
                # If there's too much overhang, game over
                '''if total_overhang > self.current_block.width * 0.8:
                    self.game_over = True
                    return'''
                
                # Add block to the stack
                self.blocks.append(self.current_block)
                self.score += 1
                
                # Create new block
                self.current_block = self.create_new_block()
                break

        # Check if block fell off the screen
        if self.current_block.y > SCREEN_HEIGHT:
            self.game_over = True

        if self.score >= 30:
            self.win = True

    def draw(self):
        # Clear the screen
        screen.fill((0, 0, 0))
        
        # Draw all blocks
        for block in self.blocks:
            block.draw()
        
        # Draw current falling block
        self.current_block.draw()
        
        # Draw score
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f"Score: {self.score}", True, (255, 255, 255))
        screen.blit(score_text, (20, 20))
        
        # Draw game over message
        if self.game_over:
            font = pygame.font.SysFont(None, 72)
            game_over_text = font.render("GAME OVER", True, (255, 0, 0))
            restart_text = font.render("Aperte R para recomeçar", True, (255, 255, 255))
            screen.blit(game_over_text, (SCREEN_WIDTH//2 - game_over_text.get_width()//2, SCREEN_HEIGHT//2 - 50))
            screen.blit(restart_text, (SCREEN_WIDTH//2 - restart_text.get_width()//2, SCREEN_HEIGHT//2 + 20))

        if self.win:
            font = pygame.font.SysFont(None, 82)
            win_game_text = font.render("Você VENCEU!", True, (0,255,100))
            restart_text = font.render("Aperte R para recomeçar", True, (255, 255, 255))
            screen.blit(win_game_text, (SCREEN_WIDTH//2 - win_game_text.get_width()//2, SCREEN_HEIGHT//2 - 50))
            screen.blit(restart_text, (SCREEN_WIDTH//2 - restart_text.get_width()//2, SCREEN_HEIGHT//2 + 20))

    def handle_input(self):
        # Move the current block left or right based on key presses
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.base.x -= 25
            # Ensure it doesn't go off screen
            self.base.x = max(0, self.base.x)
        if keys[pygame.K_RIGHT]:
            self.base.x += 25
            # Ensure it doesn't go off screen
            self.base.x = min(SCREEN_WIDTH - self.base.width, self.base.x)
        if keys[pygame.K_DOWN]:
            # Make the block fall faster
            self.base.speed += 1

        # Check for restart
        if self.game_over and keys[pygame.K_r]:
            self.reset()

def main():
    game = Game()
    
    # Main game loop
    running = True
    while running:
        # Process events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Handle game input
        game.handle_input()
        
        # Update game state
        game.update()
        
        # Draw everything
        game.draw()
        
        # Update the display
        pygame.display.flip()
        
        # Cap the frame rate
        clock.tick()
    
    # Clean up
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
