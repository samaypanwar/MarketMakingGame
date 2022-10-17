from itertools import product
import random
from collections import Counter
import math
import numpy as np


class Deck:

    suit = ('hearts', 'spades', 'diamonds', 'clubs')
    ranks = ('two', 'three', 'four', 'five', 'six', 'seven', 'eight',
             'nine', 'ten', 'jack', 'queen', 'king', 'ace')
    values = {
            'two'  : 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7,
            'eight': 8, 'nine': 9, 'ten': 10, 'jack': 11,
            'queen': 12, 'king': 13, 'ace': 1,
            }

    def __init__(self):
        self.deck = list(product(Deck.ranks, Deck.suit))
        random.shuffle(self.deck)

    def draw_card(self):
        if len(self.deck) == 0:
            return 0
        else:
            return self.deck.pop()

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def value(self, card):
        return self.values[card[0]]

    def name(self, card):
        print(f"{card[0].title()} of {card[1].title()}")


class Round:

    def __init__(self, number_of_cards: int = 3):
        self.deck = Deck()
        self.number_of_cards = number_of_cards
        self.MAX_NUM = self.number_of_cards * self.deck.values['king']
        self.MIN_NUM = self.number_of_cards * self.deck.values['ace']
        self.TRUE_SUM = 0
        self.cards = []

    def get_offer(self):

        offer = random.randint(self.MIN_NUM, self.MAX_NUM)
        p = random.random()

        if p > 0.95:

            if offer < self.TRUE_SUM:
                offer_type = 'S'
            else:
                offer_type = 'B'

        else:
            if offer < self.TRUE_SUM:
                offer_type = 'B'
            else:
                offer_type = 'S'

        return offer, offer_type

    def play(self):

        self.cards = [self.deck.draw_card() for _ in range(self.number_of_cards)]

        self.TRUE_SUM = sum([self.deck.value(card) for card in self.cards])

        offer, offer_type = self.get_offer()

        print()
        user_result = input(f"An offer has been proposed: {offer}@{offer_type} \n Would you like to transact? [Y/n]")

        while user_result.lower() not in ['y', 'n']:
            user_result = input("Would you like to transact? [Y/n]")

        if user_result.lower() == 'n':
            return 0

        else:
            # USER SIZE
            # EXPECTED MAX LOSS / GAIN / EXPECTED GAIN
            order_size = int(input("Please input your order size?"))
            estimated_max_loss = float(input("Estimated Max Loss: "))
            estimated_max_gain = float(input("Estimated Max Gain: "))
            estimated_expected_gain = float(input("Estimated Expected Gain: "))

            print("Revealing cards...")
            for card in self.cards:
                self.deck.name(card)

            print("True Sum: ", self.TRUE_SUM)
            estimated_pnl = float(input("What is your Gain/Loss?"))

            while abs(estimated_pnl) != order_size * abs(self.TRUE_SUM - offer):
                estimated_pnl = float(input("What is your Gain/Loss?"))

            if offer_type == "B":
                return order_size * (self.TRUE_SUM - offer)
            elif offer_type == "S":
                return order_size * (offer - self.TRUE_SUM)

        "TODO: print other player markets and give option to revise to main player"
        "TODO: then at the end of the game, reveal card by card to update EV for all players"
        "TODO: ask position at the end of the game"


class MarketMaker:

    def __init__(self):
        ...
