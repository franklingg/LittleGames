import pygame
import game_tools.definitions as info
import os


# "Blits" the text argument
def bliter(screen, content, font_name, font_size, color, center_pos):
    text = info.text(content, font_name, font_size, color)
    textRect = text.get_rect()
    textRect.center = center_pos
    screen.blit(text, textRect)


# Creates an interactive button
class Button:
    def __init__(self, ic, ac, rect, content):
        self.ic = info.color(ic)
        self.ac = info.color(ac)
        self.rect = pygame.Rect(rect)
        self.content = content

        mouse = pygame.mouse.get_pos()
        self.cursorWithin = pygame.Rect.collidepoint(self.rect, mouse)

    def show(self, screen):
        if self.cursorWithin:
            pygame.draw.rect(screen, self.ac, self.rect)
        else:
            pygame.draw.rect(screen, self.ic, self.rect)
        bliter(screen, self.content, None, int(self.rect[3] * 0.4), 'white', self.rect.center)

    @property
    def isClicked(self):
        click = pygame.mouse.get_pressed()
        if self.cursorWithin and click[0] == 1:
            return True
        return False


def display_gameboard(screen, x_score, o_score, round, mark, board, win):
    cur_path = os.getcwd()
    # display the background image with the board
    table = pygame.image.load(cur_path + '\\pictures\\gameboard.jpg')
    screen.blit(table, (0, 0))

    if draw_check(board):
        #  Display the title (if it is a draw)
        bliter(screen, 'Draw!', info.game_font, 60, 'almost-white', (400, 50))
    elif win:
        # Display the title (who has won)
        bliter(screen, str(mark) + ' won!', info.game_font, 60, 'almost-white', (400, 50))
    else:
        # Display the title (who's turn is)
        bliter(screen, str(mark) + ' turn', info.game_font, 60, 'almost-white', (400, 50))

    # display the round number
    bliter(screen, 'ROUND  ' + str(round), info.game_font, 50, 'almost-white', (100, 50))

    # display the x's and o's score
    bliter(screen, 'SCORE', info.game_font, 50, 'almost-white', (78, 230))
    x_img = pygame.image.load(cur_path + '\\pictures\\x.png')
    x_img_red = pygame.transform.scale(x_img,
                                       (int(x_img.get_width() * info.xo_sc), int(x_img.get_height() * info.xo_sc)))
    o_img = pygame.image.load(cur_path + '\\pictures\\o.png')
    o_img_red = pygame.transform.scale(o_img,
                                       (int(o_img.get_width() * info.xo_sc), int(o_img.get_height() * info.xo_sc)))
    screen.blit(x_img_red, (6, 275))  # blit the reduced images
    screen.blit(o_img_red, (6, 362))

    x_colon = ": " if x_score // 100 == 0 else ":"
    o_colon = ": " if o_score // 100 == 0 else ":"
    bliter(screen, x_colon + str(x_score), info.game_font, 90, 'almost-white', (107, 295))
    bliter(screen, o_colon + str(o_score), info.game_font, 90, 'almost-white', (107, 382))

    # display each mark
    for i in range(3):
        for j in range(3):
            if board[i][j] != ' ':
                mark_toBlit = x_img if board[i][j] == 'X' else o_img
                screen.blit(mark_toBlit, (182 + 156 * j, 115 + 155 * i))


def mark(marker, board, clicked, win, mute):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # Board rect: (169, 103, 469, 469) each (100, 122)
    to_mark = (False, 0, 0)
    if click[0] == 1:
        for i in range(3):
            for j in range(3):
                square_rect = pygame.Rect(169 + 157 * j, 103 + 157 * i, 155, 157)
                if pygame.Rect.collidepoint(square_rect, mouse):
                    to_mark = (True, i, j)
                    break
            if to_mark[0]:
                break

    # mark in the gameboard if it is to be marked and avoid remarking if a mark already is placed
    if to_mark[0] and clicked:
        if board[to_mark[1]][to_mark[2]] == ' ' and not win:
            board[to_mark[1]][to_mark[2]] = marker
            play_sound('marking', 0, mute)
            marker = 'X' if marker == 'O' else 'O'
            clicked = False
            return marker, board, clicked

        play_sound('wrong', 0, mute)
        clicked = False

    return marker, board, clicked


def win_check(board):
    win_bool = any(((board[0][0] == mark and board[0][1] == mark and board[0][2] == mark) or  # victory through top
                    (board[1][0] == mark and board[1][1] == mark and board[1][2] == mark) or  # middle - horizontally
                    (board[2][0] == mark and board[2][1] == mark and board[2][2] == mark) or  # bottom
                    (board[0][0] == mark and board[1][0] == mark and board[2][0] == mark) or  # left
                    (board[0][1] == mark and board[1][1] == mark and board[2][1] == mark) or  # middle - vertically
                    (board[0][2] == mark and board[1][2] == mark and board[2][2] == mark) or  # right
                    (board[0][0] == mark and board[1][1] == mark and board[2][2] == mark) or  # main diagonal
                    (board[0][2] == mark and board[1][1] == mark and board[2][0] == mark))     # secondary diagonal
                    for mark in ['X', 'O'])
    return win_bool


def draw_check(board):
    allFilled = all(all(board[i][j] != ' ' for j in range(3)) for i in range(3))
    won = win_check(board)
    return allFilled and not won


def play_sound(request, loop=0, mute=False):
    playlist = info.playlist()
    if not mute:
        sound = pygame.mixer.Sound(playlist[request])
        sound.set_volume(info.volume)
        sound.play(loop)
