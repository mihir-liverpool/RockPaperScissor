import random
while True:
    moves = ['rock', 'paper', 'scissor']
    player_wins = ['paperrock', 'scissorpaper', 'rockscissor']
    player_move = input('please choose between rock paper or scissor: ')
    computer_move = random.choice(moves)
    if player_move not in moves:
        print('please choose an option between rock paper and scissor')
    elif computer_move == player_move:
        print ('your move was ', player_move)
        print ('computers move was', computer_move)
        print('That is a draw, please try again')
    elif player_move+computer_move in player_wins:
        print('your move was ', player_move)
        print('computers move was', computer_move)
        print('you win')
    else:
        print('your move was ', player_move)
        print('computers move was', computer_move)
        print('you lose')

