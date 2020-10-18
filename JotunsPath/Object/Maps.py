import pygame.sprite
import pygame.surface
from Content import Assets


class LevelOne(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = Assets.level_one()
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0

        self.objects = pygame.sprite.Group()
        soil = self.object(pygame.Rect(0, 440, 800, 160))
        left_edge = self.object(pygame.Rect(0, 0, 3, 600))
        right_edge = self.object(pygame.Rect(797, 0, 3, 600))
        self.objects.add(soil, left_edge, right_edge)

    def object(self, rect):
        object = pygame.sprite.Sprite()
        object.image = pygame.Surface(rect.size)
        object.rect = rect
        return object