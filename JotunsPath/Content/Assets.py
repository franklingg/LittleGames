import pygame.font
import pygame.image
from Content import Path

class Color(object):
    black = (0,0,0)
    light_black = (50, 51, 51)
    light_grey = (153, 150, 165)
    pearl = (208,240,192)
    sky_blue = (93, 142, 193)
    dark_blue = (24,48,100)
    light_green = (140, 204, 76)
    jade = (0, 168, 107)
    forest_green = (40, 78, 56)
    brown = (75,83,32)
    beige = (138,154,91)
    test = (198, 139, 78)


def icon():
    return pygame.image.load(Path.icon)

def create_font(font, size):
    if font == "karma":
        return pygame.font.Font(Path.font_karma, size)
    elif font == "fonBold":
        return pygame.font.Font(Path.font_fonBold, size)
    elif font == "papercut":
        return pygame.font.Font(Path.font_papercut, size)

def home_background():
    return pygame.image.load(Path.homeBackground)

def home_button():
    return pygame.image.load(Path.homeButton)