import pygame
import os

class Renderer:
    def __init__(self, width, height, assets_path, animation_speed):
        self.width = width
        self.height = height
        self.timer_text = ""
        self.clock = pygame.time.Clock()
        
        # Set font properties
        self.font_name = os.path.join(assets_path, "./assets/font.ttf")
        self.font_size = int(self.height * 0.2)
        
        # Create screen and font objects
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.NOFRAME)
        self.font = pygame.font.Font(self.font_name, self.font_size)
        self.small_font = pygame.font.Font(None, int(self.height * 0.04))
        
        # Estimate animation speed based on music tempo
        self.animation_speed = animation_speed
        pygame.display.set_caption("Duck Timer!")
    
    def render(self, ducks, timeleft, show_fps, music):
        self.screen.fill((95, 188, 99))
        for duck in ducks:
            if not duck.invisible:
                if os.path.basename(music) == "driftveil_city.mp3" and duck.is_toothless:
                    duck.animate(self.clock.get_time() / 1000)
                else:
                    duck.animate(self.clock.get_time() / 1000, self.animation_speed)
                self.screen.blit(duck.surface, (duck.x, duck.y))
         
        if timeleft['hours'] > 0:
            self.timer_text = f"{timeleft['hours']:02}:{timeleft['minutes']:02}:{timeleft['seconds']:02}"
            
        else:
            self.timer_text = f"{timeleft['minutes']:02}:{timeleft['seconds']:02}"
            
        text_coordinates = (self.width * 0.5 - ((0.75 if timeleft['hours'] <= 0 else 2) * self.font_size), self.height * 0.5 - self.font_size * 0.625)
        timer_text_surface = self.font.render(self.timer_text, True, (0, 0, 0))
        self.screen.blit(timer_text_surface, text_coordinates)
        
        # Draw FPS if necessary
        if show_fps:
            fps_text = self.small_font.render(f"{int(self.clock.get_fps()):02}", True, (255, 0, 0))
            self.screen.blit(fps_text, (self.width - (fps_text.get_width()), 0))

        # Update only the dirty rects
        pygame.display.flip()
        self.clock.tick(144)
    
