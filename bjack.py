# Milestone project 2: Blackjack

import random

# declare some arrays to hold card values.
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five',
         'Six', 'Seven', 'Eight', 'Nine',
         'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5,
          'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

# control boolean
playing = True


# card class
class Card():

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit


# deck class
class Deck():

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return "The deck has: " + deck_comp

    def shuffle(self):
        '''
        Shuffles the cards in the list.
        '''
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()


# class for the Hand.
class Hand():
    def __init__(self):
        self.cards = []  # a list to hold the cards in the hand.
        self.value = 0   # the value of the hand, using the global dictionary.
        self.aces = 0    # handle the ace values separately.

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1  # add to self.aces

    def print_hand(self):
        hand_comp = ''
        for card in self.cards:
            hand_comp += ' ' + card.__str__()
        return "Your hand is: " + hand_comp

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


# track the player chip count
class Chips():
    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


# let the functions begin!
def take_bet(stack):
    while stack.bet < stack.total:
        try:
            stack.bet = int(input("Place your bets. "))
            return stack.bet
        except:
            print("Whoops! you can't cover that amount. Or you entered a non numeric value.")


# hit
def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing

    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's' ")

        if x[0].lower() == 'h':
            hit(deck, hand)  # hit() function defined above

        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False

        else:
            print("Sorry, please try again.")
            continue
        break


# show the cards
def show_some(player, dealer):
    print('Dealer\'s Hand: ')
    print('one card hidden!')
    print(dealer.cards[1])
    print('\n')
    print('Player\'s Hand: ')
    for card in player.cards:
        print(card)
    print('\n')


def show_all(player, dealer):
    print('Dealer\'s Hand: ')
    for card in dealer.cards:
        print(card)
    print('\n')
    print('Player\'s Hand: ')
    for card in player.cards:
        print(card)
    print('\n')


# win condition situations
def player_busts(player, dealer, chips):
    print("BUST player!")
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print("Player wins!")
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print("BUST dealer!")
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print("Dealer wins!")
    chips.lose_bet()


def push():
    print("Dealer and player tie! PUSH!")


# def main():
# if __name__ == "__main__"
while True:
    # Print an opening statement
    print("Welcome to blackjack!")

    # Create & shuffle the deck, deal two cards to each player
    game_deck = Deck()
    game_deck.shuffle()

    player = Hand()
    npc = Hand()

    for i in range(0, 2):
        player.add_card(game_deck.deal())
        npc.add_card(game_deck.deal())
    # Set up the Player's chips
        p_chips = Chips()

    # Prompt the Player for their bet
    take_bet(p_chips)

    # Show cards (but keep one dealer card hidden)
    show_some(player, npc)

    while playing:  # recall this variable from our hit_or_stand function

        # Prompt for Player to Hit or Stand
        hit_or_stand(game_deck, player)
        # Show cards (but keep one dealer card hidden)
        show_some(player, npc)
        if player.value > 21:
            player_busts(player, npc, p_chips)
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17

        if player.value <= 21:
            while npc.value < 17:
                hit(game_deck, npc)

        # Show all cards
        show_all(player, npc)
        # Run different winning scenarios
        if npc.value > 21:
            dealer_busts(player, npc, p_chips)
        elif npc.value > player.value:
            dealer_wins(player, npc, p_chips)
        elif npc.value < player.value:
            player_wins(player, npc, p_chips)
        else:
            push(player, npc)

    # Inform Player of their chips total
    print("\nPlayer's winnings stand at", p_chips.total)
    # Ask to play again
    newgame = input("Would you like to play another hand? y/n ")
    if newgame[0].lower() == 'y':
        playing = True
        continue
    else:
        print("Thanks for playing!")
        break
