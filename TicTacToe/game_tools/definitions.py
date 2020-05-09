import pygame
import os

# constants
menu_font = None
game_font = None
xo_sc = 0.32  # x and o's scale for score table
volume = 0.035

# Get the requested color
def color(color_name):
    colors = {
        'black': (0, 0, 0),
        'light-black': (56, 56, 56),
        'white': (255, 255, 255),
        'almost-white': (224, 236, 226),
        'red': (200, 0, 0),
        'bright-red': (255, 0, 0),
        'blue': (0, 0, 200),
        'bright-blue': (0, 0, 255),
        'purple': (184, 68, 187),
        'soft-purple': (197, 106, 200),
        'green': (0, 200, 0),
        'bright-green': (0, 255, 0)
    }
    return colors[color_name]


def playlist():
    cur_path = os.getcwd()
    available = {'menu-song': (cur_path + '\\sounds\\menu_song.wav'),
                 'game-song': (cur_path + '\\sounds\\game_song.wav'),
                 'marking': (cur_path + '\\sounds\\marking.wav'),
                 'button-click': (cur_path + '\\sounds\\button_click.wav'),
                 'wrong': (cur_path + '\\sounds\\wrong.wav'),
                 'start-game': (cur_path + '\\sounds\\start_game.wav'),
                 'victory': (cur_path + '\\sounds\\victory.wav'),
                 'draw': (cur_path + '\\sounds\\draw.wav')
                 }
    return available


# Return a formatted text ready to be "blitted" and its position rectangle
def text(content, font_name, size, color_name):
    font = pygame.font.Font(font_name, size)
    return_text = font.render(content, True, color(color_name))
    return return_text
