import pygame.rect


class Animation(object):

    imgRect = None

    def __init__(self, asset):
        self.img = asset[0]
        self.imgRect = self.img.get_rect()
        self.frames = asset[1]
        self.frame_w = self.imgRect.w // self.frames
        self.frame = 0

    def animate(self):
        animation = {"img": self.img,
                     "crop": pygame.Rect(self.frame_w * self.frame, 0, self.frame_w, self.imgRect.h)}
        self.frame = self.frame + 1 if self.frame < self.frames - 1 else 0
        return animation