import random
from card import PlayingCard

class CardDeck:
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = 'Clubs Diamonds Hearts Spades'.split()

    def __init__(self):
        self._create_deck()

    def _create_deck(self):
        self._cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = PlayingCard(rank, suit)
                self._cards.append(card)

    @property
    def cards(self):
        return self._cards

    # cards = property(cards) # getter, deleter, doc

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()

    @classmethod
    def get_ranks(cls):
        return cls.RANKS

    @classmethod
    def get_ranks(cls):
        return cls.RANKS

    @staticmethod
    def double(value):
        return value * 2
    
    def __len__(self):  # responds to len() 
        return len(self._cards)
    
    def __str__(self):
        class_name = type(self).__name__
        return f"{class_name}/{len(self)}"

    def __repr__(self):
        class_name = type(self).__name__
        return f"{class_name}()"


if __name__ == "__main__":
    d1 = CardDeck()
    d1.shuffle()
    print(f"{d1.cards = }")
    for _ in range(5):
        card = d1.draw()
        print(f"{card = }")
    print(f"{d1.get_ranks() = }")
    print(f"{CardDeck.get_ranks() = }")
    
    print(CardDeck.double(5))
    print(d1.double(100))

    print(f"{len(d1) = }")
    print(d1)
    print(f"{d1 = }")
