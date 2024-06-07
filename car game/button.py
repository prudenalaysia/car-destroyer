import pygame
from sys import exit
screen = pygame.display.set_mode((600, 400))

class Button():
    def __init__(self, image, pos):
        self.image = pygame.transform.scale(image, (200,200))
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
    
    def update(self):
        screen.blit(self.image, self.rect)
    
    def input(self, position):
        if position[0] in range (self.rect.left, self.rect.right) and position[1] in range (self.rect.top, self.rect.bottom):
            return True
        return False