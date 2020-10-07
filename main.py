from random import randint
guesses = 0
number = randint(1,10)
print("Guess a number between 1 and 10:")
guess = int(input())
while guess != number:
  print("Incorrect.")
  if guess < number:
    print("Go higher.")
  elif guess > number:
    print("Go lower.")
  print("Guess a number between 1 and 10:")
  guesses = guesses + 1
  guess = int(input())
print("Well done!")
guesses = guesses + 1
print(f"You guessed it in {guesses} attempts!")