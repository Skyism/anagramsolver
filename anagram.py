from trie import Trie
from board import anaBoard
def main():
    #creates Trie
    trie = Trie()

    words = open("newdict.txt", "r")
    for word in words:
        trie.insert(word.strip().lower())
    print("created trie succesfully")

    letters = input("insert board ")
    board = anaBoard()
    board.makeboard(letters)

    print(sorted(board.getall(trie), key=len, reverse=True))



main()