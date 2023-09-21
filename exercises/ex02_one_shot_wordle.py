"""EX02 One-Shot Wordle - Loops!"""

__author__ = "730659220"

sneaky_word: str = "python"
guess: str = input("What is your 6-letter guess? ")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
emoji = ""
idx = 0

while len(guess) != len(sneaky_word):
    guess = input(f"That was not {len(sneaky_word)} letters! Try again: ")
    
if len(guess) == len(sneaky_word):
    while idx <= len(sneaky_word) - 1:
        if guess[idx] == sneaky_word[idx]:
            emoji += GREEN_BOX
        else:
            if (guess[idx] != sneaky_word[idx]):
                existed = False
                alt_idx = 0
                while not existed and alt_idx <= len(sneaky_word) - 1:
                    if sneaky_word[alt_idx] == guess[idx]:
                        existed = True
                    else:
                        alt_idx += 1
                if existed:
                    emoji += YELLOW_BOX
                else:
                    emoji += WHITE_BOX
            
        idx += 1


print(emoji)

if guess == sneaky_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")