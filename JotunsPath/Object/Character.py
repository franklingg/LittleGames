from Content import Assets
from Object import Animation
import pygame


class Character(pygame.sprite.GroupSingle):

    def __init__(self, pos, level):

        pygame.sprite.GroupSingle.__init__(self)
        self.x, self.y = pos[0], pos[1]
        self.animations = {"REST": Animation(Assets.char_idle()),
                           "RUN": Animation(Assets.char_run()),
                           "ATTACK": Animation(Assets.char_attack()),
                           "JUMP": Animation(Assets.char_jump())}
        # map which the character is
        self.level = level

        # horizontal direction
        self.left = False
        self.speed = [20, 15]
        self.gravity = -0.6

        # character image (changes continuously)
        self.sprite = pygame.sprite.Sprite()
        self.rest()
        self.update()

    def set_level(self, level):
        # change the level
        self.level = level

    def run(self, direction):
        collided = pygame.sprite.groupcollide(self, self.level.objects, False, False)
        if collided is not None:
            for key in collided.keys():
                for sprite in collided[key]:
                    print(self.x)
                    if self.x == sprite.rect.x:
                        self.speed[0] = 0
                    if self.y == sprite.rect.y:
                        self.speed[1] = 0
        else:
            self.speed = [20, 15]

        if direction == "RIGHT":
            self.x += self.speed[0]
            animation = self.animations["RUN"].animate()
            self.left = False
            self.update_image(animation)
        elif direction == "LEFT":
            self.x -= self.speed[0]
            animation = self.animations["RUN"].animate()
            self.left = True
            self.update_image(animation)

    def attack(self):
        animation = self.animations["ATTACK"].animate()
        self.update_image(animation)

    def jump(self, direction = "None"):
        if direction is not None:
            self.run(direction)
        animation = self.animations["JUMP"].animate()
        self.speed[1] += self.gravity
        self.y -= self.speed[1]
        self.update_image(animation)
        if self.y > 440:
            self.y = 440
            self.speed[1] = 13
            return False
        return True

    def rest(self):
        animation = self.animations["REST"].animate()
        self.update_image(animation)

    def update_image(self, animation):
        if self.left:
            animation["img"] = pygame.transform.flip(animation["img"], True, False)

        self.sprite.image = animation["img"].subsurface(animation["crop"])
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.x, self.sprite.rect.y = self.x, self.y

    def update(self):
        self.add(self.sprite)