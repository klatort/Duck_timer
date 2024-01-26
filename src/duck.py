import json
import os
from pygame import Rect, image, transform
from random import randint, choice

class Duck:
    def __init__(self, x, y, sprite_sheet, sprite_width, sprite_height, invisible, can_move, is_toothless):
        self.sprite_sheet = sprite_sheet
        self.sprite_width = sprite_width
        self.sprite_height = sprite_height

        if isinstance(sprite_sheet, str):
            self.sprite_sheet = image.load(self.sprite_sheet).convert_alpha()
        else:
            self.sprite_sheet = sprite_sheet

        self.sprite_rect = Rect(0, 0, self.sprite_width, self.sprite_height)
        self.animation_time = 0
        self.current_frame = 0
        self.invisible = invisible
        self.can_move = can_move
        self.is_toothless = is_toothless
        self.x = x
        self.y = y

        # Generate random direction
        self.direction_x = choice([-1, 1])
        self.direction_y = choice([-1, 1])

        # Generate random speed
        self.speed_x = randint(2, 8)
        self.speed_y = randint(2, 8)
    
    def draw(self):
        return self.sprite_sheet.subsurface(self.sprite_rect)
        
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

    def animate(self, time_elapsed, animation_speed=None):
        
        # Toothless is a special case only if driftveil_city is playing
        if animation_speed is None:
            animation_speed = 0.026
        else:
            animation_speed = animation_speed / 6000
            if animation_speed < 0.02:
                animation_speed *= 2
                
        self.animation_time += time_elapsed

        if self.animation_time > animation_speed:
            self.animation_time = 0
            self.current_frame = (self.current_frame + 1) % (self.sprite_sheet.get_width() // self.sprite_width)
            self.sprite_rect.x = self.current_frame * self.sprite_width

    @classmethod
    def from_json(cls, json_file, proportions):
        with open(json_file, 'r') as file:
            try:
                data = json.load(file)
            except json.decoder.JSONDecodeError:
                print(f'Error: {json_file} is not a valid JSON file')
                return
        is_toothless = False
        if os.path.basename(json_file) == 'toothless.json':
            is_toothless = True
        x = data.get('x') * proportions[0]/1920
        y = data.get('y') * proportions[1]/1080
        sprite_sheet = os.path.join(os.path.dirname(os.path.dirname(json_file)), data.get('sprite_sheet'))
        invisible = data.get('invisible', True)
        can_move = data.get('can_move', True)
        frames = data.get('frames')

        if None in [x, y, sprite_sheet, frames]:
            raise ValueError("The JSON file must contain 'x', 'y', 'sprite_sheet', and 'frames' values.")

        sprite_sheet = image.load(sprite_sheet).convert_alpha()
        scaled_width = int(sprite_sheet.get_width() * proportions[0]/1920)
        scaled_height = int(sprite_sheet.get_height() * proportions[1]/1080)
        sprite_sheet = transform.scale(sprite_sheet, (scaled_width, scaled_height))
        sprite_width = sprite_sheet.get_width() / frames
        sprite_height = sprite_sheet.get_height()

        return cls(x, y, sprite_sheet, sprite_width, sprite_height, invisible, can_move, is_toothless)
