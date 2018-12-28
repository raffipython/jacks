# -*- coding: utf-8 -*-

import random
from pprint import pprint
from Card import Card
from Evaluator import Evaluator

import sys
sys.path.append(".")

class Blackjack():
    """Main Blackjack class"""

    def __init__(self, bal):
        """ Init method """
        self.bet = 5
        self.balance = bal
        self.cards = []

        self.deck = self.deck_builder()
        self.c = Card()
        self.holds = []
        self.hands = []


    def deck_builder(self):
        """ Deck builder method """
        main_deck = []
        for suit in ["CLUBS", "HEARTS", "DIAMONDS", "SPADES"]:
            for card in xrange(13):
                main_deck.append("{}_{}".format(card + 1, suit))
        return main_deck

    def deck_remove_card(self, index):
        """ Removes a card at given index """
        del self.deck[index]

    def next_card(self):
        """ Returns a random card from the deck """
        index = random.randint(0, len(self.deck) - 1)
        return [index, self.deck[index]]

    def update_bet(self, bet):
        """ Updates """
        self.bet = bet



    def get_holds(self):
        x = []
        i = raw_input("Which cards to hold ex. 145\n")
        for a in range(len(i)):
            x.append(int(i[a]))
        self.holds = sorted(x)
        print("\n")

    @staticmethod
    def card_value(card):
        """ Returns the value of a card or asks the player if the card is an Ace """
        c = int(card.split("_")[0])
        if c == 1:
            good_input = False
            while not good_input:
                x = raw_input("\nDrawn an Ace, count as 1 or 11? [Enter 1 or 11]\n".strip())
                try:
                    c = int(x)
                    good_input = True
                except:
                    print "Error, please try again"

        elif c > 9:
            c = 10
        return c


    def menu(self):
        print("""
        ____________________________________________________
        |Royal Flush     | 250  | 500  | 750  | 1000 | 4000 |    
        |Straight Flush	 | 50   | 100  | 150  | 200  | 250  |
        |Four of a Kind	 | 25   | 50   | 75   | 100  | 125  |
        |Full House	     | 9    | 18   | 27   | 36   | 45   |
        |Flush	         | 6    | 12   | 18   | 24   | 30   |
        |Straight	     | 4    | 8    | 12   | 16   | 20   |
        |Three of a Kind | 3    | 6    | 9    | 12   | 15   |
        |Two Pair	     | 2    | 4    | 6    | 8    | 10   | 
        |Jacks or Better | 1    | 2    | 3    | 4    | 5    |
        ----------------------------------------------------
        """)

    def gui(self):
        print("\033[H\033[J")
        one = self.cards[0].split("\n")
        two = self.cards[1].split("\n")
        three = self.cards[2].split("\n")
        four = self.cards[3].split("\n")
        five = self.cards[4].split("\n")
        for i in range(9):
            print("        {}{}{}{}{}".format(one[i], two[i], three[i], four[i], five[i]))

    def get_result(self):
        """ Returns index of winning hand """
        m = Evaluator.Picker(self.hands)
        print("Multiplier:  {}".format(m))
        return m * self.bet


def get_money():
    with open('money.txt', 'r') as fd:
        f = fd.read()
    return int(f.split("\n")[0])


def write_money(money):
    with open('money.txt', 'w') as fd:
        fd.write(str(money) + "\n")


def main():
    """ Main method """
    end_game = False
    global balance
    balance = get_money()
    counter = 0
    while not end_game:
        try:
            j = Blackjack(balance)
            for i in range(5):
                n = j.next_card()
                j.cards.append(j.c.render_card(n[1]))
                j.hands.append(n[1])
                j.deck_remove_card(n[0])
            j.gui()
            j.get_holds()

            h = []
            for i in [1, 2, 3, 4, 5]:
                if i not in j.holds:
                    h.append(i)

            for x in h:
                n = j.next_card()

                j.cards[x-1] = j.c.render_card(n[1])
                j.hands[x-1] = n[1]
            j.gui()

            balance += j.get_result()
            print("Balance:     {}".format(balance))
            write_money(balance)

            with open('end.txt', 'r') as fd:
                f = fd.read()
                if f.split("\n")[0] == "yes":
                    end_game = True
            counter += 1
            print("Counter      {}".format(counter))
            raw_input("Press any key...")
        except KeyboardInterrupt:
            quit(0)



if __name__ == '__main__':
    main()





