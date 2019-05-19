suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10,
          'Queen': 10, 'King': 10, 'Ace': 11}

import random
playing = True

######################################################################


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:

    def __init__(self):

        self.deck = []

        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))  # i think if we want more decks it has to be done here..

    def __str__(self):

        deck_comp = ""

        for card in self.deck:
            deck_comp += "\n" + card.__str__()
        return deck_comp

    def shuffle(self):

        random.shuffle(self.deck)

    def deal(self):

        single_card = self.deck.pop()

        return single_card


class Hand:

    def __init__(self):

        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):

        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == "Ace":
            self.aces += 1

    def adjust_for_ace(self):

        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1


class Chips:

    def __init__(self, total=0):
        self.total = total  # can set to user input
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

    def __str__(self):
        print(str(self.total))


def make_bet(chips):
    while True:

        chips.bet = int(input(f"How much would you like to bet? ({player_chips.total} Available) "))

        if chips.bet > chips.total:
            print(f"Insufficient Chips, you only have {chips.total} chips to play with.")

        else:
            break


def hit(deck, hand):

    single_card = deck.deal()  # pops off one card from the list of 52 card objects
    hand.add_card(single_card)  # add.card(), this adds that card to the hand (self.cards[])..
    hand.adjust_for_ace()  # adjusts hand for ACE..lol


def hit_or_stand(deck, hand):  # ask if they want to hit or stand..

    global playing

    while True:  # this loop seems to keep asking for a card, but it will be controlled by a while loop <21 ..

        x = input("Hit or Stand [h/s]")
        if x == "h":
            hit(deck, hand)

        elif x == "s":
            print("Player stands, dealers' turn..")
            playing = False

        else:
            print("Entry invalid, enter either 'h' or 'f'.. ")
            continue
        break


def show_some(player, dealer):

    print()
    print("Dealer card..")
    print(dealer.cards[1])
    print()

    print()
    print("Player cards..")
    for card in player.cards:
        print(card)
    print(f"Player total: {player.value} ")
    print()


def show_all(player, dealer):

    print()
    print("Players Cards")
    for card in player.cards:
        print(card)
    print(f"Player total: {player.value} ")
    print()


    print("Dealers cards")
    for card in dealer.cards:
        print(card)
    print(f"Dealer total: {dealer.value}")
    print()


def player_bust(player, chips, ):
    print("BUSTqq")
    chips.lose_bet()


def player_win(player, chips):
    print("Player Win")
    chips.win_bet()


def dealer_bust(dealer, chips):
    print("Dealer Bust, player wins")
    chips.win_bet()


def dealer_win(dealer, chips):
    print("Dealer wins")
    chips.lose_bet()


def push():
    print("PUSH")

def buy_in(Chips):

    Chips.total = int(input("How many chips would you like?"))

####################################################################################



player_chips = Chips()

while True:
    playing = True
    deck = Deck()
    player1 = Hand()
    dealer = Hand()

    print("Welcome to blackjack.1.\n")

    if player_chips.total <= 0:
        buy_in(player_chips)

    make_bet(player_chips)

    deal = input("To deal the cards , enter 'd' :")

    if deal == "d":

        deck.shuffle()

        player1.add_card(deck.deal())
        player1.add_card(deck.deal())
        player1.adjust_for_ace()

        dealer.add_card(deck.deal())
        dealer.add_card(deck.deal())
        dealer.adjust_for_ace()

        show_some(player1, dealer)

    while playing:

        hit_or_stand(deck, player1)

        show_some(player1, dealer)

        if player1.value > 21:

            player_bust(player1, player_chips)
            player_chips.lose_bet()
            show_all(player1, dealer)

            while dealer.value < 17:
                hit(deck, dealer)
                show_all(player1, dealer)
                

            print("You lose!!!!!")
        break


    if player1.value <= 21:

        while dealer.value < 17:
            hit(deck, dealer)

        show_all(player1, dealer)


    if dealer.value > 21:
        dealer_bust(dealer, player_chips)



    elif player1.value > dealer.value:
        player_win(player1, player_chips)


    elif player1.value < dealer.value:
        dealer_win(dealer, player_chips)


    else:
        push()



    if player_chips.total <= 0:
        print("You have run out of chips\n")
        rebuy = input("Would you like to rebuy? [Y/N]: ")
        if rebuy == "Y":
            buy_in(player_chips)
            playing = True
        else:
            print("Thanks for playing!")
            break


































