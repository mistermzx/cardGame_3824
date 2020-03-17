import os
import numpy as np
from matplotlib import pyplot as plt
from random import randint

# Generate list of cards
card_list = list()
sign_list = ['clubs', 'diamonds', 'hearts', 'spades']
specialNumbers_list = ['jack', 'queen', 'king', 'ace']
for i in range(2, 15):
    for sign in sign_list:
        if i<11:
            card_list.append(str(i) + '_of_' + sign + '.png')
        elif i<14:
            card_list.append(specialNumbers_list[i-11] + '_of_' + sign + '2.png')
        else:
            card_list.append(specialNumbers_list[i-11] + '_of_' + sign + '.png')
num_of_cards = len(card_list)

idxHistory = list()
score = 26*np.ones(2).astype(np.float)

# Generate and plot random cards:
num_of_rounds = 0
continuePlaying = True
while continuePlaying:
    print('New round (Close window, if done)')
    fig, axs = plt.subplots(2, 2)
    axs = np.reshape(axs, (4, 1))
    for i in range(4):
        if len(idxHistory) == num_of_cards:
            idxHistory = list()
            print('Card deck is full: reshuffle')
        newCard = False
        while not newCard:
            idx = randint(0, num_of_cards-1)
            if idx not in idxHistory:
                newCard = True
        idxHistory.append(idx)
        data_path = os.path.join('card_pictures',card_list[idx])
        img = plt.imread(data_path)
        axs[i][0].imshow(img)
        #axs[i][0].set_title(i+1)
        axs[i][0].axis('off')
    fig.suptitle('Cards played: '+str(len(idxHistory))+"/52\n Player 1: " + str(int(score[0])) + ", Player 2: "+ str(int(score[1])))
    plt.show()
    # buzzer = input("Playing...")
    # plt.close()
    # if (buzzer == 'a'):
    #     print('Jenny pressed')
    # elif (buzzer == 'l'):
    #     print('Martin pressed')
    #print('Cards played: '+str(len(idxHistory))+"/52\n")
    print('Who won? (1 or 2 or 0 (nobody))')
    idx_score = int(input()) - 1
    if idx_score == 0:
        score[int(idx_score)] += 2
        score[int(idx_score)+1] -= 2
    if idx_score == 1:
        score[int(idx_score)-1] -= 2    
        score[int(idx_score)] += 2

    # if int(idx_score) in [1,2]:
    #     score[int(idx_score)-1] += 2
    #     score[int]
    # print('Current score: ')
    # print(score)
    num_of_rounds += 1
    if score[0]==0 or score[1]==0:
        print('Game is lost for one of the players!')
        break
    print('You wanna keep playing? (y: yes, n: no)')
    if input()=='n':
        continuePlaying = False

# Plot Final result
x = [1, 2]
fig, ax = plt.subplots()
plt.bar(x, score)
plt.xticks(x, ('Player 1', 'Player 2'))
plt.title('Final Score\n' + 'Rounds played: ' + str(int(num_of_rounds)))
plt.show()

print('Thank you for playing!')
print('Final Score:')
print(score)
