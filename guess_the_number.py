import random

correct = 'you guessed correctly!'
too_low = 'too low'
too_high = 'too high'

def configure_range():
    '''Set the high and low values for the random number'''
    return 1, 10


def generate_secret(low, high):
    '''Generate a secret number for the user to guess'''
    return random.randint(low, high)


def get_guess():
    '''get user's guess'''

    guess = int(input('Guess the secret number? '))

    if guess == 0:
        return(guess)
    if guess == 1:
        return(guess)
    if guess == 2:
        return(guess)
    if guess == 3:
        return(guess)
    if guess == 4:
        return(guess)
    if guess == 5:
        return(guess)
    if guess == 6:
        return(guess)
    if guess == 7:
        return(guess)
    if guess == 8:
        return(guess)
    if guess == 9:
        return(guess)
    if guess == 10:
        return(guess)
    else:
        print("Please enter a number")
        get_guess()

def check_guess(guess, secret):
    '''compare guess and secret, return string describing result of comparison'''
    if guess == secret:
        return correct
    if guess < secret:
        return too_low
    if guess > secret:
        return too_high


def main():

    (low, high) = configure_range()
    secret = generate_secret(low, high)

    guess_counter = 0

    while True:
        guess = get_guess()
        result = check_guess(guess, secret)
        print(result)

        guess_counter += 1
        #print(guess_counter)
        if result == correct:
            break


if __name__ == '__main__':
    main()
