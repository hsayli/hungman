import random

def hangman():
    list1 = ["python", "java", "computer", "hacker", "painter"]
    rnumber = random.randint(0,4)
    word = list1[rnumber]
    wrong = 0
    stages = ["",
              "___________        ",
              "|                  ",
              "|          |       ",
              "|          O       ",
              "|         /|\      ",
              "|         / \      ",
              "|                  "
              ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("welcome to hungman")
    while wrong < len(stages) - 1:
        print("\n")
        guess = input("guess a letter: ")
        if guess in rletters:
            character_index = rletters.index(guess)
            board[character_index] = guess
            rletters[character_index] = "$"
        else:
            wrong += 1
        print((" ".join(board)))
        print("\n".join(stages[0:wrong + 1]))
        if "__" not in board:
            print("you win! word was: ")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("you loose!! ward was:{}.".format(word))
hangman()
        
