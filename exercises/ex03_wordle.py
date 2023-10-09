"""Creating a wordle!"""

__author__ = "730659220"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

secret_word = "codes"


def contains_char(str_input: str, letter_input: str) -> bool:
    """When given a string and a single character, True will be returned if the string contains the character and false will be returned if not."""
    assert len(letter_input) == 1
    char_idx: int = 0
 
    while char_idx < len(str_input):
        if str_input[char_idx] == letter_input:
            return True
        char_idx = char_idx + 1 
    else:
        return False
    

def emojified(guess: str, sneaky_word: str) -> str:
    """When given two strings of equal length, if a character matches or doesn't mach the sneak_word, colored emojis will be returned."""
    idx = 0
    emoji = ""
    
    while idx <= len(sneaky_word) - 1:
        if guess[idx] == sneaky_word[idx]:
            emoji += GREEN_BOX
        else:
            if contains_char(sneaky_word, guess[idx]):
                emoji += YELLOW_BOX
            else:
                emoji += WHITE_BOX
        idx = idx + 1
    return emoji


def input_guess(expected_length: int) -> str:
    """When given the expected length of a word, this function displays if the length entered matches the length prompted."""
    guess_ipt = input(f"Enter a {(expected_length)} character word: ")
    while len(guess_ipt) != expected_length:
        guess_ipt = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess_ipt


def main() -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    winner: bool = False

    while turn < 7 and not winner:
        print(f"=== Turn {turn}/6 ===")
        guess_str = input_guess(len(secret_word))
        print(emojified(guess_str, secret_word))
        if guess_str == secret_word:
            winner = True
            print(f"You won in {turn}/6 turns!")
            return
        turn = turn + 1
        if turn > 6:
            print("X/6 - Sorry, try again tomorrow!")
        

"""This is an idiom common to Python programs."""
if __name__ == "__main__":
    main()
