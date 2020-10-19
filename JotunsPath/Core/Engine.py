import pygame
from .Settings import Screen
from Content import Assets
from Object.Character import Character
from Object import Maps


class GameInstance(object):

    def __init__(self):
        self.window = pygame.display.set_mode((Screen.width, Screen.height))
        pygame.display.set_caption("Jötun's Path")
        pygame.display.set_icon(Assets.icon())
        self.clock = pygame.time.Clock()

        self.home_screen()

        self.maps = pygame.sprite.Group(Maps.LevelOne())
        self.adventurer = Character(self.maps.sprites()[0])
        self.game()

    def create_button(self, img, pos):
        return Button(self.window, img, pos)

    def home_screen(self):
        titleFont = Assets.create_font("karma", 70)
        self.background = Assets.home_background()

        start_button = self.create_button(Assets.home_button_image(), (70, 320))
        start_button.in_text("fonBold", 21, "Start Game", Assets.Color.black, Assets.Color.light_black)
        quit_button = self.create_button(Assets.home_button_image(), (70, 430))
        quit_button.in_text("fonBold", 21, "Quit Game", Assets.Color.black, Assets.Color.light_black)

        gameTitle = titleFont.render("Jötun's Path", False, Assets.Color.pearl)
        runningHome = True
        while runningHome:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or \
                        (pygame.mouse.get_pressed()[0] and quit_button.img_rect.collidepoint(pygame.mouse.get_pos())):
                    pygame.quit()
                    exit(0)
                if pygame.mouse.get_pressed()[0] and start_button.img_rect.collidepoint(pygame.mouse.get_pos()):
                    runningHome = False
            self.window.blit(self.background, [0, 0])
            self.window.blit(gameTitle, [20, 150])
            start_button.blit()
            quit_button.blit()

            self.clock.tick(Screen.FPS)
            pygame.display.update()

    def player_action(self):
        if pygame.key.get_pressed()[pygame.K_UP] and not self.adventurer.inair:
            self.adventurer.jump()

        elif pygame.key.get_pressed()[pygame.K_DOWN] or pygame.key.get_pressed()[pygame.K_s] \
                and not self.adventurer.inair:
            self.clock.tick(10)
            self.adventurer.crouch()
            self.update_game()

        elif pygame.key.get_pressed()[pygame.K_LEFT] or pygame.key.get_pressed()[pygame.K_a]:
            if self.adventurer.inair:
                if pygame.key.get_pressed()[pygame.K_p]:
                    for i in range(7):
                        self.adventurer.airattack("LEFT")
                        self.clock.tick(15)
                        self.update_game()
                    return None
                self.adventurer.run("LEFT", slow=True)
                self.adventurer.freefall()
                self.update_game()
                return None
            elif pygame.key.get_pressed()[pygame.K_p]:
                for i in range(6):
                    self.clock.tick(15)
                    self.adventurer.attack("LEFT")
                    self.update_game()
            self.clock.tick(25)
            self.adventurer.run("LEFT")
            self.update_game()

        elif pygame.key.get_pressed()[pygame.K_RIGHT] or pygame.key.get_pressed()[pygame.K_d]:
            if self.adventurer.inair:
                if pygame.key.get_pressed()[pygame.K_p]:
                    for i in range(7):
                        self.adventurer.airattack("RIGHT")
                        self.clock.tick(15)
                        self.update_game()
                    return None
                self.adventurer.run("RIGHT", slow=True)
                self.adventurer.freefall()
                self.update_game()
                return None
            elif pygame.key.get_pressed()[pygame.K_p]:
                for i in range(6):
                    self.clock.tick(15)
                    self.adventurer.attack("RIGHT")
                    self.update_game()
            self.adventurer.run("RIGHT")
            self.update_game()
            self.clock.tick(25)

        elif self.adventurer.inair:
            if pygame.key.get_pressed()[pygame.K_p]:
                for i in range(7):
                    self.adventurer.airattack()
                    self.clock.tick(15)
                    self.update_game()
                return None
            self.adventurer.freefall()
            self.update_game()

        elif pygame.key.get_pressed()[pygame.K_p]:
            for i in range(6):
                self.adventurer.attack()
                self.update_game()
                self.clock.tick(15)
        else:
            self.clock.tick(6)
            self.adventurer.rest()
            self.update_game()

    def update_game(self):
        self.adventurer.update()

        self.maps.draw(self.window)
        self.adventurer.draw(self.window)
        pygame.display.update()

    def game(self):
        running = True
        self.adventurer.set_level(self.maps.sprites()[0])
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
            self.player_action()


class Button(object):

    font = None
    text = None
    text_rect = None
    hovered_text = None

    def __init__(self, window, img, pos):
        self.window = window
        self.img = img
        self.pos = pos
        self.img_rect = pygame.Rect(pos, self.img.get_size())

    def in_text(self, font, font_size, text, color, hovered_color=None):
        self.font = Assets.create_font(font, font_size)
        self.text = self.font.render(text, False, color)
        self.text_rect = self.text.get_rect(center=self.img_rect.center)
        self.hovered_text = None if hovered_color is None else self.font.render(text, False, hovered_color)

    def blit(self):
        self.window.blit(self.img, self.img_rect)
        if self.img_rect.collidepoint(pygame.mouse.get_pos()):
            self.window.blit(self.hovered_text, self.text_rect)
        else:
            self.window.blit(self.text, self.text_rect)
