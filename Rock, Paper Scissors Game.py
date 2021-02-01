import random

def user_input():
    player="blank"
    while not( player.lower() == "r" or player.lower() == "p" or player.lower() == "s"):
        player = input("Enter the R | P | S : ")
    return player.lower()

def bot_choice():
    list = ['r','p','s']
    bot=random.choice(list)
    print('Bot choice is : ',bot)
    return bot

def check_winner(player,bot):
    if player=='r' and bot=='p':
        return "bot"
    elif player=='r' and bot=='s':
        return 'player'
    elif player=='p' and bot=='r':
        return "player"
    elif player=='p' and bot=='s':
        return 'bot'
    elif player=='s' and bot=='p':
        return 'player'
    elif player=='s' and bot=='r':
        return 'bot'
    else:
        return 'draw'

def rock_paper_scissors():

    print('<---WELCOME TO THE ROCK-PAPER-SCISSOR GAME--->')
    player_point=0
    bot_point=0
    end_the_game='n'

    while end_the_game.lower() != 'y':
        ply=user_input()
        bt=bot_choice()
        winner=check_winner(player=ply,bot=bt)
        print('Winner is \'',winner.capitalize(),'\'')
        print(' ')
        if winner == 'player':
            player_point+=2
        elif winner == 'bot':
            bot_point+=2
        else:
            player_point+=1
            bot_point+=1

        print('<---Score Board--->')
        print('Player Points : ',player_point)
        print('Bot Points : ',bot_point)
        print(' ')
        end_the_game=input('You want to end Y/N : ')

rock_paper_scissors()