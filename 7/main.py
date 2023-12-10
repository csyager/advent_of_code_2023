from collections import defaultdict
import functools

with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

hand_ranks = {
    'five_of_a_kind': 1,
    'four_of_a_kind': 2,
    'full_house': 3,
    'three_of_a_kind': 4,
    'two_pair': 5,
    'one_pair': 6,
    'high_card': 7
}

card_ranks = {'A': 1, 'K': 2, 'Q': 3, 'J': 13, 'T': 4, '9': 5, '8': 6, '7': 7,
'6': 8, '5': 9, '4': 10, '3': 11, '2': 12}

class Hand():
    def __init__(self, cards, bid):
        self.cards = sorted(cards, key=lambda x: card_ranks[x])
        self.unsorted_cards = cards
        self.bid = bid

    def __str__(self):
        return f"{self.cards} {self.bid}"


    def classify_hand(self):
        counts = defaultdict(int)
        jokers = 0
        for card in self.cards:
            if card == 'J':
                jokers += 1
            else:
                counts[card] += 1
        values = sorted(counts.values(), reverse=True)
        if jokers == 5:
            return 'five_of_a_kind'
        if values[0] == 5:
            return 'five_of_a_kind'
        if values[0] == 4:
            if jokers > 0:
                return 'five_of_a_kind'
            else:
                return 'four_of_a_kind'
        if values[0] == 3 and len(values) > 1 and values[1] == 2:
            return 'full_house'
        if values[0] == 3:
            if jokers == 2:
                return 'five_of_a_kind'
            elif jokers == 1:
                return 'four_of_a_kind'
            else:
                return 'three_of_a_kind'
        if values[0] == 2 and len(values) > 1 and values[1] == 2:
            if jokers == 1:
                return 'full_house'
            return 'two_pair'
        if values[0] == 2:
            if jokers == 3:
                return 'five_of_a_kind'
            elif jokers == 2:
                return 'four_of_a_kind'
            elif jokers == 1:
                return 'three_of_a_kind'
            else:
                return 'one_pair'
        else:
            if jokers == 5:
                return 'five_of_a_kind'
            elif jokers == 4:
                return 'five_of_a_kind'
            elif jokers == 3:
                return 'four_of_a_kind'
            elif jokers == 2:
                return 'three_of_a_kind'
            elif jokers == 1:
                return 'one_pair'
            else:
                return 'high_card'



def compare_hands(self, hand):
    print(f"comparing {self} to {hand}")
    this_class = self.classify_hand()
    other_class = hand.classify_hand()
    print(f"self is {this_class}, hand is {other_class}")
    if hand_ranks[this_class] < hand_ranks[other_class]:
        print(f"hand {self} beats hand {hand}")
        return 1
    elif hand_ranks[this_class] > hand_ranks[other_class]:
        print(f"hand {hand} beats hand {self}")
        return -1
    else:
        for i in range(5):
            if card_ranks[self.unsorted_cards[i]] < card_ranks[hand.unsorted_cards[i]]:
                print(f"highest diff card {self.cards[i]} beats {hand.cards[i]}")
                return 1
            elif card_ranks[self.unsorted_cards[i]] > card_ranks[hand.unsorted_cards[i]]:
                print(f"highest diff card {hand.cards[i]} beats {self.cards[i]}")
                return -1



def part_1():
    hands = []
    for line in lines:
        cards = line.split()[0]
        bid = line.split()[1]
        hand = Hand(cards, bid)
        hands.append(hand)

    hands.sort(key=functools.cmp_to_key(compare_hands))
    for hand in hands:
        print(hand)

    res = 0
    for i in range(len(hands)):
        res += int(hands[i].bid) * (i + 1)

    print(res)

part_1()
