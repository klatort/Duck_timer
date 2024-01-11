import pygame
import datetime
import librosa
import os
import random

class Duck:
    def __init__(self, x, y, sprite_sheet, sprite_width, sprite_height, invisible=True, can_move=True):
        self.x = x
        self.y = y
        # Generate random direction
        self.direction_x = random.choice([-1, 1])
        self.direction_y = random.choice([-1, 1])
        # Generate random speed
        self.speed_x = random.randint(5, 15)
        self.speed_y = random.randint(5, 15)
        
        self.sprite_sheet = sprite_sheet
        self.sprite_width = sprite_width
        self.sprite_height = sprite_height
        self.sprite_sheet = pygame.image.load(self.sprite_sheet)
        self.sprite_rect = pygame.Rect(0, 0, self.sprite_width, self.sprite_height)
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

class Game:
    def __init__(self, target_time):
        pygame.init()
        self.info_object = pygame.display.Info()
        self.width, self.height = self.info_object.current_w, self.info_object.current_h
        self.music_files = [file for file in os.listdir("./sounds/music/") if file.endswith(".mp3")]
        self.music = "./sounds/music/" + random.choice(self.music_files)
        self.ducks = [
            Duck(-150, 0, "sprites/bird-dance-frames.png", 1200, 1200, False, False),
            Duck(1400, 850, "sprites/dancing-duckdancing-frames.png", 164, 200),
            Duck(100, 700, "sprites/dancing-duckdancing-frames.png", 164, 200),
            Duck(200, 0, "sprites/dancing-duckdancing-frames.png", 164, 200),
            Duck(1700, 550, "sprites/dancing-duckdancing-frames.png", 164, 200),
            Duck(1600, 0, "sprites/dancing-duckdancing-frames.png", 164, 200),
            ]
        self.animation_speed = self.estimate_bpm(self.music)
        self.font_name = "font.ttf"
        self.font_size = 250
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.NOFRAME)
        self.font = pygame.font.Font(self.font_name, self.font_size)
        self.clock = pygame.time.Clock()
        self.animation_time = 0
        self.start_ticks = pygame.time.get_ticks()
        self.target_time = datetime.datetime.combine(datetime.date.today(), target_time)
        self.timeup_sound = pygame.mixer.Sound('./sounds/timeup.mp3')
        self.timeup_loop = pygame.mixer.Sound('./sounds/timeup-loop.mp3')        
        self.sound_channel = pygame.mixer.Channel(0)  # Create a new channel
        pygame.mixer.music.load(self.music)
        pygame.mixer.music.play(-1)
        remaining_time = self.target_time - datetime.datetime.now()
        self.countdown_time = remaining_time.total_seconds()
        self.is_time_up = False
        self.end = False

    def estimate_bpm(self, filename):
        y, sr = librosa.load(filename)
        tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
        return tempo/6000

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.animation_time += self.clock.get_time() / 1000
            if self.animation_time > self.animation_speed:
                self.animation_time = 0
                for ducks in self.ducks:
                    ducks.animate()
            # Move ducks
            for duck in self.ducks:
                duck.move(self.width, self.height)
            
            if not self.is_time_up:
                total_seconds = self.countdown_time - (pygame.time.get_ticks() - self.start_ticks) // 1000
                minutes = int(total_seconds // 60)
                seconds = int(total_seconds % 60)
                if(total_seconds < 0):
                    pygame.mixer.music.stop()
                    self.sound_channel.play(self.timeup_sound)
                    self.is_time_up = True
                    for duck in self.ducks:
                        duck.invisible = False
                    minutes = 0
                    seconds = 0
                timer_text = self.font.render(f"{minutes:02}:{seconds:02}", True, (0, 0, 0))
            elif self.is_time_up == True and not self.sound_channel.get_busy() and not self.end:
                self.sound_channel.play(self.timeup_loop, -1)
                self.end = True
                
            self.screen.fill((95, 188, 99))
            self.screen.blit(timer_text, (self.width / 2 - 125, self.height / 2 - 125)) 
            for ducks in self.ducks:
                ducks.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

# Usage
game = Game(datetime.time(18, 51))
game.run()