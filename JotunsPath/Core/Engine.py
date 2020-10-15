import pygame
from .Settings import Screen
from Content import Assets


class GameInstance(object):

    def __init__(self):
        # Game window
        self.window = pygame.display.set_mode((Screen.width, Screen.height))
        pygame.display.set_caption("Jötun's Path")
        pygame.display.set_icon(Assets.icon())

        self.clock = pygame.time.Clock()

        self.home_screen()

    def home_screen(self):
        titleFont = Assets.create_font("karma", 70)
        buttonsFont = Assets.create_font("fonBold", 21)
        background = Assets.home_background()
        button = Assets.home_button()
        startButtonRect = pygame.Rect((70, 320), button.get_size())
        quitButtonRect = pygame.Rect((70, 430), button.get_size())

        gameTitle = titleFont.render("Jötun's Path", False, Assets.Color.pearl)
        startText = buttonsFont.render("Start Game", False, Assets.Color.black)
        startTextRect = startText.get_rect(center = startButtonRect.center)
        quitText = buttonsFont.render("Quit Game", False, Assets.Color.black)
        quitTextRect = quitText.get_rect(center=quitButtonRect.center)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0);
            self.window.blit(background, [0,0])
            self.window.blit(button, startButtonRect)
            self.window.blit(startText, startTextRect)
            self.window.blit(button, quitButtonRect)
            self.window.blit(quitText, quitTextRect)
            self.window.blit(gameTitle, [20, 150])

            self.clock.tick(Screen.FPS)
            pygame.display.update()
