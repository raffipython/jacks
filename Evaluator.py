# -*- coding: utf-8 -*-
from collections import Counter
class Evaluator(object):

    def __init__(self):
        pass

    @staticmethod
    def Picker(hand):

        """
        multiplier
        250 Royal Flush     | 250 | 500 | 750 | 1000 | 1250 | # [4000]
        50 Straight Flush   | 50  | 100 | 150 | 200  | 250  |
        25 Four of a Kind   | 25  | 50  | 75  | 100  | 125  |
        9 Full House        | 9   | 18  | 27  | 36   | 45   |
        6 Flush             | 6   | 12  | 18  | 24   | 30   |
        4 Straight          | 4   | 8   | 12  | 16   | 20   |
        3 Three of a Kind   | 3   | 6   | 9   | 12   | 15   |
        2 Two Pair          | 2   | 4   | 6   | 8    | 10   |
        1 Jacks or Better   | 1   | 2   | 3   | 4    | 5    |
        -1 nothing
        """

        h = []
        for i in hand:
            x = i.split("_")
            h.append([x[0], x[1]])

        royal = False    #
        flush = False    #
        straight = False #
        four = False     #
        three = False    #
        two_pair = False
        jacks = False    #
        full = False     #

        suits = []
        num = []

        for i in range(5):
            suits.append(h[i][1])
        #print(suits)

        for i in range(5):
            num.append(int(h[i][0]))
        #print(num)

        spades = suits.count("SPADES")
        diamonds = suits.count("DIAMONDS")
        hearts = suits.count("HEARTS")
        clubs = suits.count("CLUBS")

        if spades == 5 or diamonds == 5 or hearts == 5 or clubs == 5:
            flush = True

        n = sorted(num)
        if 13 in n:
            if n[1] + 1 == n[2] and n[2] + 1 == n[3] and n[3] + 1 == n[4] and n[0] == 1:
                straight = True
        else:
            if n[0] + 1 == n[1] and n[1] + 1 == n[2] and n[2] + 1 == n[3] and n[3] + 1 == n[4]:
                straight = True

        if straight and flush and 13 in num:
            royal = True

        if num.count(1) == 4 or num.count(2) == 4 or num.count(3) == 4 or num.count(4) == 4 or num.count(
            5) == 4 or num.count(6) == 4 or num.count(7) == 4 or num.count(8) == 4 or num.count(9) == 4 or num.count(
            10) == 4 or num.count(11) == 4 or num.count(12) == 4 or num.count(13) == 4:
            four = True

        if num.count(1) == 3 or num.count(2) == 3 or num.count(3) == 3 or num.count(4) == 3 or num.count(
            5) == 3 or num.count(6) == 3 or num.count(7) == 3 or num.count(8) == 3 or num.count(9) == 3 or num.count(
            10) == 3 or num.count(11) == 3 or num.count(12) == 3 or num.count(13) == 3:
            three = True

        if three:
            if num.count(1) == 2 or num.count(2) == 2 or num.count(3) == 2 or num.count(4) == 2 or num.count(
                5) == 2 or num.count(6) == 2 or num.count(7) == 2 or num.count(8) == 2 or num.count(
                9) == 2 or num.count(10) == 2 or num.count(11) == 2 or num.count(12) == 2 or num.count(13) == 2:
                full = True

        # Fake only one pair
        if Counter(num).values().count(2) == 2:
            two_pair = True

        if num.count(1) == 2 or num.count(11) == 2 or num.count(12) == 2 or num.count(13) == 2:
            jacks = True

        if royal:
            print "\nRoyal Flush"
            return 250
        elif straight and flush:
            print "\nStraight Flush"
            return 50
        elif four:
            print "\nFour of a kind"
            return 25
        elif full:
            print "\nFull House"
            return 9
        elif flush:
            print "\nFlush"
            return 6
        elif straight:
            print "\nStraight"
            return 4
        elif three:
            print "\nThree of a kind"
            return 3
        elif two_pair:
            print "\nTwo Pairs"
            return 2
        elif jacks:
            print "\nJacks or better"
            return 1
        else:
            print "\nHigh Card"
            return -1

