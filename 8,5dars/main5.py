#      https://www.codewars.com/kata/56f399b59821793533000683/train/python


def sort_cards(cards):
    order = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
    return sorted(cards, key=lambda card: order.index(card))

sorted_cards = sort_cards(['3', '9', 'A', '5', 'T', '8', '2', '4', 'Q', '7', 'J', '6', 'K'])
print(sorted_cards)
