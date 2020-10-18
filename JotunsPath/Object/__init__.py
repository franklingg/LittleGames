import pygame.rect


class Animation(object):

    imgRect = None

    def __init__(self, img):
        self.img = img
        self.imgRect = self.img.get_rect()
        self.frames = self.imgRect.w // self.imgRect.h
        self.frame = 0

    def animate(self):
        animation = {"img": self.img,
                     "crop": pygame.Rect(self.imgRect.h * self.frame, 0, self.imgRect.h, self.imgRect.h)}
        self.frame = self.frame + 1 if self.frame < self.frames - 1 else 0
        return animation