
from blackjack_tools import deck_setup


# Error handling
def corrected_input(input_text, floor, ceil, message=''):
    while True:
        try:
            value = int(input(input_text))
            if value < floor or value > ceil:
                raise Exception
            break
        except:
            print(f"Valor inválido. Tente novamente. {message}\n")
            continue
    return value


# create a hand of cards
def create_hand():
    value = deck_setup.Cards()
    for i in range(2): value.hit()
    return value


# put the cards back in the deck
def reshuffle_cards(hand1, hand2, hand3):
    if hand3 == '':
        for hand in [hand1, hand2]:
            hand.retrieve()
    else:
        for hand in [hand1, hand2, hand3]:
            hand.retrieve()


# show all current cards
def show_cards(hand1, name1, hand2, name2, hand3, hidden_card=1):
    print(f"{name1}'s hand: ", end='')
    for i in range(len(hand1.set)):
        if i == hidden_card:
            print(f"|?| ", end='')
            continue
        print(f"|{hand1.set[i]}| ", end='')
    print(f"\n{name2}'s hand: ", end='')
    for i in range(len(hand2.set)): print(f"|{hand2.set[i]}| ", end='')
    if hand3 != '':
        print(f"\n{name2}'s 2nd hand: ", end='')
        for i in range(len(hand2.set)): print(f"|{hand2.set[i]}| ", end='')


# show options
def choosing(play, hand):
    if play == 1 and (hand.set[0] == hand.set[1]):
        choice = corrected_input("\nQual sua próxima ação?\n"
                                 "(1) Hit (Pegar uma carta)\n"
                                 "(2) Stand (Manter as cartas)\n"
                                 "(3) Surrender (Desistir e recuperar 50% da aposta)\n"
                                 "(4) Double (Dobrar a aposta e pegar SOMENTE mais uma carta)\n"
                                 "(5) Split (Dividir em duas apostas independentes)\n"
                                 "Sua escolha: ", 1, 5)
    elif play == 1:
        choice = corrected_input("\nQual sua próxima ação?\n"
                                 "(1) Hit (Pegar uma carta)\n"
                                 "(2) Stand (Manter as cartas)\n"
                                 "(3) Surrender (Desistir e recuperar 50% da aposta)\n"
                                 "(4) Double (Dobrar a aposta e pegar SOMENTE mais uma carta)\n"
                                 "Sua escolha: ", 1, 4)
    else:
        choice = corrected_input("\nQual sua próxima ação?\n"
                                 "(1) Hit (Pegar uma carta)\n"
                                 "(2) Stand (Manter as cartas)\n"
                                 "(3) Surrender (Desistir e recuperar 50% da aposta)\n"
                                 "Sua escolha: ", 1, 3)
    return choice


# calculate your points
def calculate_points(hand):
    points = 0
    isThereA = False
    for card in hand.set:
        if card == 'J' or card == 'Q' or card == 'K':
            points += 10
        elif card == 'A':
            points += 1
            isThereA = True
        else:
            points += int(card)
    if points <= 11 and isThereA:
        points += 10
    return points


# check if you've busted
def bust_check(score):
    if score > 21:
        return True
    else:
        return False


# automatic dealer
def dealer_hit(hand):
    score = calculate_points(hand)
    if score <= 15:
        return True
    else:
        return False


# Where the game happens
def round_menu(play, hand1, hand2, withdraw, cash, name1, name2):
    choice = choosing(play, hand2)
    if choice == 1:
        hand2.hit()
        player_score = calculate_points(hand2)
        if bust_check(player_score):
            print("\n##########  Estourou! Aposta perdida  ############")
        else:
            if dealer_hit(hand1):
                hand1.hit()
                dealer_score = calculate_points(hand1)
                if bust_check(dealer_score):
                    print(f"\n####### {name1} Estourou! Você ganhou!!  #########")
                    cash += withdraw * 2
                    return True, False, hand1, hand2, cash
        return bust_check(player_score), False, hand1, hand2, cash
    elif choice == 2:
        dealer_score = calculate_points(hand1)
        if dealer_hit(hand1):
            hand1.hit()
            dealer_score = calculate_points(hand1)
            if bust_check(dealer_score):
                print(f"\n####### {name1} Estourou! Você ganhou!!  #########")
                cash += withdraw * 2
                return True, False, hand1, hand2, cash
            return False, False, hand1, hand2, cash
        player_score = calculate_points(hand2)
        if dealer_score > player_score:
            print(f"####### {name1} venceu. Aposta perdida!  #########")
        elif dealer_score == player_score:
            cash += withdraw / 2
            print(f"####### Empate! R$ {withdraw / 2} recuperado ########")
        else:
            cash += 2 * withdraw
            print(f"####### {name2} venceu! Ganhou R$ {2 * withdraw}!  #########")
        return True, False, hand1, hand2, cash

    elif choice == 3:
        cash += withdraw / 2
        print(f"\n######## Desistiu! Recuperou R$ {withdraw / 2}!  ##########")
        return True, False, hand1, hand2, cash
    elif choice == 4:
        cash -= withdraw
        hand2.hit()
        player_score = calculate_points(hand2)
        if bust_check(player_score):
            print("\n##########  Estourou! Aposta perdida  ############")
            return True, False, hand1, hand2, cash
        dealer_score = calculate_points(hand1)
        if dealer_hit(hand1):
            hand1.hit()
            dealer_score = calculate_points(hand1)
            if bust_check(dealer_score):
                print(f"\n####### {name1} Estourou! Você ganhou!!  #########")
                cash += withdraw * 2
                return True, False, hand1, hand2, cash
        if dealer_score > player_score:
            print(f"####### {name1} venceu. Aposta perdida!  #########")
        elif dealer_score == player_score:
            cash += withdraw / 2
            print(f"####### Empate! R$ {withdraw} recuperado ########")
        else:
            cash += 4 * withdraw
            print(f"####### {name2} venceu! Ganhou R$ {4 * withdraw}!  #########")
        return True, False, hand1, hand2, cash
    else:
        return False, True, hand1, hand2, cash


