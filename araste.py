#!/usr/bin/python3
import os
from sys import argv
from src.utils import message

# read from flf font file
try:
  fontFile = open('fonts/aira.flf')
  fontLine = fontFile.readline().split(' ')
except:
  message("Error", "'fonts/aira.flf' not found")

boardh = int(fontLine[1])
korsi = int(fontLine[2])
max_block_width = int(fontLine[3])
comment_lines = int(fontLine[5])
num_chars = int(fontLine[8])
for _ in range(comment_lines):
    fontFile.readline()

# airaFont is character to block
airaFont = dict()
for i in range(num_chars):
    persianChars = fontFile.readline()[:-1]
    persionAsciiChars = '\n'.join([fontFile.readline()[:-2] for i in range(boardh)])[:-1]
    airaFont[persianChars] = persionAsciiChars


# copy a block into the board
def copyboard(blockstr, cursor, board):
    block = [list(line) for line in blockstr.split('\n')]

    for widthChars in range(len(block)):
        lsize = len(block[widthChars])
        ksize = len(block[korsi])
        for j in range(lsize):
            # print(cursor - ksize)
            board[widthChars][cursor - ksize + j] = block[widthChars][j]


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
        readText = text[i]
        if text[i] in fa:
            if text[i+1] not in before_n:
                if text[i] not in after_n:
                    readText = readText + 'ـ'
            if text[i-1] not in after_n:
                readText = 'ـ' + readText

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
        if readText in airaFont:
            board, lenc = copyboard(airaFont[readText], cursor, board)
            cursor -= lenc


    # print the remaining of the board
    for line in board:
        print(''.join(line[cursor:]))


text = argv[1]

board_width = os.get_terminal_size().columns

render(text, board_width, boardh, ' ')
