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

# mid position ideal results
mid_position_hands = {}

#pairs
for i in range(n):
    curr_hand = cards[i] + cards[i]
    
    # all pairs should be raised
    mid_position_hands[curr_hand] = 1

# suited hands
for i in range(1,n+1):
    for j in range(i,n+1):
        if(i == j): continue

        biggerCard, smallerCard = cards[i-1], cards[j-1]
        if(i < j):
            biggerCard, smallerCard = cards[j-1], cards[i-1]
        curr_hand = biggerCard + smallerCard + 's'
        
        # if Ace is in hand, raise
        if(biggerCard == 'A'):
            mid_position_hands[curr_hand] = 1
            
        # King + 4 or up raise
        elif(biggerCard == 'K' and smallerCard >= '4'):
            mid_position_hands[curr_hand] = 1
            
        # queen + 6 or up raise
        elif(biggerCard == 'Q' and smallerCard >= '6'):
            mid_position_hands[curr_hand] = 1
        
        # jack + 7 or up raise
        elif(biggerCard == 'J' and smallerCard >= '7'):
            mid_position_hands[curr_hand] = 1

        # ten + 7 or up raise
        elif(biggerCard == 'T' and smallerCard >= '7'):
            mid_position_hands[curr_hand] = 1

        # 9 + 7 or up raise
        elif(biggerCard == '9' and smallerCard >= '7'):
            mid_position_hands[curr_hand] = 1

        # 8 + 7 or up raise
        elif(biggerCard == '8' and smallerCard >= '6'):
            mid_position_hands[curr_hand] = 1

        # 7 + 6 or up raise
        elif(biggerCard == '7' and smallerCard >= '6'):
            mid_position_hands[curr_hand] = 1
        else:
            mid_position_hands[curr_hand] = 0
        
        
# unsuited hands
for i in range(1,n+1):
    for j in range(i,n+1):
        if(i == j): continue

        biggerCard, smallerCard = cards[i-1], cards[j-1]
        if(i < j):
            biggerCard, smallerCard = cards[j-1], cards[i-1]
        curr_hand = biggerCard + smallerCard + 'o'
        

        # Ace + 8 and higher, raise
        if(biggerCard == 'A' and smallerCard >= '8'):
            mid_position_hands[curr_hand] = 1
        
        # King + ten or higher, raise
        elif(biggerCard == 'K' and smallerCard > '9'):
            mid_position_hands[curr_hand] = 1
            
        # queen + ten or higher, raise
        elif(biggerCard == 'Q' and smallerCard > '9'):
            mid_position_hands[curr_hand] = 1

        # jack + ten or higher, raise
        elif(biggerCard == 'J' and smallerCard > '9'):
            mid_position_hands[curr_hand] = 1

        else:
            mid_position_hands[curr_hand] = 0
        
# Late position
late_position_hands = {}

#pairs
for i in range(n):
    curr_hand = cards[i] + cards[i]
    
    # all pairs should be raised
    late_position_hands[curr_hand] = 1

# suited hands
for i in range(1,n+1):
    for j in range(i,n+1):
        if(i == j): continue

        biggerCard, smallerCard = cards[i-1], cards[j-1]
        if(i < j):
            biggerCard, smallerCard = cards[j-1], cards[i-1]
        curr_hand = biggerCard + smallerCard + 's'
        
        # if Ace, king or queen is in hand, raise
        if(biggerCard in ['A', 'K', 'Q']): 
            late_position_hands[curr_hand] = 1
        
        # jack + 4 or up raise
        elif(biggerCard == 'J' and smallerCard >= '4'):
            late_position_hands[curr_hand] = 1

        # (10, 9,8,7) + 5 or up raise
        elif(biggerCard in ['T', '9', '8','7'] and smallerCard >= '5'):
            late_position_hands[curr_hand] = 1

        # (6,5) + 6 or up raise
        elif(biggerCard in ['6','5'] and smallerCard >= '4'):
            late_position_hands[curr_hand] = 1
        else:
            late_position_hands[curr_hand] = 0

# unsuited hands
for i in range(1,n+1):
    for j in range(i,n+1):
        if(i == j): continue

        biggerCard, smallerCard = cards[i-1], cards[j-1]
        if(i < j):
            biggerCard, smallerCard = cards[j-1], cards[i-1]
        curr_hand = biggerCard + smallerCard + 'o'
        

        # Ace + 4 and higher, raise
        if(biggerCard == 'A' and smallerCard >= '4'):
            late_position_hands[curr_hand] = 1
        
        # King,queen + 9 or higher, raise
        elif(biggerCard in ['K','Q'] and smallerCard >= '9'):
            late_position_hands[curr_hand] = 1

        # (ten, 9) + 8 or higher, raise
        elif(biggerCard in ['T','9'] and smallerCard >= '8'):
            late_position_hands[curr_hand] = 1

        #(8) + 7 or higher, raise
        elif(biggerCard == '8' and smallerCard >= '7'):
            late_position_hands[curr_hand] = 1
        else:
            late_position_hands[curr_hand] = 0
        
        # Use this to test if the GTO data is correct
        # if(late_position_hands[curr_hand] == 1 and biggerCard == 'J'):
        #     print(curr_hand)


# print(poker_Hands['KJo'])
accuracy.accuracy_of_model(poker_Hands, "UTG")
accuracy.accuracy_of_model(mid_position_hands, "UTG+1")
accuracy.accuracy_of_model(late_position_hands, "UTG+3")




    


        

        
            

    
    