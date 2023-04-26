import random

def generate_random_number():
    return random.randint(0, 100)
max_tries = 10
def play_game():
    tries_count = 0
    tries_numbers = []
    random_number =generate_random_number()
    while tries_count < max_tries:
        user_num = int(input("Enter Your Number : "))
        if (user_num < 0 or user_num > 100):
            print("Your Number Out of Rannge 0-100 only")
            continue
        if (user_num in tries_numbers):
            print("You enterd this number before change it ")
            continue
        if (user_num > random_number ):
            print("Your Number is bigger than the random number")
            tries_numbers.append(user_num)
            tries_count += 1
            continue
        elif (user_num < random_number ):
            print("Your Number is smaller than the random number")
            tries_numbers.append(user_num)
            tries_count += 1
            continue
        else:
            print("Congratulations! You guessed the number in", max_tries - tries_count, "tries.")
            play_again = input("Do you want to play again? (y/n): ")
            if play_again.lower() == 'y':
                tries_numbers = []
                random_number  = generate_random_number()
            else:
                print("Thanks for playing!")
                return
        
    print("Sorry, you ran out of tries. The random number was", random_number)
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() == 'y':
        play_game()
    else:
        print("Thanks for playing!")
play_game()