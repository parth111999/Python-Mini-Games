import random
randomnum = random.randint(1,50)

userguess = None
guesses = 0 

while (userguess != randomnum):
  userguess = int(input("Enter your guessed number : "))
  guesses += 1
  if (userguess == randomnum):
    print("You Have Guessed it Correctly XD ")
  else:
    if (userguess > randomnum):
      print("Guess a Smaller Number")
    else:
      print("Guess a Larger Number")
print(f"You Have Guessed the Number in {guesses} guesses")

with open("hiscore.txt", "r") as f:
    hiscore = int(f.read())

if(guesses<hiscore):
    print("You have just broken the high score!")
    with open("hiscore.txt", "w") as f:
        f.write(str(guesses))