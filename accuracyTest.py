import poker


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
            #print(curr_hand)
        if(biggerCard == 'K' and (smallerCard == 'Q' or smallerCard == 'J')):
            poker_Hands[curr_hand] = 1
            #print(curr_hand)
        else:
            poker_Hands[curr_hand] = 0

# Testing accuaracy of the model
correct = 0
total = 0     

for combos in poker_Hands:
    card1 = combos[0]
    card2 = combos[1]

    if(card1 == 'T'): card1 = '10'
    if(card2 == 'T'): card2 = '10'

    suited = True
    if(len(combos) == 2 or combos[2] == 'o'):
        suited = False

    #Gets the action from the input
    action = poker.get_action_from_input("test", card1, card2, suited, "UTG", 100)[0]['player_states']['test']['action']
    
    if((action == 'RAISE' and poker_Hands[combos] == 1) or (action == 'FOLD' and poker_Hands[combos] == 0)):
        correct += 1
    else:
        print(f"Wrong: {combos} {action}")
    total += 1

print(f"Accuracy: {correct * 100/total}%")   
    


        

        
            

    
    