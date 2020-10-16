import pygame
from .Settings import Screen
from Content import Assets


class GameInstance(object):

    def __init__(self):
        self.window = pygame.display.set_mode((Screen.width, Screen.height))
        pygame.display.set_caption("Jötun's Path")
        pygame.display.set_icon(Assets.icon())

        self.clock = pygame.time.Clock()

        self.home_screen()

    def home_screen(self):
        titleFont = Assets.create_font("karma", 70)
        background = Assets.home_background()

        startButton = Button(Assets.home_button(), (70,320))
        startButton.in_text("fonBold", 21, "Start Game", Assets.Color.black, Assets.Color.light_black)
        quitButton = Button(Assets.home_button(), (70, 430))
        quitButton.in_text("fonBold", 21, "Quit Game", Assets.Color.black, Assets.Color.light_black)

        gameTitle = titleFont.render("Jötun's Path", False, Assets.Color.pearl)
        runningHome = True
        while runningHome:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
                if pygame.mouse.get_pressed()[0] and quitButton.imgRect.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                    exit(0)
                if pygame.mouse.get_pressed()[0] and startButton.imgRect.collidepoint(pygame.mouse.get_pos()):
                    runningHome = False
            self.window.blit(background, [0,0])
            self.window.blit(gameTitle, [20, 150])
            startButton.blit(self.window)
            quitButton.blit(self.window)

            self.clock.tick(Screen.FPS)
            pygame.display.update()


class Button(object):

    def __init__(self, img, pos):
        self.img = img
        self.pos = pos
        self.imgRect = pygame.Rect(pos, self.img.get_size())

    def in_text(self, font, fontSize, text, color, hoveredColor = None):
        self.font = Assets.create_font(font, fontSize)
        self.text = self.font.render(text, False, color)
        self.textRect = self.text.get_rect(center = self.imgRect.center)
        self.hoveredText = None if hoveredColor is None else self.font.render(text, False, hoveredColor)

    def blit(self, window):
        window.blit(self.img, self.imgRect)
        if self.imgRect.collidepoint(pygame.mouse.get_pos()):
            window.blit(self.hoveredText, self.textRect)
        else:
            window.blit(self.text, self.textRect)