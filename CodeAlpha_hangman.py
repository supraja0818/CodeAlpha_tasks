import random
pics = [
    """
     +---+
         |
         |
         |
        ===""",
    """

     +---+
     O   |
         |
         |
        ===""",
    """
     +---+
     O   |
     |   |
         |
        ===""",
    """
     +---+
     O   |
    /|   |
         |
        ===""",
    """
     +---+
     O   |
    /|\\  |
         |
        ===""",
    """
     +---+
     O   |
    /|\\  |
    /    |
        ===""",
    """
     +---+
     O   |
    /|\\  |
    / \\  |
        ==="""
]
words = ["python", "apple", "banana", "school", "hangman"]
secret = random.choice(words)
secret_letters = list(secret)

guessed = []
wrong = []

max_wrong = len(pics) - 1

print("Welcome to Hangman!")

while True:
    print(pics[len(wrong)])
    display = ""
    for ch in secret:
        if ch in guessed:
            display += ch + " "
        else:
            display += "_ "
    print("\nWord:", display)
    print("Wrong letters:", wrong)
    print("Tries left:", max_wrong - len(wrong))

    # Check win
    if all(ch in guessed for ch in secret_letters):
        print("\n🎉 You won! The word was:", secret)
        break

    # Check loss
    if len(wrong) > max_wrong - 1:
        print("\n💀 You lost! The word was:", secret)
        break

    # Take input
    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.")
        continue

    if guess in guessed or guess in wrong:
        print("You already guessed this letter.")
        continue

    # Check guess match
    if guess in secret_letters:
        guessed.append(guess)
    else:
        wrong.append(guess)
