import random
import csv
error = False
tokens = 20

nickname = input("Zadejte přezdívku -> ")
if len(nickname) < 3:
    print("Přezdívka je moc krátká.")
    error = True
if len(nickname) > 10 and error != True:
    print("Přezdívka je moc dlouhá.")
    error = True

if nickname.isalnum() and error != True:
    pass
else:
    print("Přezdívka obsahuje nepovolené znaky.")
    error = True
if error != True:

    def new_game():
        tokens = 20
        print('-------- BLACKJACK --------')
        print(f"| -> Vaše tokeny: {tokens}")
        game_tokens = input('| -> Kolik chcete vsadit? -> ')
        if game_tokens.isnumeric():
            game_tokens = int(game_tokens)
            if game_tokens <= tokens :
                print(f"| -> Hotovo, vsadili jste {game_tokens} tokenů.")
            else:
                print(f"| -> Nemáte dostatek tokenů, maximální můžete vsadit {tokens} tokenů.")
                print('************** -- RESTART -- **************')
                new_game()
        else:
            print('| -> Zadejte prosím validní data (číslo)')
            print('************** -- RESTART -- **************')
            new_game()

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

        def game_continues():
            print("|---------------------------------------")
            print("| -> Hra pokračuje")
            print(f"| -> Vaše karty -> {player_deck}")
            print(f"| -> Hodnota vašich karet -> {total_score_calculating(player_deck)}")
            print("|---------------------------------------")
            print("| -> Možnosti:")
            print("|    -> Další karta -> '1'")
            print("|    -> Složit -> '2'")
            print("|    -> Double down -> '3'")
            game_choice = input("|    -> Váš výběr (1, 2, 3) -> ")
            return game_choice

        # Menu
        print("|---------------------------------------")
        print(f"| -> Vaše karty: {player_deck}       ")
        print(f"| -> Celková hodnota vašich karet: {total_score_calculating(player_deck)}")
        print("|---------------------------------------")
        print("| -> Možnosti:")
        print("|    -> Další karta -> '1'")
        print("|    -> Složit -> '2'")
        print("|    -> Double down -> '3'")
        game_choice = input("|    -> Váš výběr (1/2/3) -> ")

        while game_choice == '1':
            game_choice = 0
            player_deck.append(deck.pop())
            if total_score_calculating(player_deck) > 21:
                tokens -= game_tokens
                print("|---------------------------------------")
                print("| -> Prohrál jsi :(")
                print(f"| -> Zbývá vám {tokens} tokenů")
                print(f"| -> Vaše karty -> {player_deck}")
                print(f"| -> Hodnota vašich karet -> {total_score_calculating(player_deck)}")
                if tokens != 0:
                    print("| -> Možnosti:")
                    print("|    -> Další hra -> '1'")
                    print("|    -> Ukončit hru -> '2'")
                    end_choice = input("|    -> Váš výběr (1/2) -> ")
                else:
                    print("|---------------------------------------")
                    print('| -> Došly vám žetony')
                    print("| -> Možnosti:")
                    print("|    -> Dopnit žetony -> '1'")
                    print("|    -> Ukončit hru -> '2'")
                    end_choice = input("|    -> Váš výběr (1/2) -> ")
                    if end_choice.isnumeric():
                        end_choice = int(end_choice)
                        if end_choice == 1 and tokens != 0:
                            end_choice = 0
                            game_choice = 0
                            new_game()
                            print('Nová hra')
                        elif end_choice == 2 and tokens != 0:
                            end_choice = 0
                            game_choice = 0
                            print('Konec hry.')
                        else:
                            print('bruh')
                    else:
                        print('Zadejte prosím 1/2')
                        game_choice = 0
            elif total_score_calculating(player_deck) < 21:
                game_continues()

        while game_choice == '2':
            game_choice = 0
            if total_score_calculating(dealer_deck) < total_score_calculating(player_deck):
                print("|---------------------------------------")
                print('| -> Vyhráli jste :)')
                tokens = tokens + game_tokens
                print(f"| -> Vaše karty -> {player_deck}")
                print(f"| -> Hodnota vašich karet -> {total_score_calculating(player_deck)}")
                print(f"| -> Karty dealera -> {dealer_deck}")
                print(f"| -> Hodnota karet dealera -> {total_score_calculating(dealer_deck)}")
                game_choice = 0
                player_header = ['nickname', 'score']
                player_data = [nickname, tokens]
                with open('data.csv', 'a', encoding='UTF8', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(player_header)
                    writer.writerow(player_data)
                file.close()
                print("|---------------------------------------")
                print('| -> Přejete si začít další hru?')
                print("| -> Možnosti:")
                print("|    -> Ano -> '1'")
                print("|    -> Ne -> '2'")
                end_choice = input("|    -> Váš výběr (1/2) -> ")
                if end_choice.isnumeric():
                    end_choice = int(end_choice)
                    if end_choice == 1 and tokens != 0:
                        end_choice = 0
                        game_choice = 0
                        new_game()
                        print('Nová hra')
                    elif end_choice == 2 and tokens != 0:
                        end_choice = 0
                        game_choice = 0
                        print('Konec hry.')
                    else:
                        print('bruh')
                else:
                    print('Zadejte prosím 1/2')
            elif total_score_calculating(dealer_deck) == total_score_calculating(player_deck):
                print('stejne')
                game_choice = 0
            elif total_score_calculating(dealer_deck) > total_score_calculating(player_deck):
                print('prohral jsi')
                game_choice = 0

        while game_choice == '3':
            game_choice = 0
            if game_tokens <= tokens:
                game_tokens = game_tokens + game_tokens
                tokens -= game_tokens
                print(f"| -> Vsazené tokeny -> {game_tokens}")
                if total_score_calculating(dealer_deck) < total_score_calculating(player_deck):
                    print("|---------------------------------------")
                    print('| -> Vyhráli jste :)')
                    tokens = tokens + game_tokens
                    print(f"| -> Vaše karty -> {player_deck}")
                    print(f"| -> Hodnota vašich karet -> {total_score_calculating(player_deck)}")
                    print(f"| -> Karty dealera -> {dealer_deck}")
                    print(f"| -> Hodnota karet dealera -> {total_score_calculating(dealer_deck)}")
                    game_choice = 0
                    player_header = ['nickname', 'score']
                    player_data = [nickname, tokens]
                    with open('data.csv', 'a', encoding='UTF8', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow(player_header)
                        writer.writerow(player_data)
                    file.close()
                    print("|---------------------------------------")
                    print('| -> Přejete si začít další hru?')
                    print("| -> Možnosti:")
                    print("|    -> Ano -> '1'")
                    print("|    -> Ne -> '2'")
                    end_choice = input("|    -> Váš výběr (1/2) -> ")
                    if end_choice.isnumeric():
                        end_choice = int(end_choice)
                        if end_choice == 1 and tokens != 0:
                            end_choice = 0
                            game_choice = 0
                            new_game()
                            print('| -> Nová hra')
                        elif end_choice == 2 and tokens != 0:
                            end_choice = 0
                            game_choice = 0
                            print('| -> Konec hry.')
                        else:
                            print("|---------------------------------------")
                            print('| -> Došly vám žetony')
                            print("| -> Možnosti:")
                            print("|    -> Dopnit žetony -> '1'")
                            print("|    -> Ukončit hru -> '2'")
                            end_choice = input("|    -> Váš výběr (1/2) -> ")
                            if end_choice.isnumeric():
                                end_choice = int(end_choice)
                                if end_choice == 1 and tokens == 0:
                                    end_choice = 0
                                    game_choice = 0
                                    new_game()
                                    print('Nová hra')
                                elif end_choice == 2 and tokens == 0:
                                    end_choice = 0
                                    game_choice = 0
                                    print('Konec hry.')
                                else:
                                    print('Došlo k chybě.')
                                    new_game()
                            else:
                                print('Zadejte prosím 1/2')
                    else:
                        print('| -> Zadejte prosím 1/2')
                elif total_score_calculating(dealer_deck) == total_score_calculating(player_deck):
                    print('| -> stejne')
                    game_choice = 0
                elif total_score_calculating(dealer_deck) > total_score_calculating(player_deck):
                    print('| -> prohral jsi')
                    game_choice = 0
            else:
                print('| -> Nelze vsadi tolik tokenů')
                game_choice = 0
        while game_choice != 1 and game_choice != 2 and game_choice != 3:
            print('| -> Zadejte prosím 1/2/3')
            game_choice = 0
            new_game()

new_game()
