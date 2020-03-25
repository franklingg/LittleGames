# Jogo de Blackjack entre 1 jogador e um dealer automático

import blackjack_tools.game_functions as tools


# initial variables
dealer = 'Dealer'
player = 'Jogador'
bet_min = 20
balance = 200

# starting the game
print("\nBem-vindo ao Super Cassino de Chernobyl! Hoje temos um ótimo Blackjack para você.")

while True:
    start = tools.corrected_input("\n######  START MENU  #######\n"
                                  "(1) Começar a jogar\n"
                                  "(2) Tutorial de Blackjack\n"
                                  "(3) Configurações\n"
                                  "Sua escolha: ", 1, 3)
    if start == 1:
        break
    elif start == 2:
        print(
            "\n##########################################  TUTORIAL  ######################################################\n"
            "Blackjack é o jogo mais famoso do mundo em cassinos. O objetivo é pontuar, com cartas, o mais próximo de 21, \n"
            "sem estourar. Cada jogador recebe inicialmente 2 cartas (onde K,Q,J valem 10 pontos; o Ás vale 1 ou 11), o \n"
            "Dealer tem uma carta à mostra e uma escondida. Em cada jogada, o jogador pode: a) manter suas cartas (se \n"
            "acreditar que pode estourar; b) pedir mais uma carta ao dealer; c) render-se (e recuperar 50% da sua aposta;\n"
            "d) dobrar a aposta (só é válido para o primeiro movimento e o jogador somente pode receber mais uma carta;\n")
    else:
        configuration = tools.corrected_input("\n##############  SETTINGS  ##############\n"
                                              "(1) Editar saldo inicial e aposta mínima\n"
                                              "(2) Editar nomes\n"
                                              "Sua escolha: ", 1, 2)
        if configuration == 1:
            balance = tools.corrected_input("Novo saldo: R$ ", 0, float('inf'))
            bet_min = tools.corrected_input("Nova aposta mínima: R$ ", 0, balance)
        elif configuration == 2:
            dealer = input("Novo nome para o dealer: ")
            player = input("Novo nome para o jogador: ")

# starting rounds
round = 1
while True:
    if balance < bet_min:
        print("\nSaldo insuficiente (PS.: você perdeu toda a grana!)")
        break
    bet = tools.corrected_input(f"\nRodada {round}. Qual o valor da sua aposta (Aposta mínima: {bet_min})? R$ ", bet_min, balance, 'Aposta ou saldo insuficiente(s)')
    balance -= bet
    player_hand = tools.create_hand()
    dealer_hand = tools.create_hand()
    turn = 0
    while True:
        turn += 1
        tools.show_cards(dealer_hand, dealer, player_hand, player)
        end_check, dealer_hand, player_hand, balance = tools.round_menu(turn, dealer_hand, player_hand, bet, balance, dealer, player)
        if end_check:
            tools.show_cards(dealer_hand, dealer, player_hand, player, False)
            break

    tools.reshuffle_cards(dealer_hand, player_hand)

    round += 1
    left_game = tools.corrected_input(f"\n\nBoa partida!\n"
                                      f"(1) Deseja jogar a rodada {round} ou\n"
                                      f"(2) Deixar o jogo?\n"
                                      f"Sua escolha: ", 1, 2)
    if left_game == 2:
        break
print(f"Seu saldo final foi de R$ {balance}")
