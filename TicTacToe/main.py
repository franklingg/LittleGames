import pygame
import game_tools.definitions as info
import game_tools.functions as creator
from random import choice


def start_menu():
    keepIntro = True
    # Intro song
    pygame.mixer.music.load(info.playlist()['menu-song'])
    pygame.mixer.music.set_volume(info.volume)
    pygame.mixer.music.play(-1)

    while keepIntro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepIntro = False
                keepPlaying = False

        background = pygame.image.load('pictures\\startscreen.png')
        gameDisplay.blit(background, (0,0))

        Start_But = creator.Button('green', 'bright-green', (313, 350, 150, 60), 'START GAME')
        Start_But.show(gameDisplay)
        Quit_But = creator.Button('red', 'bright-red', (313,450,150,60), 'QUIT GAME')
        Quit_But.show(gameDisplay)

        if Start_But.isClicked:
            pygame.mixer.music.stop()
            creator.play_sound('start-game')
            keepIntro = False
            keepPlaying = True
        elif Quit_But.isClicked:
            keepIntro = False
            keepPlaying = False

        pygame.display.update()
        clock.tick(20)

    return keepIntro, keepPlaying


def game_loop():
    introRun = True
    gameRun = True
    first_move = True
    already_clicked = False
    win = False
    mute = False
    round = 1
    x_score = o_score = 0
    turn = ''
    markingboard = [[' ' for n in range(3)] for m in range(3)]
    while gameRun:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameRun = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if creator.Button.isClicked:
                    already_clicked = True

        if introRun:
            introRun, gameRun = start_menu()
            if not introRun and not mute:
                pygame.mixer.music.load(info.playlist()['game-song'])
                pygame.mixer.music.play(-1)
        else:
            if first_move and not win:
                turn = choice(['X', 'O'])  # randomly choose who starts
                first_move = False
                already_clicked = False

            if creator.draw_check(markingboard) and not first_move:
                creator.play_sound('draw', 0, mute)
                first_move = True
            elif win and not first_move:
                creator.play_sound('victory', 0, mute)
                turn = 'X' if turn == 'O' else 'O'   # next mark turn
                if turn == 'X':
                    x_score += 1
                else:
                    o_score += 1
                first_move = True

            turn, markingboard, already_clicked = creator.mark(turn, markingboard, already_clicked, win, mute)
            win = creator.win_check(markingboard) or creator.draw_check(markingboard)

            creator.display_gameboard(gameDisplay, x_score, o_score, round, turn, markingboard, win)

            # Restart rounds
            Restart_But = creator.Button('black', 'light-black', (647, 240, 150, 60), '          NEW ROUND')
            Restart_But.show(gameDisplay)
            restart_icon = pygame.image.load('pictures\\restart.png')
            gameDisplay.blit(restart_icon, (645,249))

            if Restart_But.isClicked and already_clicked:
                creator.play_sound('button-click', 0, mute)
                round += 1
                first_move = True
                already_clicked = False
                win = False
                markingboard = [[' ' for n in range(3)] for m in range(3)]
                pygame.display.update()
                continue

            # Return to main menu
            Home_But = creator.Button('black', 'light-black', (647, 321, 150, 60), '           MAIN MENU')
            Home_But.show(gameDisplay)
            home_icon = pygame.image.load('pictures\\home.png')
            gameDisplay.blit(home_icon, (648, 330))

            if Home_But.isClicked and already_clicked:
                pygame.mixer.music.stop()
                introRun = True
                round = 1
                x_score = 0
                o_score = 0
                already_clicked = False
                win = False
                markingboard = [[' ' for n in range(3)] for m in range(3)]


            # Mute button
            if not mute:
                Mute_But = creator.Button('black', 'light-black', (647, 500, 150, 60), '       MUTE')
                mute_icon = pygame.image.load('pictures\\unmuted.png')
            else:
                Mute_But = creator.Button('black', 'light-black', (647, 500, 150, 60), '         UNMUTE')
                mute_icon = pygame.image.load('pictures\\muted.png')
            Mute_But.show(gameDisplay)
            gameDisplay.blit(mute_icon, (648, 508))

            if Mute_But.isClicked and already_clicked:
                creator.play_sound('button-click', 0)
                mute = True if not mute else False
                if mute:
                    pygame.mixer.music.stop()
                else:
                    pygame.mixer.music.load(info.playlist()['game-song'])
                    pygame.mixer.music.play(-1)
                already_clicked = False

            pygame.display.update()
            clock.tick(60)


pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('TIC TAC TOE')
pygame.display.set_icon(pygame.image.load('pictures\icon.png'))

clock = pygame.time.Clock()

game_loop()
pygame.quit()