import random
import BlackJack


wins_on_hit = [0] * 23
wins_on_stand = [0] * 23
loss_on_hit = [0] * 23
loss_on_stand = [0] * 23
draw = [0] * 23
turns = 0


print("PHV|WoH|LoH|WoS|LoS|Draw")
for turns in range(100000):
    hit_or_stay = random.randint(0, 1)
    deck = BlackJack.Deck()
    player = BlackJack.Player()
    dealer = BlackJack.Dealer()
    player.players_turn(deck)
    player.players_turn(deck)
    player_hand_value = player.get_player_hand_value()
    dealer.dealers_turn(deck)
    dealer_hand_value = dealer.get_dealer_hand_value()
    if hit_or_stay == 0:
        player.players_turn(deck)
        if player.black_jack():
            wins_on_hit[player_hand_value] += 1
        elif dealer.black_jack():
            loss_on_hit[player_hand_value] += 1
        elif player.get_player_hand_value() < dealer.get_dealer_hand_value() < 21:
            loss_on_hit[player_hand_value] += 1
        elif dealer.get_dealer_hand_value() < player.get_player_hand_value() < 21:
            wins_on_hit[player_hand_value] += 1
        elif player.get_player_hand_value() == dealer.get_dealer_hand_value():
            draw[player_hand_value] += 1
    elif hit_or_stay == 1:
        if player.black_jack():
            wins_on_stand[player_hand_value] += 1
        elif dealer.black_jack():
            loss_on_stand[player_hand_value] += 1
        elif player.get_player_hand_value() < dealer.get_dealer_hand_value() < 21:
            loss_on_stand[player_hand_value] += 1
        elif dealer.get_dealer_hand_value() < player.get_player_hand_value() < 21:
            wins_on_stand[player_hand_value] += 1
        elif player.get_player_hand_value() == dealer.get_dealer_hand_value():
            draw[player_hand_value] += 1

for index in range(4, 22):
    print(f'{index} | {wins_on_hit[index]} | {loss_on_hit[index]} | {wins_on_stand[index]} | {loss_on_stand[index]}'
          f' | {draw[index]}')



