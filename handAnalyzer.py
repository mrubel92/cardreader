import card

'''handAnalyzer method takes in 2 arrays of 5 cards (deck.Card) and returns an integer, 
1 meaning 1st entered hand is better, 2 meaning 2nd entered hand is better, 0 means they chop'''
def handAnalyzer(firstHand, secondHand):
	firstHandKicker = 0
	secondHandKicker = 0
	
	#straight flush
	if flush(firstHand) and straight(firstHand) and not(flush(secondHand) and straight(secondHand)):
		return 1
	if flush(secondHand) and straight(secondHand) and not(flush(firstHand) and straight(firstHand)):
		return 2
	if flush(secondHand) and straight(secondHand) and flush(firstHand) and straight(firstHand):
		return highCard(firstHand, secondHand)
		
		'''######################################################################################'''
	
	#quads	
	if quads(firstHand) != 0 and quads(secondHand) == 0:
		return 1
	if quads(secondHand) != 0 and quads(firstHand) == 0:
		return 2
	if quads(firstHand) != 0 and quads(secondHand) != 0:
		if quads(firstHand) > quads(secondHand):
			return 1
		if quads(firstHand) < quads(secondHand):	
			return 2
		
		#kicker logic todo: potentiall move logic to quad function?
		for c in range(0, len(firstHand)):
			if rank(firstHand[c].getRank()) != quads(firstHand):
				firstHandKicker = rank(firstHand[c].getRank())
		for c in range(0, len(secondHand)):
			if rank(secondHand[c].getRank()) != quads(secondHand):
				secondHandKicker = rank(secondHand[c].getRank())
		if firstHandKicker > secondHandKicker:
			return 1
		if secondHandKicker > firstHandKicker:
			return 2
		return 0
	
	'''######################################################################################'''
	
	#full house
	hand1return = fullHouse(firstHand)
	hand2return = fullHouse(secondHand)
	
	if hand1return[0] !=0 and hand2return[0] == 0:
		return 1
		
	if hand2return[0] !=0 and hand1return[0] == 0:
		return 2
		
	if hand1return[0] !=0 and hand2return[0] != 0:
		if hand1return[0] > hand2return[0]:
			return 1
		if hand2return[0] > hand1return[0]:
			return 2
		if hand1return[1] > hand2return[1]:
			return 1
		if hand2return[1] > hand1return[1]:
			return 2
			
		return 0
	'''######################################################################################'''
	
	#flush
	if flush(firstHand) and not flush(secondHand):
		return 1
	if flush(secondHand) and not flush(firstHand):
		return 2
	if flush(firstHand) and flush(secondHand):
		return highCard(firstHand, secondHand)
	
	'''######################################################################################'''
	
	#straight
	if straight(firstHand) and not straight(secondHand):
		return 1
	if straight(secondHand) and not straight(firstHand):
		return 2
	if straight(firstHand) and straight(secondHand):
		return highCard(firstHand, secondHand)	
	
	'''######################################################################################'''
	
	#threeofakind
	hand1return = trips(firstHand)
	hand2return = trips(secondHand)
	
	if hand1return[0] !=0 and hand2return[0] == 0:
		return 1
		
	if hand2return[0] !=0 and hand1return[0] == 0:
		return 2
	
	if hand1return[0] !=0 and hand2return[0] != 0:
		if hand1return[0] > hand2return[0]:
			return 1
		if hand2return[0] > hand1return[0]:
			return 2
		if hand1return[1] > hand2return[1]:
			return 1
		if hand2return[1] > hand1return[1]:
			return 2
		if hand1return[2] > hand2return[2]:
			return 1
		if hand2return[2] > hand1return[2]:
			return 2
			
		return 0
	
	
	'''######################################################################################'''
	
	#twopair
	hand1return = twoPair(firstHand)
	hand2return = twoPair(secondHand)
	
	if hand1return[0] !=0 and hand2return[0] == 0:
		return 1
		
	if hand2return[0] !=0 and hand1return[0] == 0:
		return 2
	
	if hand1return[0] !=0 and hand2return[0] != 0:
		if hand1return[0] > hand2return[0]:
			return 1
		if hand2return[0] > hand1return[0]:
			return 2
		if hand1return[1] > hand2return[1]:
			return 1
		if hand2return[1] > hand1return[1]:
			return 2
		if hand1return[2] > hand2return[2]:
			return 1
		if hand2return[2] > hand1return[2]:
			return 2
			
		return 0
	
	'''######################################################################################'''
	
	#pair
	hand1return = pair(firstHand)
	hand2return = pair(secondHand)
	
	if hand1return[0] !=0 and hand2return[0] == 0:
		return 1
		
	if hand2return[0] !=0 and hand1return[0] == 0:
		return 2
	
	if hand1return[0] !=0 and hand2return[0] != 0:
		if hand1return[0] > hand2return[0]:
			return 1
		if hand2return[0] > hand1return[0]:
			return 2
		if hand1return[1] > hand2return[1]:
			return 1
		if hand2return[1] > hand1return[1]:
			return 2
		if hand1return[2] > hand2return[2]:
			return 1
		if hand2return[2] > hand1return[2]:
			return 2
		if hand1return[3] > hand2return[3]:
			return 1
		if hand2return[3] > hand1return[3]:
			return 2
			
		return 0
	
	'''######################################################################################'''
	
	#high card
	return highCard(firstHand, secondHand)
	

#return True if cards comprise flush, False if not	
def flush(cardArray):
	for c in range(0, len(cardArray) - 1):
		if cardArray[c].getSuit() != cardArray[c + 1].getSuit():
			return False
	
	return True
	
#return True if cards comprise straight, False if not
def straight(cardArray):
	lowCard = 0
	nextCardFound = False

	for c in range(0, len(cardArray)):
		if lowCard == 0:
			lowCard = rank(cardArray[c].getRank())
		elif rank(cardArray[c].getRank()) < lowCard:
			lowCard = rank(cardArray[c].getRank())
	
	#look for second card
	for c in range(0, len(cardArray)):
		if rank(cardArray[c].getRank()) == (lowCard + 1):
			nextCardFound = True
	if nextCardFound == False:
		return False
	
	nextCardFound = False
	
	#look for third card
	for c in range(0, len(cardArray)):
		if rank(cardArray[c].getRank()) == lowCard + 2:
			nextCardFound = True
	if nextCardFound == False:
		return False
	
	nextCardFound = False
	
	#look for third card
	for c in range(0, len(cardArray)):
		if rank(cardArray[c].getRank()) == lowCard + 3:
			nextCardFound = True
	if nextCardFound == False:
		return False
	
	nextCardFound = False
	
	#look for third card
	for c in range(0, len(cardArray)):
		if rank(cardArray[c].getRank()) == lowCard + 4:
			nextCardFound = True
	if nextCardFound == False:
		return False

		
	return True

#returns 1 if first hand is highest, 2 if second is fhighest, 0 if equal
def highCard(firstHand, secondHand):
	ahighest = 0
	asecond = 0
	athird = 0
	afourth = 0
	afifth = 0
	
	bhighest = 0
	bsecond = 0
	bthird = 0
	bfourth = 0
	bfifth = 0
	
	for a in range(0, len(firstHand)):
		if rank(firstHand[a].getRank()) > ahighest:
			afifth = afourth
			afourth = athird
			athird = asecond
			asecond = ahighest
			ahighest = rank(firstHand[a].getRank())
		elif rank(firstHand[a].getRank()) > asecond:
			afifth = afourth
			afourth = athird
			athird = asecond
			asecond = rank(firstHand[a].getRank())
		elif rank(firstHand[a].getRank()) > athird:
			afifth = afourth
			afourth = athird
			athird = rank(firstHand[a].getRank())
		elif rank(firstHand[a].getRank()) > afourth:
			afifth = afourth
			afourth = rank(firstHand[a].getRank())
		else:
			afifth = rank(firstHand[a].getRank())
			
	for b in range(0, len(secondHand)):
		if rank(secondHand[b].getRank()) > bhighest:
			bfifth = bfourth
			bfourth = bthird
			bthird = bsecond
			bsecond = bhighest
			bhighest = rank(secondHand[b].getRank())
		elif rank(secondHand[b].getRank()) > bsecond:
			bfifth = bfourth
			bfourth = bthird
			bthird = bsecond
			bsecond = rank(secondHand[b].getRank())
		elif rank(secondHand[b].getRank()) > bthird:
			bfifth = bfourth
			bfourth = bthird
			bthird = rank(secondHand[b].getRank())
		elif rank(secondHand[b].getRank()) > bfourth:
			bfifth = bfourth
			bfourth = rank(secondHand[b].getRank())
		else:
			bfifth = rank(secondHand[b].getRank())
			
	#print(str(ahighest) + "||" + str(asecond) + "||" + str(athird) + "||" + str(afourth) + "||" + str(afifth) + "||")
			
	if ahighest > bhighest:
		return 1
	
	if bhighest > ahighest:
		return 2
		
	if asecond > bsecond:
		return 1
	
	if asecond < bsecond:
		return 2
		
	if athird > bthird:
		return 1
		
	if bthird > athird:
		return 2
		
	if afourth > bfourth:
		return 1
		
	if bfourth > afourth:
		return 2
		
	if afifth > bfifth:
		return 1
		
	if bfifth > afifth:
		return 2
		
	return 0

#returns [rank of pair, kicker1, kicker2, kicker3], [0, 0, 0, 0] if no pair	
def pair(cardArray):
	pairrank = 0
	kicker1 = 0
	kicker2 = 0
	kicker3 = 0
	index1 = 0
	index2 = 0
	for a in range(0, len(cardArray) - 1):
		for b in range(a + 1, len(cardArray)):
			if cardArray[a].getRank() == cardArray[b].getRank():
				pairrank = rank(cardArray[a].getRank())
				index1 = a
				index2 = b
				
	if pairrank == 0:
		return [0, 0, 0, 0]
	
	for a in range(0, len(cardArray)):
		if a != index1 and a != index2:
			if rank(cardArray[a].getRank()) > kicker1:
				kicker3 = kicker2
				kicker2 = kicker1
				kicker1 = rank(cardArray[a].getRank())
			elif rank(cardArray[a].getRank()) > kicker2:
				kicker3 = kicker2
				kicker2 = rank(cardArray[a].getRank())
			else:
				kicker3 = rank(cardArray[a].getRank())
	
	return [pairrank, kicker1, kicker2, kicker3]
	
#returns [rank of trips, first kicker, second kicker] [0, 0, 0] if no trips
def trips(cardArray):
	used = []
	used.append(False)
	used.append(False)
	used.append(False)
	used.append(False)
	used.append(False)
	triprank = 0
	kicker1 = 0
	kicker2 = 0
	
	for a in range(0, len(cardArray) - 2):
		for b in range(a + 1, len(cardArray) - 1):
			if rank(cardArray[a].getRank()) == rank(cardArray[b].getRank()) and used[a] == False and used[b] == False:
				for c in range(b + 1, len(cardArray)):
					if rank(cardArray[a].getRank()) == rank(cardArray[c].getRank()) and used[c] == False:
						triprank = rank(cardArray[a].getRank())
						used[a] = True
						used[b] = True
						used[c] = True
					
	for a in range(0, len(cardArray)):
		if used[a] == False:
			if kicker1 == 0:
				kicker1 = rank(cardArray[a].getRank())
			else:
				kicker2 = rank(cardArray[a].getRank())
			
	if triprank == 0:
		return [0, 0, 0]
		
	if kicker1 > kicker2:
		return[triprank, kicker1, kicker2]
	
	return[triprank, kicker2, kicker1]
	
#if four of a kind, return numeric rank, else return 0
def quads(cardArray):
	card1rank = rank(cardArray[0].getRank())
	card2rank = rank(cardArray[1].getRank())
	card3rank = rank(cardArray[2].getRank())
	card4rank = rank(cardArray[3].getRank())
	card5rank = rank(cardArray[4].getRank())
	
	if card1rank == card2rank:
		if card2rank != card3rank:
			if card2rank == card4rank and card2rank == card5rank:
				return card1rank
			else:
				return 0
		else:
			if card3rank == card4rank or card3rank == card5rank:
				return card1rank
			else:
				return 0
	else:
		if card1rank == card3rank and card1rank == card4rank and card1rank == card5rank:
			return card1rank
		if card2rank == card3rank and card2rank == card4rank and card2rank == card5rank:
			return card2rank
		else:
			return 0
			
	return 0

#this function will return a two integer array [triprank, pairrank], [0, 0] when not FH
def fullHouse(cardArray):
	used = []
	used.append(False)
	used.append(False)
	used.append(False)
	used.append(False)
	used.append(False)
	
	triprank = 0
	pairrank = 0
	
	for a in range(0, len(cardArray) - 2):
		for b in range (a + 1, len(cardArray) - 1):
			if rank(cardArray[a].getRank()) == rank(cardArray[b].getRank()) and used[a] == False and used[b] == False and a < b:
				for c in range(b + 1, len(cardArray)):
					if rank(cardArray[a].getRank()) == rank(cardArray[c].getRank()) and b < c:
						triprank = rank(cardArray[a].getRank())
						used[a] = True
						used[b] = True
						used[c] = True
						#print(triprank)
						
	if triprank == 0:
		return [0, 0]
	else:
		for a in range(0, len(cardArray) - 1):
			if used[a] == False:
				for b in range(a + 1, len(cardArray)):
					if used[b] == False:
						if rank(cardArray[a].getRank()) == rank(cardArray[b].getRank()):
							pairrank = rank(cardArray[a].getRank())
							used[a] = True
							used[b] = True

							
	if pairrank == 0:
		return [0, 0]
	
	return [triprank, pairrank]
	
#this function will return [toprank, bottomrank, kickerrank] or [0, 0, 0] if no 2p
def twoPair(cardArray):
	used = []
	used.append(False)
	used.append(False)
	used.append(False)
	used.append(False)
	used.append(False)
	
	pair1 = 0
	pair2 = 0
	kicker = 0
	
	for x in range(0, 2):
		a = 0
		b = 0
		for a in range(0, len(cardArray) - 1):
			for b in range(a + 1, len(cardArray)):
				#print(str(a) + str(b) + str(x))
				if cardArray[a].getRank() == cardArray[b].getRank():
					if pair1 == 0:
						pair1 = rank(cardArray[a].getRank())
						used[a] = True
						used[b] = True
					elif pair1 != rank(cardArray[a].getRank()):
						pair2 = rank(cardArray[a].getRank())
						used[a] = True
						used[b] = True
					
	if pair1 == 0 or pair2 == 0:
		return [0, 0, 0]
		
	for a in range(0, len(cardArray)):
		if used[a] == False:
			kicker = rank(cardArray[a].getRank())
	
	return [pair1, pair2, kicker]

#this function converts the card rank to a numeric comparable value per poker rules
def rank(cardRank):
	rank = 0
	if cardRank == "T":
		rank = 9
	elif cardRank == "J":
		rank = 10
	elif cardRank == "Q":
		rank = 11
	elif cardRank == "K":
		rank = 12
	elif cardRank == "A":
		rank = 13
	else:
		rank = int(cardRank) - 1
		
	return rank