import random

words = ["orca", "cobra", "veado", "zebra", "corvo", "mosquito", "peixe", "jacare", "hiena", "lula", "minhoca"]
word = random.choice(words)

def hangman(word):
    wrong = 0
    stages = ["",
             "________ FORCA  ",
             "|               ",
             "|       |       ",
             "|       0       ",
             "|      /|\\     ",
             "|      / \\     ",
             "|               "
             ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("WELCOME TO HANGMAN!!")
    print()
    print((" ".join(board)))

    while wrong < len(stages) - 1:
        print()
        char = input("Guess a letter: ")
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))

        if "__" not in board:
            print("You win!. It was:")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong]))
        print(("You lose!. It was:"))
        print(" ".join(word))
            

hangman(word)