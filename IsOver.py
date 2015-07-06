# coding : utf-8


class IsOver():
    """docstring for IsOver"""
    def __init__(self, chessbook):
        super(IsOver, self).__init__()
        self.chessbook = chessbook
        self.parse(self.chessbook)

    def isWin(self, chessbookParsed):
        winList = [123, 456, 789, 147, 258, 369, 159, 357]
        for winWay in chessbookParsed:
            if winWay in winList:
                return True
        return False

# x:player1 o:player2 n:null
    def parse(self, string):
        
        pass

