import pygame
from .Settings import Screen, Controls
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

        self.controls = Controls()
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
        if pygame.key.get_pressed()[self.controls.jump] and not self.adventurer.inair:
            self.adventurer.jump()

        if (pygame.key.get_pressed()[self.controls.crouch_arrow] or pygame.key.get_pressed()[self.controls.crouch_letter]) \
                and not self.adventurer.inair:
            self.adventurer.crouch()
            self.clock.tick(10)

        if pygame.key.get_pressed()[self.controls.attack]:
            if self.adventurer.inair:
                for i in range(3):
                    self.adventurer.airattack()
                    self.update_game()
                    self.clock.tick(10)
            else:
                for i in range(6):
                    self.adventurer.attack()
                    self.clock.tick(16)
                    self.update_game()
            self.adventurer.attacking = True
        if pygame.key.get_pressed()[self.controls.run_right_arrow] or pygame.key.get_pressed()[self.controls.run_right_letter]:
            if self.adventurer.attacking:
                self.adventurer.move("RIGHT")
            elif self.adventurer.inair:
                self.adventurer.move("RIGHT", slow=True)
            elif not self.adventurer.crouched:
                self.adventurer.run("RIGHT")
                self.clock.tick(15)
        if pygame.key.get_pressed()[self.controls.run_left_arrow] or pygame.key.get_pressed()[self.controls.run_left_letter]:
            if self.adventurer.attacking:
                self.adventurer.move("LEFT")
            elif self.adventurer.inair:
                self.adventurer.move("LEFT", slow=True)
            elif not self.adventurer.crouched:
                self.adventurer.run("LEFT")
                self.clock.tick(15)
        if self.adventurer.inair:
            self.adventurer.freefall()
        elif self.controls.nothing_pressed():
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
