class PlayingCard:  # inherits from 'object'
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    @property
    def rank(self):  # getter property
        return self._rank

    @rank.setter
    def rank(self, value): # setter property
        if isinstance(value, str):
            self._rank = value    
        else:
            raise TypeError(f"rank must be str, not {type(value).__name__}")

    @property
    def suit(self):
        return self._suit
    
    @suit.setter
    def suit(self, value):
        if isinstance(value, str):
            self._suit = value    
        else:
            raise TypeError(f"suit must be str, not {type(value).__name__}")

    def __str__(self):  # human-friendly view
        return f"{self.rank}-{self.suit}"

    def __repr__(self):  # how to recreate object
        return f"PlayingCard('{self.rank}', '{self.suit}')"

if __name__ == "__main__":
    c1 = PlayingCard('8', 'Diamonds')
    c2 = PlayingCard('A', 'Hearts')
    print(f"{type(c1.rank) = }")
    print(f"{type(PlayingCard.rank) = }")
    
    print(f"{c1.rank = }")
    c1.rank = '7'  # rank setter value
    # c1.rank = 48
    print(f"{c1 = }")  # repr(c1)
    print(c1)          # str(c1)

    