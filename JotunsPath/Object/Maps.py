import pygame.sprite
import pygame.surface
from Content import Assets


class LevelOne(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = Assets.level_one()
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0

        self.walls = pygame.sprite.Group()
        self.grounds = pygame.sprite.Group()
        soil = self.object(pygame.Rect(0, 515, 800, 80))
        left_edge = self.object(pygame.Rect(0, 0, 0, 600))
        right_edge = self.object(pygame.Rect(800, 0, 0, 600))
        self.walls.add(left_edge, right_edge)
        self.grounds.add(soil)

        # level attributes: size and cursor
        self.x = 800
        self.cursor = 0

    def object(self, rect):
        object = pygame.sprite.Sprite()
        object.image = pygame.Surface(rect.size)
        object.rect = rect
        return object