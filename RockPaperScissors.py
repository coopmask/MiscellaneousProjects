import random

print()

#explain the rules of the game
print('The rules of rock, paper, scissors are quite simple. Rock vs. paper results in a win for paper. \
Rock vs. scissors results in a win for rock. Scissors vs. paper results in a win for scissors. Let\'s begin!')

#enter the game loop, ask the player for their choice, get the computer's choice, and check who won
game_choices = ['rock', 'paper', 'scissors']

while True:

    print()

    first_choice = input('Choose rock, paper, or scissors: ')

    while first_choice not in game_choices:
        first_choice = input('Enter a valid choice: ').lower()

    print()

    print(f'Your choice is {first_choice}. Now the computer will choose...')

    print()

    computer_choice = random.choice(game_choices)
    print(f'The computer has chosen {computer_choice}.')

    if first_choice == 'rock' and computer_choice == 'paper' or first_choice == 'scissors' and computer_choice == 'rock' \
            or first_choice == 'paper' and computer_choice == 'scissors':

        print()

        print('The computer wins! Better luck next time!')

    elif first_choice == computer_choice:

        print()

        print('It\'s a tie!')

    else:

        print()

        print('Congratulations! You beat the computer!')

    print()

    #after the game is over, ask the user if they would like to play again
    replay = input('Would you like to play again? Y/N: ').upper()

    if replay == 'N':
        break

print('Thank your for playing rock, paper, scissors!')

