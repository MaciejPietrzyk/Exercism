def value_of_card(card):
   if card in ('K', 'Q', 'J'):
       return 10
   elif card == 'A':
       return 1
   else:
       return int(card)


def higher_card(card_one, card_two):
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)

    if value_one > value_two:
        return card_one
    elif value_two > value_one:
        return card_two
    else:
        return card_one, card_two


def value_of_ace(card_one, card_two):
    if card_one == 'A' or card_two == 'A':
        return 1
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)
    if value_one + value_two <= 10:
        return 11
    else:
        return 1

def is_blackjack(card_one, card_two):
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)

    if card_one == 'A' and value_two == 10:
        return True
    elif card_two == 'A' and value_one == 10:
        return True
    else:
        return False
    
def can_split_pairs(card_one, card_two):
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)

    if value_one == value_two:
        return True
    else:
        return False


def can_double_down(card_one, card_two):
    value = value_of_card(card_one) + value_of_card(card_two)
    return value in (9, 10, 11)

    if card_one == 'A':
        value_one = 11

    if card_two == 'A':
        value_two = 11

    value = value_one + value_two

    if value in (9, 10, 11):
        return True
    else:
        return False
