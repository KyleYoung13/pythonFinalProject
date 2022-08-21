import random


# https://stackoverflow.com/questions/41970795/what-is-the-best-way-to-create-a-deck-of-cards

def faces():
    return ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]


def suits():
    return ["Clubs", "Diamonds", "Hearts", "Spades"]


class Card:
    def __init__(self, face, suit):
        self._face = face
        self._suit = suit

    def get_card_value(self):
        if self._face == "Q" or self._face == "J" or self._face == "K":
            return 10
        elif self._face == "A":
            return 11
        else:
            return int(self._face)


class Deck:
    def __init__(self):
        self._cards = []
        self._cards = [Card(face, suit) for face in faces() for suit in suits()]
        random.shuffle(self._cards)

    def get_cards(self):
        return self._cards.pop()


class Hand:
    def __init__(self):
        self._cards = []

    def add_card(self, card):
        self._cards.append(card)

    def get_hand_value(self):
        value = 0
        for card in self._cards:
            value += card.get_card_value()
        return value



class Dealer:
    def __init__(self):
        self._hand = Hand()

    def dealers_turn(self, deck):
        while self._hand.get_hand_value() < 17:
            self._hand.add_card(deck.get_cards())

    def get_dealer_hand_value(self):
        return self._hand.get_hand_value()

    def black_jack(self):
        if self.get_dealer_hand_value() == 21:
            return True
        elif self.get_dealer_hand_value() > 21:
            return False
        elif self.get_dealer_hand_value() < 21:
            return False


class Player:

    def __init__(self):
        self._hand = Hand()

    def players_turn(self, deck):
        self._hand.add_card(deck.get_cards())

    def get_player_hand_value(self):
        return self._hand.get_hand_value()

    def black_jack(self):
        if self.get_player_hand_value() == 21:
            return True
        elif self.get_player_hand_value() > 21:
            return False
        elif self.get_player_hand_value() < 21:
            return False




