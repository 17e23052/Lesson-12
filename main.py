guesses = 0
number = 4
print("Guess a number between 1 and 10:")
guess = int(input())
while guess != 4:
  print("Incorrect.")
  print("Guess a number between 1 and 10:")
  guesses = guesses + 1
  guess = int(input())
print("Well done!")
guesses = guesses + 1
print(f"You guessed it in {guesses} attempts!")