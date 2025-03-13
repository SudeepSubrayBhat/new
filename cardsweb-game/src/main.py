# main.py

from game import Deck

def main():
    deck = Deck()
    deck.shuffle()

    player_hand = [deck.deal() for _ in range(5)]
    print("Player's hand:", player_hand)

if __name__ == "__main__":
    main()