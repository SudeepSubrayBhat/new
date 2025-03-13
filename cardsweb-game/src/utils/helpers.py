def shuffle_deck(deck):
    import random
    random.shuffle(deck)
    return deck

def deal_hand(deck, hand_size):
    hand = deck[:hand_size]
    del deck[:hand_size]
    return hand

def validate_input(user_input, valid_options):
    return user_input in valid_options

def display_hand(hand):
    return ', '.join(str(card) for card in hand)