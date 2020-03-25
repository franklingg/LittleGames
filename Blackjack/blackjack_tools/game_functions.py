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
def reshuffle_cards(dealer_hand, player_hand):
    for hand in [dealer_hand, player_hand]:
        hand.retrieve()


# show all current cards
def show_cards(dealer_hand, dealer, player_hand, player, hidden_card=True):
    print(f"{dealer}'s hand: ", end='')
    for i in range(len(dealer_hand.set)):
        if hidden_card and i == 1:
            print(f"|?| ", end='')
            continue
        print(f"|{dealer_hand.set[i]}| ", end='')
    print(f"\n{player}'s hand: ", end='')
    for i in range(len(player_hand.set)): print(f"|{player_hand.set[i]}| ", end='')


# show options
def choosing(turn):
    if turn == 1:
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


# check who won (if no one busted)
def win_check(dealer_hand, player_hand, dealer, player, balance, bet, multiply=1):
    dealer_score = calculate_points(dealer_hand)
    player_score = calculate_points(player_hand)
    if dealer_score > player_score:
        print(f"####### {dealer} venceu. Aposta perdida!  #########")
        return balance
    elif dealer_score == player_score:
        balance += multiply * bet / 2
        print(f"####### Empate! R$ {multiply * bet / 2} recuperado ########")
        return balance
    else:
        balance += 2 * bet * multiply
        print(f"####### {player} venceu! Ganhou R$ {2 * bet * multiply}!  #########")
        return balance


# check if you've busted
def bust_check(hand, name):
    if calculate_points(hand) > 21:
        print(f"####### {name} estourou! #######")
        return True
    else:
        return False


# automatic dealer
def dealer_play(dealer_hand, dealer, balance, bet, multiply=1):
    score = calculate_points(dealer_hand)
    dealer_bust = False
    if score <= 15:
        dealer_hand.hit()
        dealer_bust = bust_check(dealer_hand, dealer)
        if dealer_bust:
            balance += bet * 2 * multiply
    return dealer_hand, balance, dealer_bust


# Where the game happens
def round_menu(turn, dealer_hand, player_hand, bet, balance, dealer, player):
    dealer_bust = False
    choice = choosing(turn)
    if choice == 1:
        player_hand.hit()
        player_bust = bust_check(player_hand, player)
        if not player_bust:
            dealer_hand, balance, dealer_bust = dealer_play(dealer_hand, dealer, balance, bet)
        return (player_bust or dealer_bust), dealer_hand, player_hand, balance

    elif choice == 2:
        dealer_hand, balance, dealer_bust = dealer_play(dealer_hand, dealer, balance, bet)
        if bust_check(dealer_hand, dealer):
            return True, dealer_hand, player_hand, balance
        balance = win_check(dealer_hand, player_hand, dealer, player, balance, bet)
        return True, dealer_hand, player_hand, balance

    elif choice == 3:
        balance += bet / 2
        print(f"\n######## Desistiu! Recuperou R$ {bet / 2}!  ##########")
        return True, dealer_hand, player_hand, balance

    else:
        if balance < bet:
            print(f"\n####### Saldo insuficiente para dobrar! R$ {balance} restante. ########")
            return False, dealer_hand, player_hand, balance
        balance -= bet
        player_hand.hit()
        if bust_check(player_hand, player):
            return True, dealer_hand, player_hand, balance

        dealer_hand, balance, dealer_bust = dealer_play(dealer_hand, dealer, balance, bet, 2)
        if dealer_bust:
            return True, dealer_hand, player_hand, balance

        balance = win_check(dealer_hand, player_hand, dealer, player, balance, bet, 2)
        return True, dealer_hand, player_hand, balance
