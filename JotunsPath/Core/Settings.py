import pygame


class Screen(object):
    width = 800
    height = 600
    FPS = 60


class Controls(object):

    def __init__(self):
        self.run_left_arrow = pygame.K_LEFT
        self.run_left_letter = pygame.K_a
        self.run_right_arrow = pygame.K_RIGHT
        self.run_right_letter = pygame.K_d
        self.jump = pygame.K_UP
        self.crouch_arrow = pygame.K_DOWN
        self.crouch_letter = pygame.K_s
        self.attack = pygame.K_p

    def nothing_pressed(self):
        for k in Controls().__dict__.values():
            if pygame.key.get_pressed()[k]:
                return False
        return True
