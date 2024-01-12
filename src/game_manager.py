import pygame
import librosa
import os
import random
import datetime
from src.duck import Duck

class GameManager:
    def __init__(self, hours, minutes, seconds):
        pygame.init()
        self.info_object = pygame.display.Info()
        self.width, self.height = self.info_object.current_w, self.info_object.current_h
        self.music_files = [file for file in os.listdir("./sounds/music/") if file.endswith(".mp3")]
        self.music = "./sounds/music/" + random.choice(self.music_files)
        self.ducks = [
            Duck(-150, 0, "./assets/sprites/bird-dance-frames.png", 1200, 1200, False, False),
            Duck(1400, 850, "./assets/sprites/dancing-duckdancing-frames.png", 164, 200),
            Duck(100, 700, "./assets/sprites/dancing-duckdancing-frames.png", 164, 200),
            Duck(200, 0, "./assets/sprites/dancing-duckdancing-frames.png", 164, 200),
            Duck(1700, 550, "./assets/sprites/dancing-duckdancing-frames.png", 164, 200),
            Duck(1260, 400, "./assets/sprites/dancing-duckdancing-frames.png", 164, 200),
            Duck(960, 300, "./assets/sprites/dancing-duckdancing-frames.png", 164, 200),
            Duck(860, 700, "./assets/sprites/dancing-duckdancing-frames.png", 164, 200),
            Duck(360, 900, "./assets/sprites/dancing-duckdancing-frames.png", 164, 200),
            Duck(800, 1600, "./assets/sprites/dancing-duckdancing-frames.png", 164, 200),
            ]
        self.animation_speed = self.estimate_bpm(self.music)
        self.font_name = "./assets/font.ttf"
        self.font_size = 250
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.NOFRAME)
        self.font = pygame.font.Font(self.font_name, self.font_size)
        self.clock = pygame.time.Clock()
        self.start_ticks = pygame.time.get_ticks()
        self.target_time = datetime.datetime.combine(datetime.date.today(), datetime.time(hours, minutes, seconds))
        self.timeup_sound = pygame.mixer.Sound('./sounds/timeup.mp3')      
        pygame.mixer.music.load(self.music)
        pygame.mixer.music.play(-1)
        remaining_time = self.target_time - datetime.datetime.now()
        self.countdown_time = remaining_time.total_seconds()
        self.is_time_up = False

    def estimate_bpm(self, filename):
        y, sr = librosa.load(filename)
        tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
        return tempo

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            for ducks in self.ducks:
                ducks.animate(self.clock.get_time() / 1000, self.animation_speed)
            # Move ducks
            for duck in self.ducks:
                duck.move(self.width, self.height)
            
            if not self.is_time_up:
                total_seconds = self.countdown_time - (pygame.time.get_ticks() - self.start_ticks) // 1000
                minutes = int(total_seconds // 60)
                seconds = int(total_seconds % 60)
                if(total_seconds < 0):
                    self.timeup_sound.play()
                    self.is_time_up = True
                    for duck in self.ducks:
                        duck.invisible = False
                    minutes = 0
                    seconds = 0
                timer_text = self.font.render(f"{minutes:02}:{seconds:02}", True, (0, 0, 0))
                
            self.screen.fill((95, 188, 99))
            self.screen.blit(timer_text, (self.width / 2 - 125, self.height / 2 - 125)) 
            for ducks in self.ducks:
                ducks.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
