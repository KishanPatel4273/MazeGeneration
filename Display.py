import pygame
import math
from Screen import *

class Display():
        def __init__(self, width, height):
                pygame.init()
                self.width = width
                self.height = height
                self.display = pygame.display.set_mode((width,height))
                pygame.display.set_caption("MAZE")
                self.clock = pygame.time.Clock()
                self.running = True
                self.screen = Screen(0, 5, self.width, self.height, 10, 20)
        

        def run(self):
                while self.running:
                        for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        self.running = False
                        self.tick()
                        self.render()
                        pygame.display.flip()
                        self.clock.tick(60)#set frame rat5

        def tick(self):
                self.screen.tick_screen()
               
        def render(self):
                self.display.fill((255,255,255))
                pixels = pygame.surfarray.array2d(self.display)
                self.screen.render_screen(pixels)
                pygame.surfarray.blit_array(self.display, pixels)      
                
def main():
        screen = Display(1024, 600)
        screen.run()

if __name__ == '__main__':
        main()