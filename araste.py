#!/usr/bin/python3
import os
from sys import argv
from src.utils import message

# read from flf font file
a = open('f1.flf')
b = a.readline().split(' ')
boardh = int(b[1])
korsi = int(b[2])
max_block_width = int(b[3])
comment_lines = int(b[5])
num_chars = int(b[8])
for _ in range(comment_lines):
    a.readline()

# f1 is character to block
f1 = dict()
for i in range(num_chars):
    c = a.readline()[:-1]
    d = '\n'.join([a.readline()[:-2] for i in range(boardh)])[:-1]
    f1[c] = d


# copy a block into the board
def copyboard(blockstr, cursor, board):
    block = [list(line) for line in blockstr.split('\n')]

    for i in range(len(block)):
        lsize = len(block[i])
        ksize = len(block[korsi])
        for j in range(lsize):
            # print(cursor - ksize)
            board[i][cursor - ksize + j] = block[i][j]


    return board, len(block[korsi])

# characters which need character to be separated if it is after them
after_n = list("رذزدژآاءوؤ!؟?\n. ‌،:؛")
# characters which need character to be separated if it is before them
before_n = list(" ‌،؛:.؟!?\n")
# list of characters in persian alphabet
fa = list('ضصثقفغعهخحجچشسیبلاتنمکگظطزرذدپوؤءژ' + '\u200d')

# convert text into ascii art and print
def render(text, boardw, boardh, empty_char = ' '):

    # generate an empty board
    board = [ [empty_char for i in range(boardw)] for j in range(boardh)]

    # rtl cursor
    cursor = boardw - max_block_width

    # add space to beginning and end of text to make it easier to handle
    text = ' ' + text + ' '

    # read characters from text
    for i in range(1, len(text) - 1):

        # find appropriate variation of character
        z = text[i]
        if text[i] in fa:
            if text[i+1] not in before_n:
                if text[i] not in after_n:
                    z = z + 'ـ'
            if text[i-1] not in after_n:
                z = 'ـ' + z

        # check if you need a newline
        # if cursor has reached the end of the board or if character is a newline character
        if cursor < max_block_width or text[i] in ['\n', '\r']:

            # print the board
            for line in board:
                print(''.join(line[cursor:]))

            # reset the board and cursor
            cursor = boardw - max_block_width
            board = [ [empty_char for i in range(boardw)] for j in range(boardh)]
        
        # copy the block of the character into the board
        if z in f1:
            board, lenc = copyboard(f1[z], cursor, board)
            cursor -= lenc


    # print the remaining of the board
    for line in board:
        print(''.join(line[cursor:]))


text = argv[1]

board_width = os.get_terminal_size().columns

render(text, board_width, boardh, ' ')
