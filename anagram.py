from trie import Trie
from board import anaBoard

trie = Trie()
def maketrie():
    #creates Trie
    words = open("newdict.txt", "r")
    for word in words:
        trie.insert(word.strip().lower())
    print("created trie succesfully")

def solver():
    letters = input("insert board ")
    board = anaBoard()
    board.makeboard(letters)

    print(sorted(board.getall(trie), key=len, reverse=True))

def start():
    maketrie()
    while True:
        action = input("Type R to resume, Q to quit ")
        if action == "Q":
            return
        elif action == "R":
            solver()
        else:
            print("Invalid input")

start()