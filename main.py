import os
import numpy as np
from matplotlib import pyplot as plt
from random import randint

USE_SOLVER = True

class Game:

    card_list = list()
    num_of_cards = 0
    rounds_played = 0
    score = np.zeros(2) # change it to card stacks
    idxHistory = list()
    continuePlaying = True

    def __init__(self):
        self.score = 26*np.ones(2).astype(np.int)
        self.rounds_played = 0
        self.card_list = generateCardList()
        self.num_of_cards = len(self.card_list)
        self.idxHistory = list()
        self.continuePlaying = True

    def displayCards(self):
        print('New round (Close window, if done)')
        fig, axs = plt.subplots(2, 2)
        axs = np.reshape(axs, (4, 1))
        for i in range(4):
            if len(self.idxHistory) == self.num_of_cards:
                self.idxHistory = list()
                print('Card deck is full: reshuffle')
            newCard = False
            while not newCard:
                idx = randint(0, self.num_of_cards-1)
                if idx not in self.idxHistory:
                    newCard = True
            self.idxHistory.append(idx)
            data_path = os.path.join('card_pictures',self.card_list[idx])
            img = plt.imread(data_path)
            axs[i][0].imshow(img)
            axs[i][0].axis('off')
        fig.suptitle('Cards played: '+str(len(self.idxHistory))+"/52\n Player 1: " + str(int(self.score[0])) + ", Player 2: "+ str(int(self.score[1])))
        plt.show()
        self.rounds_played += 1
    
    def addScore (self, winner):
        # winner 1 or 2
        idx_winner = winner-1
        if idx_winner == 0:
            self.score[int(idx_winner)] += 2
            self.score[int(idx_winner)+1] -= 2
        if idx_winner == 1:
            self.score[int(idx_winner)-1] -= 2    
            self.score[int(idx_winner)] += 2
    
    def checkFinished(self, userInput):
        if self.score[0] <= 0 or self.score[1] <= 0:
            print('Game is lost for one of the players!')
            self.continuePlaying = False
        if userInput == 'n':
            print('User quit game...')
            self.continuePlaying = False
    
    def plotFinalResult(self):
        x = [1, 2]
        fig, ax = plt.subplots()
        plt.bar(x, self.score)
        plt.xticks(x, ('Player 1', 'Player 2'))
        plt.title('Final Score\n' + 'Rounds played: ' + str(int(self.rounds_played)))
        plt.show()
        print('Thank you for playing!')
        print('Final Score:')
        print(self.score)


def generateCardList():
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
    return card_list



def main():
    game = Game()
    while game.continuePlaying:
        game.displayCards()
        print('Who won? (1 or 2 or 0 (nobody))')
        winner = int(input())
        game.addScore(winner)
        print('You wanna keep playing? (y: yes, n: no)')
        userInput = input()
        game.checkFinished(userInput) #TODO: separate lost case 
    game.plotFinalResult()

main()