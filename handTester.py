import unittest
import handAnalyzer
import card

class TestRankFunctions(unittest.TestCase):
	def testQuadFunction(self):
		hand1 = [card.Card("A", "h"), card.Card("A", "d"), card.Card("A", "c"), card.Card("A", "s"), card.Card("Q", "h")]
		self.assertTrue(handAnalyzer.quads(hand1) == 13)
		hand1 = [card.Card("A", "d"), card.Card("Q", "d"), card.Card("A", "c"), card.Card("A", "s"), card.Card("A", "h")]
		self.assertTrue(handAnalyzer.quads(hand1) == 13)
		hand1 = [card.Card("A", "h"), card.Card("A", "d"), card.Card("Q", "c"), card.Card("A", "s"), card.Card("A", "h")]
		self.assertTrue(handAnalyzer.quads(hand1) == 13)
		hand1 = [card.Card("A", "h"), card.Card("A", "d"), card.Card("A", "c"), card.Card("Q", "s"), card.Card("A", "h")]
		self.assertTrue(handAnalyzer.quads(hand1) == 13)
		hand1 = [card.Card("Q", "h"), card.Card("A", "d"), card.Card("A", "c"), card.Card("A", "s"), card.Card("A", "h")]
		self.assertTrue(handAnalyzer.quads(hand1) == 13)
		
		hand1 = [card.Card("A", "h"), card.Card("A", "d"), card.Card("A", "c"), card.Card("Q", "s"), card.Card("Q", "h")]
		self.assertTrue(handAnalyzer.quads(hand1) == 0)
		
	def testFullHouseFunction(self):
		hand1 = [card.Card("A", "h"), card.Card("A", "d"), card.Card("A", "c"), card.Card("Q", "s"), card.Card("Q", "h")]
		self.assertTrue(handAnalyzer.fullHouse(hand1) == [13, 11])
		hand1 = [card.Card("A", "d"), card.Card("A", "d"), card.Card("Q", "c"), card.Card("A", "s"), card.Card("Q", "h")]
		self.assertTrue(handAnalyzer.fullHouse(hand1) == [13, 11])
		hand1 = [card.Card("A", "h"), card.Card("Q", "d"), card.Card("Q", "c"), card.Card("A", "s"), card.Card("A", "h")]
		self.assertTrue(handAnalyzer.fullHouse(hand1) == [13, 11])
		hand1 = [card.Card("Q", "h"), card.Card("A", "d"), card.Card("A", "c"), card.Card("Q", "s"), card.Card("A", "h")]
		self.assertTrue(handAnalyzer.fullHouse(hand1) == [13, 11])
		hand1 = [card.Card("Q", "h"), card.Card("A", "d"), card.Card("A", "c"), card.Card("A", "s"), card.Card("Q", "h")]
		self.assertTrue(handAnalyzer.fullHouse(hand1) == [13, 11])
		
		hand1 = [card.Card("A", "h"), card.Card("A", "d"), card.Card("J", "c"), card.Card("Q", "s"), card.Card("Q", "h")]
		self.assertTrue(handAnalyzer.fullHouse(hand1) == [0, 0])
		hand1 = [card.Card("A", "h"), card.Card("A", "d"), card.Card("J", "c"), card.Card("A", "s"), card.Card("Q", "h")]
		self.assertTrue(handAnalyzer.fullHouse(hand1) == [0, 0])
		
	def testFlushFunction(self):
		hand1 = [card.Card("A", "h"), card.Card("K", "h"), card.Card("J", "h"), card.Card("T", "h"), card.Card("Q", "h")]
		self.assertTrue(handAnalyzer.flush(hand1))
		
		hand1 = [card.Card("A", "h"), card.Card("K", "d"), card.Card("J", "h"), card.Card("T", "h"), card.Card("Q", "h")]
		self.assertFalse(handAnalyzer.flush(hand1))
		
	def testStraightFunction(self):
		hand1 = [card.Card("A", "h"), card.Card("K", "h"), card.Card("J", "h"), card.Card("T", "h"), card.Card("Q", "h")]
		self.assertTrue(handAnalyzer.straight(hand1))
		hand1 = [card.Card("T", "h"), card.Card("K", "h"), card.Card("J", "h"), card.Card("A", "h"), card.Card("Q", "h")]
		self.assertTrue(handAnalyzer.straight(hand1))
		
		hand1 = [card.Card("A", "h"), card.Card("K", "d"), card.Card("J", "h"), card.Card("9", "h"), card.Card("Q", "h")]
		self.assertFalse(handAnalyzer.straight(hand1))
		
	def testTripFunction(self):
		hand1 = [card.Card("A", "h"), card.Card("A", "d"), card.Card("A", "c"), card.Card("Q", "s"), card.Card("J", "h")]
		self.assertTrue(handAnalyzer.trips(hand1) == [13, 11, 10])
		hand1 = [card.Card("A", "d"), card.Card("A", "d"), card.Card("J", "c"), card.Card("A", "s"), card.Card("Q", "h")]
		self.assertTrue(handAnalyzer.trips(hand1) == [13, 11, 10])
		hand1 = [card.Card("A", "h"), card.Card("A", "d"), card.Card("Q", "c"), card.Card("K", "s"), card.Card("A", "h")]
		self.assertTrue(handAnalyzer.trips(hand1) == [13, 12, 11])
		hand1 = [card.Card("T", "h"), card.Card("A", "d"), card.Card("A", "c"), card.Card("Q", "s"), card.Card("A", "h")]
		self.assertTrue(handAnalyzer.trips(hand1) == [13, 11, 9])
		hand1 = [card.Card("Q", "h"), card.Card("A", "d"), card.Card("A", "c"), card.Card("A", "s"), card.Card("7", "h")]
		self.assertTrue(handAnalyzer.trips(hand1) == [13, 11, 6])
		
		hand1 = [card.Card("A", "h"), card.Card("A", "d"), card.Card("J", "c"), card.Card("Q", "s"), card.Card("Q", "h")]
		self.assertTrue(handAnalyzer.trips(hand1) == [0, 0, 0])
		hand1 = [card.Card("A", "h"), card.Card("Q", "d"), card.Card("J", "c"), card.Card("A", "s"), card.Card("Q", "h")]
		self.assertTrue(handAnalyzer.trips(hand1) == [0, 0, 0])
		
	def testPairFunction(self):
		hand1 = [card.Card("J", "h"), card.Card("K", "h"), card.Card("J", "h"), card.Card("T", "h"), card.Card("Q", "d")]
		self.assertTrue(handAnalyzer.pair(hand1) == [10, 12, 11, 9])
		hand1 = [card.Card("T", "h"), card.Card("K", "h"), card.Card("J", "h"), card.Card("T", "h"), card.Card("Q", "d")]
		self.assertTrue(handAnalyzer.pair(hand1) == [9, 12, 11, 10])
		hand1 = [card.Card("Q", "h"), card.Card("K", "h"), card.Card("J", "h"), card.Card("T", "h"), card.Card("Q", "d")]
		self.assertTrue(handAnalyzer.pair(hand1) == [11, 12, 10, 9])
		hand1 = [card.Card("J", "h"), card.Card("K", "h"), card.Card("T", "h"), card.Card("Q", "h"), card.Card("Q", "d")]
		self.assertTrue(handAnalyzer.pair(hand1) == [11, 12, 10, 9])
		
		hand1 = [card.Card("A", "h"), card.Card("K", "d"), card.Card("J", "h"), card.Card("9", "h"), card.Card("Q", "h")]
		self.assertTrue(handAnalyzer.pair(hand1) == [0, 0, 0, 0])
		
	def testHighCardFunction(self):
		hand1 = [card.Card("J", "h"), card.Card("K", "h"), card.Card("A", "h"), card.Card("4", "h"), card.Card("3", "c")]
		hand2 = [card.Card("J", "h"), card.Card("K", "h"), card.Card("A", "h"), card.Card("4", "h"), card.Card("3", "c")]
		self.assertTrue(handAnalyzer.highCard(hand1, hand2) == 0)
		
		hand1 = [card.Card("J", "h"), card.Card("K", "h"), card.Card("A", "h"), card.Card("4", "h"), card.Card("3", "c")]
		hand2 = [card.Card("J", "h"), card.Card("K", "h"), card.Card("A", "h"), card.Card("4", "h"), card.Card("2", "c")]
		self.assertTrue(handAnalyzer.highCard(hand1, hand2) == 1)
		
		hand1 = [card.Card("J", "h"), card.Card("K", "h"), card.Card("A", "h"), card.Card("4", "h"), card.Card("2", "c")]
		hand2 = [card.Card("J", "h"), card.Card("K", "h"), card.Card("A", "h"), card.Card("4", "h"), card.Card("3", "c")]
		self.assertTrue(handAnalyzer.highCard(hand1, hand2) == 2)
		
		hand1 = [card.Card("J", "h"), card.Card("K", "h"), card.Card("A", "h"), card.Card("5", "h"), card.Card("3", "c")]
		hand2 = [card.Card("J", "h"), card.Card("K", "h"), card.Card("A", "h"), card.Card("4", "h"), card.Card("3", "c")]
		self.assertTrue(handAnalyzer.highCard(hand1, hand2) == 1)
		
		hand1 = [card.Card("J", "h"), card.Card("K", "h"), card.Card("A", "h"), card.Card("4", "h"), card.Card("3", "c")]
		hand2 = [card.Card("J", "h"), card.Card("K", "h"), card.Card("A", "h"), card.Card("5", "h"), card.Card("3", "c")]
		self.assertTrue(handAnalyzer.highCard(hand1, hand2) == 2)
		
		hand1 = [card.Card("J", "h"), card.Card("K", "h"), card.Card("A", "h"), card.Card("4", "h"), card.Card("3", "c")]
		hand2 = [card.Card("T", "h"), card.Card("K", "h"), card.Card("A", "h"), card.Card("4", "h"), card.Card("3", "c")]
		self.assertTrue(handAnalyzer.highCard(hand1, hand2) == 1)
		
		hand1 = [card.Card("T", "h"), card.Card("K", "h"), card.Card("A", "h"), card.Card("4", "h"), card.Card("3", "c")]
		hand2 = [card.Card("J", "h"), card.Card("K", "h"), card.Card("A", "h"), card.Card("4", "h"), card.Card("3", "c")]
		self.assertTrue(handAnalyzer.highCard(hand1, hand2) == 2)
		
		hand1 = [card.Card("J", "h"), card.Card("K", "h"), card.Card("A", "h"), card.Card("4", "h"), card.Card("3", "c")]
		hand2 = [card.Card("J", "h"), card.Card("Q", "h"), card.Card("A", "h"), card.Card("4", "h"), card.Card("3", "c")]
		self.assertTrue(handAnalyzer.highCard(hand1, hand2) == 1)
		
		hand1 = [card.Card("J", "h"), card.Card("Q", "h"), card.Card("A", "h"), card.Card("4", "h"), card.Card("3", "c")]
		hand2 = [card.Card("J", "h"), card.Card("K", "h"), card.Card("A", "h"), card.Card("4", "h"), card.Card("3", "c")]
		self.assertTrue(handAnalyzer.highCard(hand1, hand2) == 2)
		
		hand1 = [card.Card("J", "h"), card.Card("Q", "h"), card.Card("A", "h"), card.Card("4", "h"), card.Card("3", "c")]
		hand2 = [card.Card("J", "h"), card.Card("Q", "h"), card.Card("K", "h"), card.Card("4", "h"), card.Card("3", "c")]
		self.assertTrue(handAnalyzer.highCard(hand1, hand2) == 1)
		
		hand1 = [card.Card("J", "h"), card.Card("Q", "h"), card.Card("K", "h"), card.Card("4", "h"), card.Card("3", "c")]
		hand2 = [card.Card("J", "h"), card.Card("Q", "h"), card.Card("A", "h"), card.Card("4", "h"), card.Card("3", "c")]
		self.assertTrue(handAnalyzer.highCard(hand1, hand2) == 2)
		

class TestHandAnalyzer(unittest.TestCase):

	def testStraightFlush(self):
		#Test Straight Flush
		hand1 = [card.Card("A", "s"), card.Card("K", "s"), card.Card("Q", "s"), card.Card("J", "s"), card.Card("T", "s")]
		hand2 = [card.Card("A", "d"), card.Card("K", "d"), card.Card("Q", "d"), card.Card("J", "d"), card.Card("T", "d")]
		self.assertTrue(handAnalyzer.handAnalyzer(hand1, hand2) == 0)
		
		hand1 = [card.Card("9", "s"), card.Card("K", "s"), card.Card("Q", "s"), card.Card("J", "s"), card.Card("T", "s")]
		hand2 = [card.Card("A", "d"), card.Card("K", "d"), card.Card("Q", "d"), card.Card("J", "d"), card.Card("T", "d")]
		self.assertTrue(handAnalyzer.handAnalyzer(hand1, hand2) == 2)
		
		hand1 = [card.Card("A", "s"), card.Card("K", "s"), card.Card("Q", "s"), card.Card("J", "s"), card.Card("T", "s")]
		hand2 = [card.Card("9", "d"), card.Card("K", "d"), card.Card("Q", "d"), card.Card("J", "d"), card.Card("T", "d")]
		self.assertTrue(handAnalyzer.handAnalyzer(hand1, hand2) == 1)
	
	def testQuads(self):	
		#Test Quads vs Quads
		hand1 = [card.Card("T", "d"), card.Card("T", "s"), card.Card("T", "s"), card.Card("J", "s"), card.Card("T", "s")]
		hand2 = [card.Card("7", "s"), card.Card("7", "s"), card.Card("7", "s"), card.Card("7", "s"), card.Card("9", "d")]
		self.assertTrue(handAnalyzer.handAnalyzer(hand1, hand2) == 1)
	
		hand1 = [card.Card("T", "d"), card.Card("T", "s"), card.Card("T", "s"), card.Card("J", "s"), card.Card("T", "s")]
		hand2 = [card.Card("T", "s"), card.Card("T", "d"), card.Card("T", "s"), card.Card("J", "s"), card.Card("T", "d")]
		self.assertTrue(handAnalyzer.handAnalyzer(hand1, hand2) == 0)
		
		hand1 = [card.Card("T", "d"), card.Card("T", "s"), card.Card("T", "s"), card.Card("J", "s"), card.Card("T", "s")]
		hand2 = [card.Card("Q", "h"), card.Card("Q", "c"), card.Card("Q", "s"), card.Card("J", "d"), card.Card("Q", "d")]
		self.assertTrue(handAnalyzer.handAnalyzer(hand1, hand2) == 2)
		
		#Test Quads vs SF
		hand1 = [card.Card("A", "s"), card.Card("K", "s"), card.Card("Q", "s"), card.Card("J", "s"), card.Card("T", "s")]
		hand2 = [card.Card("Q", "h"), card.Card("Q", "c"), card.Card("Q", "s"), card.Card("J", "d"), card.Card("Q", "d")]
		self.assertTrue(handAnalyzer.handAnalyzer(hand1, hand2) == 1)
		
		hand1 = [card.Card("Q", "h"), card.Card("Q", "c"), card.Card("Q", "s"), card.Card("J", "d"), card.Card("Q", "d")]
		hand2 = [card.Card("A", "s"), card.Card("K", "s"), card.Card("Q", "s"), card.Card("J", "s"), card.Card("T", "s")]
		self.assertTrue(handAnalyzer.handAnalyzer(hand1, hand2) == 2)
		
	def testFullHouse(self):
		#Test FH vs FH
		hand1 = [card.Card("A", "h"), card.Card("A", "c"), card.Card("Q", "s"), card.Card("A", "d"), card.Card("Q", "d")]
		hand2 = [card.Card("A", "s"), card.Card("A", "s"), card.Card("Q", "s"), card.Card("A", "s"), card.Card("Q", "s")]
		self.assertTrue(handAnalyzer.handAnalyzer(hand1, hand2) == 0)
		
		hand1 = [card.Card("A", "h"), card.Card("A", "c"), card.Card("K", "s"), card.Card("A", "d"), card.Card("K", "d")]
		hand2 = [card.Card("A", "s"), card.Card("A", "s"), card.Card("Q", "s"), card.Card("A", "s"), card.Card("Q", "s")]
		self.assertTrue(handAnalyzer.handAnalyzer(hand1, hand2) == 1)
		
		hand1 = [card.Card("A", "h"), card.Card("A", "c"), card.Card("Q", "s"), card.Card("A", "d"), card.Card("Q", "d")]
		hand2 = [card.Card("A", "s"), card.Card("A", "s"), card.Card("K", "s"), card.Card("A", "s"), card.Card("K", "s")]
		self.assertTrue(handAnalyzer.handAnalyzer(hand1, hand2) == 2)
		
		hand1 = [card.Card("A", "h"), card.Card("A", "c"), card.Card("A", "s"), card.Card("K", "d"), card.Card("K", "d")]
		hand2 = [card.Card("K", "s"), card.Card("K", "s"), card.Card("K", "s"), card.Card("A", "s"), card.Card("A", "s")]
		self.assertTrue(handAnalyzer.handAnalyzer(hand1, hand2) == 1)
		
		hand1 = [card.Card("A", "h"), card.Card("A", "c"), card.Card("Q", "s"), card.Card("A", "d"), card.Card("Q", "d")]
		hand2 = [card.Card("A", "s"), card.Card("A", "s"), card.Card("K", "s"), card.Card("A", "s"), card.Card("K", "s")]
		self.assertTrue(handAnalyzer.handAnalyzer(hand1, hand2) == 2)
		
		#Test versus quads
		hand1 = [card.Card("A", "h"), card.Card("A", "c"), card.Card("Q", "s"), card.Card("A", "d"), card.Card("Q", "d")]
		hand2 = [card.Card("T", "s"), card.Card("T", "d"), card.Card("T", "s"), card.Card("J", "s"), card.Card("T", "d")]
		self.assertTrue(handAnalyzer.handAnalyzer(hand1, hand2) == 2)
		
		hand1 = [card.Card("T", "s"), card.Card("T", "d"), card.Card("T", "s"), card.Card("J", "s"), card.Card("T", "d")]
		hand2 = [card.Card("A", "h"), card.Card("A", "c"), card.Card("Q", "s"), card.Card("A", "d"), card.Card("Q", "d")]
		self.assertTrue(handAnalyzer.handAnalyzer(hand1, hand2) == 1)
		
	def testFlush(self):
		#Test Flush v Flush
		hand1 = [card.Card("A", "h"), card.Card("K", "h"), card.Card("J", "h"), card.Card("T", "h"), card.Card("9", "h")]
		hand2 = [card.Card("A", "s"), card.Card("K", "s"), card.Card("J", "s"), card.Card("T", "s"), card.Card("9", "s")]
		self.assertTrue(handAnalyzer.handAnalyzer(hand1, hand2) == 0)
		
		hand1 = [card.Card("A", "h"), card.Card("K", "h"), card.Card("J", "h"), card.Card("T", "h"), card.Card("8", "h")]
		hand2 = [card.Card("A", "s"), card.Card("K", "s"), card.Card("J", "s"), card.Card("T", "s"), card.Card("9", "s")]
		self.assertTrue(handAnalyzer.handAnalyzer(hand1, hand2) == 2)
		
		hand1 = [card.Card("A", "h"), card.Card("K", "h"), card.Card("J", "h"), card.Card("T", "h"), card.Card("9", "h")]
		hand2 = [card.Card("A", "s"), card.Card("K", "s"), card.Card("J", "s"), card.Card("T", "s"), card.Card("8", "s")]
		self.assertTrue(handAnalyzer.handAnalyzer(hand1, hand2) == 1)
		
		hand1 = [card.Card("A", "h"), card.Card("K", "h"), card.Card("J", "h"), card.Card("7", "h"), card.Card("9", "h")]
		hand2 = [card.Card("A", "s"), card.Card("K", "s"), card.Card("J", "s"), card.Card("T", "s"), card.Card("9", "s")]
		self.assertTrue(handAnalyzer.handAnalyzer(hand1, hand2) == 2)
		
		hand1 = [card.Card("A", "h"), card.Card("K", "h"), card.Card("J", "h"), card.Card("T", "h"), card.Card("9", "h")]
		hand2 = [card.Card("A", "s"), card.Card("K", "s"), card.Card("J", "s"), card.Card("7", "s"), card.Card("9", "s")]
		self.assertTrue(handAnalyzer.handAnalyzer(hand1, hand2) == 1)
		
		hand1 = [card.Card("A", "h"), card.Card("K", "h"), card.Card("7", "h"), card.Card("T", "h"), card.Card("9", "h")]
		hand2 = [card.Card("A", "s"), card.Card("K", "s"), card.Card("J", "s"), card.Card("T", "s"), card.Card("9", "s")]
		self.assertTrue(handAnalyzer.handAnalyzer(hand1, hand2) == 2)
		
		hand1 = [card.Card("A", "h"), card.Card("K", "h"), card.Card("J", "h"), card.Card("T", "h"), card.Card("9", "h")]
		hand2 = [card.Card("A", "s"), card.Card("K", "s"), card.Card("7", "s"), card.Card("T", "s"), card.Card("9", "s")]
		self.assertTrue(handAnalyzer.handAnalyzer(hand1, hand2) == 1)
		
		hand1 = [card.Card("A", "h"), card.Card("7", "h"), card.Card("J", "h"), card.Card("T", "h"), card.Card("9", "h")]
		hand2 = [card.Card("A", "s"), card.Card("K", "s"), card.Card("J", "s"), card.Card("T", "s"), card.Card("9", "s")]
		self.assertTrue(handAnalyzer.handAnalyzer(hand1, hand2) == 2)
		
		hand1 = [card.Card("A", "h"), card.Card("K", "h"), card.Card("J", "h"), card.Card("T", "h"), card.Card("9", "h")]
		hand2 = [card.Card("A", "s"), card.Card("7", "s"), card.Card("J", "s"), card.Card("T", "s"), card.Card("9", "s")]
		self.assertTrue(handAnalyzer.handAnalyzer(hand1, hand2) == 1)
		
		hand1 = [card.Card("7", "h"), card.Card("K", "h"), card.Card("J", "h"), card.Card("T", "h"), card.Card("9", "h")]
		hand2 = [card.Card("A", "s"), card.Card("K", "s"), card.Card("J", "s"), card.Card("T", "s"), card.Card("9", "s")]
		self.assertTrue(handAnalyzer.handAnalyzer(hand1, hand2) == 2)
		
		hand1 = [card.Card("A", "h"), card.Card("K", "h"), card.Card("J", "h"), card.Card("T", "h"), card.Card("9", "h")]
		hand2 = [card.Card("7", "s"), card.Card("K", "s"), card.Card("J", "s"), card.Card("T", "s"), card.Card("9", "s")]
		self.assertTrue(handAnalyzer.handAnalyzer(hand1, hand2) == 1)
		
		#Flush v FH
		hand1 = [card.Card("A", "h"), card.Card("K", "h"), card.Card("J", "h"), card.Card("T", "h"), card.Card("9", "h")]
		hand2 = [card.Card("A", "h"), card.Card("A", "c"), card.Card("Q", "s"), card.Card("A", "d"), card.Card("Q", "d")]
		self.assertTrue(handAnalyzer.handAnalyzer(hand1, hand2) == 2)
		
		hand1 = [card.Card("A", "h"), card.Card("A", "c"), card.Card("Q", "s"), card.Card("A", "d"), card.Card("Q", "d")]
		hand2 = [card.Card("A", "h"), card.Card("K", "h"), card.Card("J", "h"), card.Card("T", "h"), card.Card("9", "h")]
		self.assertTrue(handAnalyzer.handAnalyzer(hand1, hand2) == 1)
		
		#Flush v SF
		hand1 = [card.Card("A", "h"), card.Card("K", "h"), card.Card("J", "h"), card.Card("T", "h"), card.Card("9", "h")]
		hand2 = [card.Card("A", "s"), card.Card("K", "s"), card.Card("Q", "s"), card.Card("J", "s"), card.Card("T", "s")]
		self.assertTrue(handAnalyzer.handAnalyzer(hand1, hand2) == 2)
		
		hand1 = [card.Card("A", "s"), card.Card("K", "s"), card.Card("Q", "s"), card.Card("J", "s"), card.Card("T", "s")]
		hand2 = [card.Card("A", "h"), card.Card("K", "h"), card.Card("J", "h"), card.Card("T", "h"), card.Card("9", "h")]
		self.assertTrue(handAnalyzer.handAnalyzer(hand1, hand2) == 1)
		
	def testStraight(self):
		hand1 = [card.Card("A", "h"), card.Card("K", "h"), card.Card("J", "h"), card.Card("T", "h"), card.Card("Q", "d")]
		hand2 = [card.Card("A", "h"), card.Card("K", "h"), card.Card("J", "h"), card.Card("T", "h"), card.Card("Q", "d")]
		self.assertTrue(handAnalyzer.handAnalyzer(hand1, hand2) == 0)
		
		hand1 = [card.Card("A", "h"), card.Card("K", "h"), card.Card("J", "h"), card.Card("T", "h"), card.Card("Q", "d")]
		hand2 = [card.Card("9", "h"), card.Card("K", "h"), card.Card("J", "h"), card.Card("T", "h"), card.Card("Q", "d")]
		self.assertTrue(handAnalyzer.handAnalyzer(hand1, hand2) == 1)
		
		hand1 = [card.Card("9", "h"), card.Card("K", "h"), card.Card("J", "h"), card.Card("T", "h"), card.Card("Q", "d")]
		hand2 = [card.Card("A", "h"), card.Card("K", "h"), card.Card("J", "h"), card.Card("T", "h"), card.Card("Q", "d")]
		self.assertTrue(handAnalyzer.handAnalyzer(hand1, hand2) == 2)
		
		#Straight v Flush
		hand1 = [card.Card("9", "h"), card.Card("K", "h"), card.Card("J", "h"), card.Card("T", "h"), card.Card("Q", "d")]
		hand2 = [card.Card("A", "h"), card.Card("K", "h"), card.Card("J", "h"), card.Card("T", "h"), card.Card("9", "h")]
		self.assertTrue(handAnalyzer.handAnalyzer(hand1, hand2) == 2)
		
		hand1 = [card.Card("A", "h"), card.Card("K", "h"), card.Card("J", "h"), card.Card("T", "h"), card.Card("9", "h")]
		hand2 = [card.Card("9", "h"), card.Card("K", "h"), card.Card("J", "h"), card.Card("T", "h"), card.Card("Q", "d")]
		self.assertTrue(handAnalyzer.handAnalyzer(hand1, hand2) == 1)
		
		#Straight v SF
		hand1 = [card.Card("9", "h"), card.Card("K", "h"), card.Card("J", "h"), card.Card("T", "h"), card.Card("Q", "d")]
		hand2 = [card.Card("A", "s"), card.Card("K", "s"), card.Card("Q", "s"), card.Card("J", "s"), card.Card("T", "s")]
		self.assertTrue(handAnalyzer.handAnalyzer(hand1, hand2) == 2)
		
		hand1 = [card.Card("A", "s"), card.Card("K", "s"), card.Card("Q", "s"), card.Card("J", "s"), card.Card("T", "s")]
		hand2 = [card.Card("9", "h"), card.Card("K", "h"), card.Card("J", "h"), card.Card("T", "h"), card.Card("Q", "d")]
		self.assertTrue(handAnalyzer.handAnalyzer(hand1, hand2) == 1)
		
	def testTrips(self):
		#Test trips v trips
		hand1 = [card.Card("A", "s"), card.Card("A", "h"), card.Card("A", "c"), card.Card("J", "s"), card.Card("T", "s")]
		hand2 = [card.Card("A", "s"), card.Card("A", "h"), card.Card("A", "c"), card.Card("J", "s"), card.Card("T", "s")]
		self.assertTrue(handAnalyzer.handAnalyzer(hand1, hand2) == 0)
		
		hand1 = [card.Card("K", "s"), card.Card("K", "h"), card.Card("K", "c"), card.Card("J", "s"), card.Card("T", "s")]
		hand2 = [card.Card("A", "s"), card.Card("A", "h"), card.Card("A", "c"), card.Card("J", "s"), card.Card("T", "s")]
		self.assertTrue(handAnalyzer.handAnalyzer(hand1, hand2) == 2)
		
		hand1 = [card.Card("A", "s"), card.Card("A", "h"), card.Card("A", "c"), card.Card("J", "s"), card.Card("T", "s")]
		hand2 = [card.Card("K", "s"), card.Card("K", "h"), card.Card("K", "c"), card.Card("J", "s"), card.Card("T", "s")]
		self.assertTrue(handAnalyzer.handAnalyzer(hand1, hand2) == 1)
		
		hand1 = [card.Card("A", "s"), card.Card("A", "h"), card.Card("A", "c"), card.Card("J", "s"), card.Card("T", "s")]
		hand2 = [card.Card("A", "s"), card.Card("A", "h"), card.Card("A", "c"), card.Card("T", "s"), card.Card("7", "s")]
		self.assertTrue(handAnalyzer.handAnalyzer(hand1, hand2) == 1)
		
		hand1 = [card.Card("A", "s"), card.Card("A", "h"), card.Card("A", "c"), card.Card("T", "s"), card.Card("7", "s")]
		hand2 = [card.Card("A", "s"), card.Card("A", "h"), card.Card("A", "c"), card.Card("J", "s"), card.Card("T", "s")]
		self.assertTrue(handAnalyzer.handAnalyzer(hand1, hand2) == 2)
		
		hand1 = [card.Card("A", "s"), card.Card("A", "h"), card.Card("A", "c"), card.Card("J", "s"), card.Card("T", "s")]
		hand2 = [card.Card("A", "s"), card.Card("A", "h"), card.Card("A", "c"), card.Card("J", "s"), card.Card("9", "s")]
		self.assertTrue(handAnalyzer.handAnalyzer(hand1, hand2) == 1)
		
		hand1 = [card.Card("A", "s"), card.Card("A", "h"), card.Card("A", "c"), card.Card("J", "s"), card.Card("9", "s")]
		hand2 = [card.Card("A", "s"), card.Card("A", "h"), card.Card("A", "c"), card.Card("J", "s"), card.Card("T", "s")]
		self.assertTrue(handAnalyzer.handAnalyzer(hand1, hand2) == 2)
		
		# Test trips v straight
		hand1 = [card.Card("A", "s"), card.Card("A", "h"), card.Card("A", "c"), card.Card("J", "s"), card.Card("9", "s")]
		hand2 = [card.Card("9", "h"), card.Card("K", "h"), card.Card("J", "h"), card.Card("T", "h"), card.Card("Q", "d")]
		self.assertTrue(handAnalyzer.handAnalyzer(hand1, hand2) == 2)
		
		hand2 = [card.Card("A", "s"), card.Card("A", "h"), card.Card("A", "c"), card.Card("J", "s"), card.Card("9", "s")]
		hand1 = [card.Card("9", "h"), card.Card("K", "h"), card.Card("J", "h"), card.Card("T", "h"), card.Card("Q", "d")]
		self.assertTrue(handAnalyzer.handAnalyzer(hand1, hand2) == 1)
		
	def testTwoPair(self):
	
		#Test two pair vs two pair
		hand1 = [card.Card("A", "h"), card.Card("A", "c"), card.Card("K", "s"), card.Card("K", "d"), card.Card("Q", "d")]
		hand2 = [card.Card("A", "s"), card.Card("A", "s"), card.Card("K", "s"), card.Card("K", "s"), card.Card("Q", "d")]
		self.assertTrue(handAnalyzer.handAnalyzer(hand1, hand2) == 0)
		
		hand1 = [card.Card("A", "h"), card.Card("A", "c"), card.Card("K", "s"), card.Card("K", "d"), card.Card("Q", "d")]
		hand2 = [card.Card("A", "s"), card.Card("A", "s"), card.Card("Q", "s"), card.Card("K", "s"), card.Card("Q", "d")]
		self.assertTrue(handAnalyzer.handAnalyzer(hand1, hand2) == 1)
		
		hand1 = [card.Card("A", "h"), card.Card("A", "c"), card.Card("J", "s"), card.Card("J", "d"), card.Card("Q", "d")]
		hand2 = [card.Card("A", "s"), card.Card("A", "s"), card.Card("Q", "s"), card.Card("J", "s"), card.Card("Q", "d")]
		self.assertTrue(handAnalyzer.handAnalyzer(hand1, hand2) == 2)
		
		hand1 = [card.Card("A", "h"), card.Card("A", "c"), card.Card("Q", "s"), card.Card("Q", "d"), card.Card("J", "d")]
		hand2 = [card.Card("K", "s"), card.Card("K", "s"), card.Card("Q", "s"), card.Card("Q", "s"), card.Card("J", "d")]
		self.assertTrue(handAnalyzer.handAnalyzer(hand1, hand2) == 1)
		
		hand1 = [card.Card("K", "s"), card.Card("K", "s"), card.Card("Q", "s"), card.Card("Q", "s"), card.Card("J", "d")]
		hand2 = [card.Card("A", "s"), card.Card("A", "s"), card.Card("Q", "s"), card.Card("J", "s"), card.Card("Q", "d")]
		self.assertTrue(handAnalyzer.handAnalyzer(hand1, hand2) == 2)
		
		hand1 = [card.Card("A", "h"), card.Card("A", "c"), card.Card("T", "s"), card.Card("T", "d"), card.Card("J", "d")]
		hand2 = [card.Card("K", "s"), card.Card("K", "s"), card.Card("Q", "s"), card.Card("Q", "s"), card.Card("J", "d")]
		self.assertTrue(handAnalyzer.handAnalyzer(hand1, hand2) == 1)
		
		hand1 = [card.Card("K", "s"), card.Card("K", "s"), card.Card("Q", "s"), card.Card("Q", "s"), card.Card("J", "d")]
		hand2 = [card.Card("A", "s"), card.Card("A", "s"), card.Card("T", "s"), card.Card("T", "s"), card.Card("J", "d")]
		self.assertTrue(handAnalyzer.handAnalyzer(hand1, hand2) == 2)
		
		hand1 = [card.Card("A", "h"), card.Card("A", "c"), card.Card("Q", "s"), card.Card("Q", "d"), card.Card("J", "d")]
		hand2 = [card.Card("K", "s"), card.Card("K", "s"), card.Card("T", "s"), card.Card("T", "s"), card.Card("J", "d")]
		self.assertTrue(handAnalyzer.handAnalyzer(hand1, hand2) == 1)
		
		hand1 = [card.Card("K", "s"), card.Card("K", "s"), card.Card("T", "s"), card.Card("T", "s"), card.Card("J", "d")]
		hand2 = [card.Card("A", "s"), card.Card("A", "s"), card.Card("Q", "s"), card.Card("J", "s"), card.Card("Q", "d")]
		self.assertTrue(handAnalyzer.handAnalyzer(hand1, hand2) == 2)
		
		# test two pair vs trips
		hand1 = [card.Card("A", "s"), card.Card("A", "h"), card.Card("A", "c"), card.Card("J", "s"), card.Card("T", "s")]
		hand2 = [card.Card("A", "s"), card.Card("A", "h"), card.Card("J", "c"), card.Card("J", "s"), card.Card("T", "s")]
		self.assertTrue(handAnalyzer.handAnalyzer(hand1, hand2) == 1)
		
		hand2 = [card.Card("A", "s"), card.Card("A", "h"), card.Card("A", "c"), card.Card("J", "s"), card.Card("T", "s")]
		hand1 = [card.Card("A", "s"), card.Card("A", "h"), card.Card("J", "c"), card.Card("J", "s"), card.Card("T", "s")]
		self.assertTrue(handAnalyzer.handAnalyzer(hand1, hand2) == 2)
		
		#test two pair v two pair
		hand2 = [card.Card("7", "s"), card.Card("5", "s"), card.Card("K", "c"), card.Card("7", "d"), card.Card("5", "h")]
		hand1 = [card.Card("7", "s"), card.Card("6", "s"), card.Card("5", "s"), card.Card("7", "d"), card.Card("5", "h")]
		self.assertTrue(handAnalyzer.handAnalyzer(hand1, hand2) == 2)
		
	def testPair(self):
		hand1 = [card.Card("A", "s"), card.Card("A", "h"), card.Card("Q", "c"), card.Card("J", "s"), card.Card("T", "s")]
		hand2 = [card.Card("A", "s"), card.Card("A", "h"), card.Card("Q", "c"), card.Card("J", "s"), card.Card("T", "s")]
		self.assertTrue(handAnalyzer.handAnalyzer(hand1, hand2) == 0)
		
		hand1 = [card.Card("A", "s"), card.Card("A", "h"), card.Card("K", "c"), card.Card("J", "s"), card.Card("T", "s")]
		hand2 = [card.Card("A", "s"), card.Card("A", "h"), card.Card("Q", "c"), card.Card("J", "s"), card.Card("T", "s")]
		self.assertTrue(handAnalyzer.handAnalyzer(hand1, hand2) == 1)
		
		hand2 = [card.Card("A", "s"), card.Card("A", "h"), card.Card("K", "c"), card.Card("J", "s"), card.Card("T", "s")]
		hand1 = [card.Card("A", "s"), card.Card("A", "h"), card.Card("Q", "c"), card.Card("J", "s"), card.Card("T", "s")]
		self.assertTrue(handAnalyzer.handAnalyzer(hand1, hand2) == 2)
		
		hand1 = [card.Card("A", "s"), card.Card("A", "h"), card.Card("Q", "c"), card.Card("J", "s"), card.Card("T", "s")]
		hand2 = [card.Card("A", "s"), card.Card("A", "h"), card.Card("Q", "c"), card.Card("T", "s"), card.Card("9", "s")]
		self.assertTrue(handAnalyzer.handAnalyzer(hand1, hand2) == 1)
		
		hand2 = [card.Card("A", "s"), card.Card("A", "h"), card.Card("Q", "c"), card.Card("J", "s"), card.Card("T", "s")]
		hand1 = [card.Card("A", "s"), card.Card("A", "h"), card.Card("Q", "c"), card.Card("T", "s"), card.Card("9", "s")]
		self.assertTrue(handAnalyzer.handAnalyzer(hand1, hand2) == 2)
		
		hand1 = [card.Card("A", "s"), card.Card("A", "h"), card.Card("Q", "c"), card.Card("J", "s"), card.Card("T", "s")]
		hand2 = [card.Card("A", "s"), card.Card("A", "h"), card.Card("Q", "c"), card.Card("J", "s"), card.Card("9", "s")]
		self.assertTrue(handAnalyzer.handAnalyzer(hand1, hand2) == 1)
		
		hand1 = [card.Card("A", "s"), card.Card("A", "h"), card.Card("Q", "c"), card.Card("J", "s"), card.Card("9", "s")]
		hand2 = [card.Card("A", "s"), card.Card("A", "h"), card.Card("Q", "c"), card.Card("J", "s"), card.Card("T", "s")]
		self.assertTrue(handAnalyzer.handAnalyzer(hand1, hand2) == 2)
		
		hand1 = [card.Card("A", "s"), card.Card("A", "h"), card.Card("Q", "c"), card.Card("J", "s"), card.Card("T", "s")]
		hand2 = [card.Card("K", "s"), card.Card("K", "h"), card.Card("Q", "c"), card.Card("J", "s"), card.Card("9", "s")]
		self.assertTrue(handAnalyzer.handAnalyzer(hand1, hand2) == 1)
		
		hand2 = [card.Card("A", "s"), card.Card("A", "h"), card.Card("Q", "c"), card.Card("J", "s"), card.Card("T", "s")]
		hand1 = [card.Card("K", "s"), card.Card("K", "h"), card.Card("Q", "c"), card.Card("J", "s"), card.Card("9", "s")]
		self.assertTrue(handAnalyzer.handAnalyzer(hand1, hand2) == 2)
		
		#pair v 2p
		hand1 = [card.Card("K", "s"), card.Card("K", "h"), card.Card("J", "c"), card.Card("J", "s"), card.Card("T", "s")]
		hand2 = [card.Card("A", "s"), card.Card("A", "h"), card.Card("Q", "c"), card.Card("J", "s"), card.Card("T", "s")]
		self.assertTrue(handAnalyzer.handAnalyzer(hand1, hand2) == 1)
		
		hand2 = [card.Card("K", "s"), card.Card("K", "h"), card.Card("J", "c"), card.Card("J", "s"), card.Card("T", "s")]
		hand1 = [card.Card("A", "s"), card.Card("A", "h"), card.Card("Q", "c"), card.Card("J", "s"), card.Card("T", "s")]
		self.assertTrue(handAnalyzer.handAnalyzer(hand1, hand2) == 2)
		
	def testHighCard(self):
		#HS v HS is covered in TestRankFunctions.testHighCardFunction. Skipping for now
		#HC v pair
		
		hand1 = [card.Card("T", "s"), card.Card("A", "h"), card.Card("Q", "c"), card.Card("J", "s"), card.Card("T", "s")]
		hand2 = [card.Card("7", "s"), card.Card("A", "h"), card.Card("Q", "c"), card.Card("J", "s"), card.Card("T", "s")]
		self.assertTrue(handAnalyzer.handAnalyzer(hand1, hand2) == 1)
		
		hand2 = [card.Card("T", "s"), card.Card("A", "h"), card.Card("Q", "c"), card.Card("J", "s"), card.Card("T", "s")]
		hand1 = [card.Card("7", "s"), card.Card("A", "h"), card.Card("Q", "c"), card.Card("J", "s"), card.Card("T", "s")]
		self.assertTrue(handAnalyzer.handAnalyzer(hand1, hand2) == 2)
		
if __name__ == '__main__':
	unittest.main()