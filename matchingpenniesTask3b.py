#!/usr/bin/env python

# A simple game to calculate payoffs for 2 players
# in an "almost inifite setting of matching pennies

from random import random

def play_game(penny1, penny2):

    # the first moves for player 1 and player 2 are defined
    # for all starting pairs
    p1_start = penny1
    p2_start = penny2

    # initialise the counts for heads 
    # and tails for player 1 and 2 to zero
    heads_count_1 = 0
    tails_count_1 = 0
    heads_count_2 = 0
    tails_count_2 = 0

    # define heads as a number bigger or equal to 0.5 
    # and tails as a number smaller than 0.5
    # and increment respective counter
    if p1_start >= 0.5:
        heads_count_1 += 1
    elif p1_start < 0.5:
        tails_count_1 += 1
    if p2_start >= 0.5:
        heads_count_2 += 1
    elif p2_start < 0.5:
        tails_count_2 += 1


    # choose a high enough number for the number of rounds
    # so it converges towards 1/2
    for i in range(100000):
        
        # update the statistics of the heads played so far
	# as a ratio of heads to total
        # number of rounds for each player

        player_1_stats_h = heads_count_1/(heads_count_1+tails_count_1)
        # player_1_stats_t is just (1 - player_1_stats_h)
        player_2_stats_h = heads_count_2/(heads_count_2+tails_count_2)
        # player_2_stats_t is just (1 - player_2_stats_h)

        # compares the counts of player 1 so far and defines 
        # the best response for player 2
        if (player_1_stats_h > 0.5): 
            # player 2 plays tails
            tails_count_2 += 1
        elif (player_1_stats_h < 0.5):
            # player 2 plays heads
            heads_count_2 += 1
        else:
            if (random() >= 0.5):
                heads_count_2 +=1
            else:
                tails_count_2 +=1

        # compares the counts of player 2 so far and defines
        # the best response for player 1
        if (player_2_stats_h > 0.5):
            # player 1 plays heads
            heads_count_1 += 1
        elif (player_2_stats_h < 0.5):
            # player 1 plays tails
            tails_count_1 += 1
        else: 
            if random() >= 0.5:
                heads_count_1 +=1
            else:
                tails_count_1 +=1
    
    
    print("Player 1's statistical mixed strategy is: {}, {}"
	.format(player_1_stats_h, 1-player_1_stats_h))
    print("Player 2's statistical mixed strategy is: {}, {}"
	.format(player_2_stats_h, 1-player_2_stats_h))

def main():
    print("With starting strategy (Heads, Heads): ")
    play_game(1,1) # heads & heads starting strategy
    print("With starting strategy (Heads, Tails): ")
    play_game(1,0) # heads & tails starting strategy
    print("With starting strategy (Tails, Heads): ")
    play_game(0,1) # tails & heads starting strategy
    print("With starting strategy (Tails, Tails): ")
    play_game(0,0) # tails & tails starting strategy


if __name__ == '__main__':
    main()
