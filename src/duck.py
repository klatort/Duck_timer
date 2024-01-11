from pygame import Rect, image
from random import randint, choice

class Duck:
    def __init__(self, x, y, sprite_sheet, sprite_width, sprite_height, invisible=True, can_move=True):
        self.x = x
        self.y = y
        # Generate random direction
        self.direction_x = choice([-1, 1])
        self.direction_y = choice([-1, 1])
        # Generate random speed
        self.speed_x = randint(5, 15)
        self.speed_y = randint(5, 15)
        
        self.sprite_sheet = sprite_sheet
        self.sprite_width = sprite_width
        self.sprite_height = sprite_height
        self.sprite_sheet = image.load(self.sprite_sheet)
        self.sprite_rect = Rect(0, 0, self.sprite_width, self.sprite_height)
        self.current_frame = 0
        self.invisible = invisible
        self.can_move = can_move
        
    def draw(self, screen):
        if not self.invisible:
            screen.blit(self.sprite_sheet, (self.x, self.y), self.sprite_rect)
            
    def move(self, width, height):
        if self.can_move:
            # Calculate new position
            new_x = self.x + self.direction_x * self.speed_x
            new_y = self.y + self.direction_y * self.speed_y

            # Check if new position is within screen boundaries
            if new_x < 0 or new_x + self.sprite_width > width:
                self.direction_x *= -1  # Reverse direction on x-axis
            if new_y < 0 or new_y + self.sprite_height > height:
                self.direction_y *= -1  # Reverse direction on y-axis

            # Update position
            self.x += self.direction_x * self.speed_x
            self.y += self.direction_y * self.speed_y
    
    def animate(self):
        self.current_frame = (self.current_frame + 1) % (self.sprite_sheet.get_width() // self.sprite_width)
        self.sprite_rect.x = self.current_frame * self.sprite_width