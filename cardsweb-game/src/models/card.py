class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f"{self.rank} of {self.suit}"

    def compare(self, other):
        rank_order = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        if rank_order.index(self.rank) > rank_order.index(other.rank):
            return 1
        elif rank_order.index(self.rank) < rank_order.index(other.rank):
            return -1
        else:
            return 0