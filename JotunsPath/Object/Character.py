from Content import Assets
from Object import Animation, GRAVITY
import pygame


class Character(pygame.sprite.GroupSingle):

    def __init__(self, level):

        pygame.sprite.GroupSingle.__init__(self)
        self.x, self.y = 50, 400
        self.animations = {"REST": Animation(Assets.char_idle()),
                           "RUN": Animation(Assets.char_run()),
                           "ATTACK": Animation(Assets.char_attack()),
                           "AIRATTACK": Animation(Assets.char_airattack()),
                           "JUMP": Animation(Assets.char_jump()),
                           "CROUCH": Animation(Assets.char_crouch())}
        # map which the character is
        self.level = level

        # horizontal direction
        self.left = False

        self.speed = [20, 0]
        self.inair = False
        self.attacking = False
        self.crouched = False

        # character image (changes continuously)
        self.sprite = pygame.sprite.Sprite()


    def set_level(self, level):
        # change the level
        self.level = level

    def move(self, direction, slow=False):
        if direction == "RIGHT":
            self.x = self.x + self.speed[0] * 0.19 if slow else self.x + self.speed[0]
            self.left = False
        elif direction == "LEFT":
            self.x = self.x - self.speed[0] * 0.19 if slow else self.x - self.speed[0]
            self.left = True

        for object in pygame.sprite.groupcollide(self, self.level.walls, False, False).items():
            for wall in object[1]:
                if self.y + self.sprite.rect.h > wall.rect.y:
                    if self.left and self.x - self.speed[0] <= wall.rect.x:
                        self.x = wall.rect.x
                    elif not self.left and self.x + self.sprite.rect.w + self.speed[0] >= wall.rect.x:
                        self.x = wall.rect.x - self.sprite.rect.w
        if self.x < 0:
            self.x = 0
        if self.x + self.sprite.rect.w > self.level.x:
            self.x = self.level.x - self.sprite.rect.w

    def run(self, direction, slow=False):
        self.move(direction)
        animation = self.animations["RUN"].animate()
        self.update_image(animation)

    def attack(self):
        animation = self.animations["ATTACK"].animate()
        self.attacking = True
        self.update_image(animation)

    def airattack(self):
        for _ in range(5):
            self.freefall()
        animation = self.animations["AIRATTACK"].animate()
        self.attacking = True
        self.update_image(animation)

    def jump(self):
        self.speed[1] = 10.5
        self.inair = True

    def rest(self):
        animation = self.animations["REST"].animate()
        self.update_image(animation)

    def freefall(self):
        if self.inair:
            self.speed[1] += GRAVITY
            self.y -= self.speed[1]

            animation = self.animations["JUMP"].animate()
            self.update_image(animation)

    def crouch(self):
        animation = self.animations["CROUCH"].animate()
        self.y += 15
        self.crouched = True
        self.update_image(animation)

    def update_image(self, animation):
        if self.left:
            animation["img"] = pygame.transform.flip(animation["img"], True, False)

        self.sprite.image = animation["img"].subsurface(animation["crop"])
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.x, self.sprite.rect.y = self.x, self.y

    def update(self):
        collided = pygame.sprite.groupcollide(self, self.level.grounds, False, False)
        if not collided:
            self.inair = True
        else:
            for object in pygame.sprite.groupcollide(self, self.level.grounds, False, False).items():
                for ground in object[1]:
                    if self.crouched:
                        self.y -= 15
                    if self.inair and self.sprite.rect.bottom - self.speed[1] > ground.rect.y:
                        self.inair = False
                        self.speed[1] = 0
                        self.y = self.sprite.rect.top
        self.attacking = False
        self.crouched = False
        self.add(self.sprite)