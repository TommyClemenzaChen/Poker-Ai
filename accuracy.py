import poker
def accuracy_of_model(poker_Hands, position):

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
        action = poker.get_action_from_input("test", card1, card2, suited, position, 100)[0]['player_states']['test']['action']
        
        if((action == 'RAISE' and poker_Hands[combos] == 1) or (action == 'FOLD' and poker_Hands[combos] == 0)):
            correct += 1
        else:
            print(f"Wrong: {combos} {action}")
        total += 1

    print(f"Accuracy: {correct * 100/total}%")  