"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730659220"

# ensuring that word entered is 5 characters and character entered is 1 character
user_word: str = input("Enter a 5-character word: ")
if len(user_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
user_letter: str = input("Enter a single character: ")
if len(user_letter) != 1:
     print("Error: Character must be a single character.")
     exit()
print(f"Searching for {user_letter} in {user_word}")

# finding location of character in word
match_char = 0
if user_letter == user_word[0]:
    print (f"{user_letter} found at index 0")
    match_char = match_char + 1
if user_letter == user_word[1]:
    print (f"{user_letter} found at index 1")
    match_char = match_char + 1
if user_letter == user_word[2]:
    print (f"{user_letter} found at index 2")
    match_char = match_char + 1
if user_letter == user_word[3]:
    print (f"{user_letter} found at index 3")
    match_char = match_char + 1
if user_letter == user_word[4]:
    print (f"{user_letter} found at index 4")
    match_char = match_char + 1

# find number of instances of character in word
if match_char == 1:
    print (f"1 instance of {user_letter} found in {user_word}")
if match_char == 2:
    print (f"2 instances of {user_letter} found in {user_word}")
if match_char == 3:
    print (f"3 instances of {user_letter} found in {user_word}")
if match_char == 4:
    print (f"4 instances of {user_letter} found in {user_word}")
if match_char == 5:
    print (f"5 instances of {user_letter} found in {user_word}")
if match_char == 0:
    print (f"No instances of {user_letter} found in {user_word}")