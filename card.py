class Card:
	def __init__(self, rank, suit):
		self.rank = rank
		self.suit = suit
	def getRank(self):
		return self.rank
	def getSuit(self):
		return self.suit
	def getCardStr(self):
		return self.rank + self.suit
