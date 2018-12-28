# -*- coding: utf-8 -*-

class Card(object):

    def __init__(self):
        self.card = ""
        self.suit = ""
        self.symbol = {"CLUBS": "♣", "HEARTS": "♥", "DIAMONDS": "♦", "SPADES": "♠"}

    def render_card(self, c):
        parts = c.split("_")
        self.card = parts[0]
        self.suit = parts[1]
        if self.card == '1':
            rank = "A"
            space = ' '
        elif self.card == '10':
            rank = self.card
            space = ''
        elif int(self.card) > 10:
            suits = {"11": "J", "12": "Q", "13": "K"}
            rank = suits.get(self.card)
            space = ' '
        else:
            rank = self.card
            space = ' '

        suit = self.symbol.get(self.suit)
        lines = [[] for i in range(9)]

        # add the individual card on a line by line basis
        lines[0].append('┌─────────┐')
        lines[1].append('│{}{}       │'.format(rank, space))  # use two {} one for char, one for space or char
        lines[2].append('│         │')
        lines[3].append('│         │')
        lines[4].append('│    {}    │'.format(suit))
        lines[5].append('│         │')
        lines[6].append('│         │')
        lines[7].append('│       {}{}│'.format(space, rank))
        lines[8].append('└─────────┘')

        # make each line into a single list
        for index, line in enumerate(lines):
            lines[index] = ''.join(line)

        # convert the list into a single string
        return '\n'.join(lines)

