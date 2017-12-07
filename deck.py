import card
import random
from random import shuffle
import datetime

class Deck:
	def __init__(self):
		rank = "0"
		suit = " "
		count = 0
		self.dealt = 0
		self.deckArray = []
		for r in range(1, 14):
			if r == 1:
				rank = "A"
			elif r == 10:
				rank = "T"
			elif r == 11:
				rank = "J"
			elif r == 12:
				rank = "Q"
			elif r == 13:
				rank = "K"
			else:
				rank = str(r)
			for s in range(1, 5):
				if s == 1:
					suit = "s"
				if s == 2:
					suit = "c"
				if s == 3:
					suit = "d"
				if s == 4:
				    suit = "h"
					
				newCard = card.Card(rank, suit)
				
				self.deckArray.append(newCard)
				count += 1
				
	def dispDeck(self):
		'''This method for debugging purposes '''
		for c in range(0, len(self.deckArray)):
			print(self.deckArray[c].getRank() + self.deckArray[c].getSuit())
	
	def shuffleDeck(self, seed):
		
		random.seed(seed)
		iterations = random.randint(100, 200)
		oldDeck = list(self.deckArray)
		#for x in range(0, iterations):
		oldDeck = list(self.deckArray)
		for y in range(0, len(oldDeck)):
			sysran = random.SystemRandom()
			sysran.seed(seed * y)
			deleteNum = sysran.randint(0, len(oldDeck) - 1)
			self.deckArray[y] = oldDeck[deleteNum]
			oldDeck.pop(deleteNum)
		
	def dealCard(self):
		dealing = self.deckArray[self.dealt]
		self.dealt += 1
		return dealing
		
	def removeCard(self, inCard):
		#Find card
		found = False
		for c in range(0, len(self.deckArray)):
			if found == False:
				if self.deckArray[c].getRank() == inCard.getRank() and self.deckArray[c].getSuit() == inCard.getSuit():
					self.deckArray.pop(c)
					found = True
