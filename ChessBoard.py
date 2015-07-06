# coding : utf-8
import sqlite3

class ChessBoard(object):
    """docstring for ChessBoard"""
    def __init__(self, arg):
        super(ChessBoard, self).__init__()
        self.arg = arg

    def printBoard(chessbook):
        # 1|2|3
        # 4|5|6
        # 7|8|9

        print "{0}|{1}|{2}\n{3}|{4}|{5}\n{6}|{7}|{8}".format(chessbook)
