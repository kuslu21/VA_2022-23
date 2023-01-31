import random

error = False

# nickname = input("Zadejte přezdívku -> ")
# if len(nickname) < 3:
#     print("Přezdívka je moc krátká.")
#     error = True
# if len(nickname) > 10 and error != True:
#     print("Přezdívka je moc dlouhá.")
#     error = True
#
# if nickname.isalnum() and error != True:
#     pass
# else:
#     print("Přezdívka obsahuje nepovolené znaky.")
#     error = True
# if error != True:

def new_game():
    tokens = 20
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    random.shuffle(deck)

    player_deck = []
    dealer_deck = []

    for i in range(2):
        player_deck.append(deck.pop())
        dealer_deck.append(deck.pop())

    def total_score_calculating(player_deck):
        total = 0
        for card in player_deck:
            if card in ['J', 'Q', 'K']:
                total += 10
            elif card == 'A':
                if total + 11 > 21:
                    total += 1
                else:
                    total += 11
            else:
                total += card
        return total

    def total_score_calculating(dealer_deck):
        total = 0
        for card in dealer_deck:
            if card in ['J', 'Q', 'K']:
                total += 10
            elif card == 'A':
                if total + 11 > 21:
                    total += 1
                else:
                    total += 11
            else:
                total += card
        return total
    total_score_calculating(player_deck)
    total_score_calculating(dealer_deck)
    print("|-------------------------------")
    print(f"| -> Vaše tokeny: {tokens}          ")
    # print("|-------------------------------")
    print(f"| -> Vaše karty: {player_deck}       ")
    print(f"| -> Hodnota vašich karet: {total_score_calculating(player_deck)}")
    # print("|-------------------------------")
    print(f"| -> Karty dealera: {dealer_deck}")
    print(f"| -> Hodnota karet dealera: {total_score_calculating(dealer_deck)}")
    print("|-------------------------------")

    print("| -> Možnosti:")
    print("|    -> Další karta -> 1")
    print("|    -> Složit -> 2")
    print("|    -> Double down -> 3")
    game_choice = input("|    -> Váš výběr (1, 2..) -> ")

    if game_choice == '1':
        player_deck.append(deck.pop())
        if total_score_calculating(player_deck) > 21:
            print("|-------------------------------")
            print("| -> Posral jsi to :/")
            print(f"| -> Vaše karty -> {player_deck}")
            print(f"| -> Vaše karty -> {dealer_deck}")
            tokens -= 1
        elif game_choice == '2':
            while total_score_calculating(dealer_deck):
                dealer_deck.append(deck.pop())
            if total_score_calculating(dealer_deck) > 21:
                print("Deler to podělal, vyhráváš!")
                print(f"| -> Vaše karty -> {player_deck}")
                print(f"| -> Vaše karty -> {dealer_deck}")
                tokens += 1



new_game()
