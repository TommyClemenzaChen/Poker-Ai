import random

#create a card class for a game of poker
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def getSuit(self):
        return self.suit
    def getRank(self):
        return self.rank
    def __str__(self):
        return str(self.rank) + " of " + str(self.suit)
    
class Deck:
    def __init__(self, cards):
        self.cards = cards

    def createDeck(self):
        for x in ["spades", "hearts", "clubs", "diamonds"]:
            for y in ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]:
                self.cards.append(Card(x,y))
        self.shuffle()
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def empty(self):
        return len(self.cards) == 0
    
class player:
    def __init__(self, hand, money):
        #list of 2 cards
        self.hand = hand
        self.money = money
        self.bet = 0

    #Actions
    def fold(self):
        self.cards = []
    
    def bet(self, amount):
        self.bet += amount
    
    def showCard(self, index):
        return self.cards[index]
    
    #Getters
    def getBet(self):
        return self.bet

    def getCards(self):
        return self.cards
    
    def getMoney(self):
        return self.money
    
class game:
    def __init__(self, flop):
        self.flop = flop
        self.pot = 0
        self.players = []
        self.deck = self.deck.createDeck()
    
    def addPlayer(self, player):
        self.players.append(player)

    
    
    
    