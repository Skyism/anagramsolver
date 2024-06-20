from trie import Trie
class anaBoard:
    def __init__(self):
        self.board = []


    def makeboard(self, string):
        for char in string:
            self.board.append(char)

    def getunused(self, used):
        unused = []
        for i in range(len(self.board)):
            if str(i) not in used:
                unused.append(i)
        return unused

    def solve(self, index, path, used, results, trie):
        path.append(self.board[index])
        used.append(str(index))
        word = "".join(path)

        if trie.search(word) and len(word) >= 3:
            results.add(word)

        if trie.prefixsearch(word):
            unused = self.getunused(used)
            for i in unused:
                self.solve(i, path, used, results, trie)

        path.pop()
        used.remove(str(index))

    def getall(self, trie):
        results = set()
        for x in range(len(self.board)):
            self.solve(x, [], [], results, trie)
        return results


