
import os
import pygame
from Core import GameInstance

if __name__ == '__main__':
    pygame.init()
    game = GameInstance()
    os.environ['SDL_VIDEO_CENTERED'] = '1'


"""
img2 = pygame.image.load("Layer_0003_6.png")
img = pygame.image.load("Layer_0002_7.png")
rect = img.get_rect()
rect2 = img2.get_rect()
cropRect2 = (0, 150, rect2.w, rect2.h)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if cropRect2[0] >= rect2.w:
        cropRect2 = (rect2.w - 800, 150, rect2.w, rect2.h)
    else:
        cropRect2 = (cropRect2[0] + 1, 150, rect2.w, rect2.h)
    self.window.fill([0, 0, 0])
    self.window.blit(img, [0, 0], cropRect2)
    self.window.blit(img, [800 - cropRect2[0], 0], (0, 150, rect.w, rect.h))
    self.window.blit(img2, [0, 0], cropRect2)
    self.window.blit(img2, [800 - cropRect2[0], 0], (0, 150, rect2.w, rect2.h))
    pygame.display.update()
"""