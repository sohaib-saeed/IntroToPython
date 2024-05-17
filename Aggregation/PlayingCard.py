import random


class PlayingCard:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.value_str = self._get_value_str()
        self.suit_str = self._get_suit_str()

    def _get_value_str(self):
        if self.value == 1:
            return "Ace"
        elif self.value == 11:
            return "Jack"
        elif self.value == 12:
            return "Queen"
        elif self.value == 13:
            return "King"
        else:
            return str(self.value)

    def _get_suit_str(self):
        if self.suit == 1:
            return "Hearts"
        elif self.suit == 2:
            return "Diamonds"
        elif self.suit == 3:
            return "Clubs"
        else:
            return "Spades"


class Hand:
    def __init__(self):
        self.__cards = []
        self._deal_cards()

    def _deal_cards(self):
        for i in range(5):
            value = random.randint(1,13)
            suit = random.randint(1,4)
            card = PlayingCard(value, suit)
            while card in self.__cards:
                value = random.randint(1, 13)
                suit = random.randint(1, 4)
                card = PlayingCard(value, suit)
            self.__cards.append(card)
    def display(self):
        for card in self.__cards:
            print(f"{card.value_str} of {card.suit_str}")


def main():
    hand = Hand()
    hand.display()
    print("-------------")
    h2 = Hand()
    h2.display()
if __name__ == "__main__":
    main()
