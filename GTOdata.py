import accuracy


poker_Hands = {}

cards = ['2','3','4','5','6','7','8','9','T','J','Q','K', 'A']
n = len(cards)

# pairs
for i in range(n):

    curr_hand = cards[i] + cards[i]
    #Pairs
        
    #5 and up will be 1
    if(i >= 3):
        poker_Hands[curr_hand] = 1
    else:
        poker_Hands[curr_hand] = 0



# suited hands
for i in range(1,n+1):
    for j in range(i,n+1):
        if(i == j): continue

        biggerCard, smallerCard = cards[i-1], cards[j-1]
        if(i < j):
            biggerCard, smallerCard = cards[j-1], cards[i-1]
        curr_hand = biggerCard + smallerCard + 's'
        
        # Ace + 3 and higher
        if(biggerCard == 'A' and smallerCard > '2'):
            poker_Hands[curr_hand] = 1
            
        # King + 6 and up
        elif(biggerCard == 'K' and smallerCard >= '6'):
            poker_Hands[curr_hand] = 1
            
        elif(biggerCard == 'Q' and smallerCard >= '9'):
            poker_Hands[curr_hand] = 1
        elif(biggerCard == 'J' and smallerCard >= '9'):
            poker_Hands[curr_hand] = 1
        elif(biggerCard == 'T' and smallerCard >= '9'):
            poker_Hands[curr_hand] = 1
        else:
            poker_Hands[curr_hand] = 0

# unsiuited hands
for i in range(1,n+1):
    for j in range(i,n+1):
        if(i == j): continue

        biggerCard, smallerCard = cards[i-1], cards[j-1]
        if(i < j):
            biggerCard, smallerCard = cards[j-1], cards[i-1]
        curr_hand = biggerCard + smallerCard + 'o'
        

        # Ace + 9 and higher
        if(biggerCard == 'A' and smallerCard > '9'):
            poker_Hands[curr_hand] = 1
            
        elif(biggerCard == 'K' and (smallerCard == 'Q' or smallerCard == 'J')):
            poker_Hands[curr_hand] = 1
            #print(curr_hand)
        else:
            poker_Hands[curr_hand] = 0

# UTG + 1
HJ_Poker_Hands = poker_Hands.copy()

# print(poker_Hands['KJo'])
accuracy.accuracy_of_model(poker_Hands, "UTG")




    


        

        
            

    
    