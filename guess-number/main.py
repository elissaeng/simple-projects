import random

# Practice using random.randint()

# GUESS THE NUMBER (COMPUTER)
# region ------------------------------------------------

# With paramater
# def guess_number(x):
#     random_number = random.randint(1, x)
#     guess = None
#     while guess != random_number:
#         guess = int(input(f'Guess a number between 1 and {x}: '))
#         if  guess < random_number:
#             print('Guess again, too low')
#         elif guess > random_number:
#             print('Guess again, too high')
#     print(f'Congrats! you guessed the right {random_number}!')

# guess_number(5)

# Without paramater
# def guess_number():
#     random_number = random.randint(1, 5)
#     guess = None
#     while guess != random_number:
#         guess = int(input(f'Give me a number between 1 and 5: '))
#         if guess > random_number:
#             print('Guess again, too high.')
#         elif guess < random_number:
#             print('Guess again, too low')
#     print('Congrats! You guessed correctly!')

# guess_number()

# endregion


# GUESS THE NUMBER (USER)
# region ------------------------------------------------
# def computer_guess(x):
#     low = 1
#     high = x
#     feedback = ''
#     while feedback != 'c':
#         if low != high:
#             guess = random.randint(low, high)
#         else:
#             guess = low
#         feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)? ').lower()
#         if feedback == 'h':
#             high = guess - 1
#         elif feedback == 'l':
#             low = guess + 1
#     print(f'Hooray! The computer guessed your number, {guess}, correctly!')

# computer_guess(10)

#endregion


# MYSTERY NUMBER CHALLENGE
# region ------------------------------------------------
def play_game(low, high, attempts):
    secret_number = random.randint(low, high)
    print(f'Guess a number between {low} and {high}. You have {attempts} attempts.\n')
    
    for attempt in range(attempts):
        guess = int(input('Enter your guess: '))
        if guess == secret_number:
            print('Congrats! You guessed correctly!')
            return
        elif guess < secret_number:
            print('Too low!')
        else:
            print('Too high!')

    print(f'Sorry, you ran out of attempts. The secret number was {secret_number}')

play_game(1, 15, 3)

#endregion


# Practice with conditionals:

# TEMPERATURE CHECKER
# region ------------------------------------------------

# Without a function
# get_temp = int(input(f'What is the temperature right now? '))
# if get_temp < 0:
#     print('Holy smokes it is freezing!')
# elif get_temp >= 0 and get_temp <= 10:
#     print('It is cold.')
# elif get_temp >= 11 and get_temp <= 20:
#     print('It is cool.')
# else: 
#     print('It is warm!')

# # With a function
# def temp():
#     get_temp = int(input(f'What is the temperature right now?'))
#     if get_temp < 0:
#         print('Holy smokes it is freezing!')
#     elif get_temp >= 0 and get_temp <= 10:
#         print('It is cold.')
#     elif get_temp >= 11 and get_temp <= 20:
#         print('It is cool.')
#     else: 
#         print('It is warm!')

# temp()

# # With a paramater/argument
# def temp(temperature):
#     if temperature <= 0:
#         print('Holy smokes it is freezing. Go inside you"ll get frostbite')
#     elif temperature >= 0 and temperature <= 10:
#         print('It is a little chilly.')
#     elif temperature >= 11 and temperature <= 20:
#         print('It is a wee bit chilly.')
#     else:
#         print('Hooray it is warm!')

# get_temp = int(input(f'What is the temperature right now? '))
# temp(get_temp)

# endregion


# NUMBER CHECKER
# region ------------------------------------------------
# def check_number(n):
#     if n > 0:
#         print('The number is positive.')
#     elif n < 0:
#         print('The number is negative.')
#     else:
#         print('The number is zero.')

# check_number(0)
# check_number(2)
# check_number(-1)

# endregion


# EVEN OR ODD
# region ------------------------------------------------
# def even_or_odd(n):
#     if n % 2 == 0:
#         print('The number is even.')
#     else:
#         print('The number is odd.')

# even_or_odd(24)
# even_or_odd(9)

# endregion