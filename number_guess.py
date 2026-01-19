import random


    
def guess(secret_number):
    user_number = int(input("Enter a guess for a number between 1 and 10:"))
    if secret_number == user_number:
        print("You have guessed correctly!!!")
    elif user_number > secret_number:
        print("Too high! Guess again!")
        guess(secret_number)
    elif user_number < secret_number:
        print("Too low! Guess again!")
        guess(secret_number)

def main():
    secret_number = random.randint(1, 10)
    guess(secret_number)

if __name__ == "__main__":
    main()