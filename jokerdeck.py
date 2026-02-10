from carddeck import CardDeck
from card import PlayingCard

class CardGame:
    def play(self):
        print("Playing")

class JokerDeck(CardDeck, CardGame):
    def _create_deck(self):
        super()._create_deck()
        for joker_number in 1, 2:
            card = PlayingCard(f"Joker {joker_number}", "*** JOKER ***")
            self._cards.append(card)

if __name__ == "__main__":
    j = JokerDeck()
    j.shuffle()
    print(j.cards)
    print()
    for _ in range(5):
        print(j.draw())
    j.play()
    print(j)
    print(f"{j = }")
