#!/usr/bin/python3
import os
from sys import argv
<<<<<<< HEAD
 
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
=======
from src.utils import message

# read from flf font file
font_filename = 'fonts/aipara.flf'
try:
  fontFile = open(font_filename)
  flf_headers = fontFile.readline().split(' ')
except:
  message("Error", f"{font_filename} not found")

boardh = int(flf_headers[1])
korsi = int(flf_headers[2])
max_block_width = int(flf_headers[3])
comment_lines = int(flf_headers[5])
num_chars = int(flf_headers[8])
for _ in range(comment_lines):
    fontFile.readline()

# font glyphs is character to block
font_glyphs = dict()
for i in range(num_chars):
    persianChars = fontFile.readline()[:-1]
    persionAsciiChars = '\n'.join([fontFile.readline()[:-2] for i in range(boardh)])[:-1]
    font_glyphs[persianChars] = persionAsciiChars
>>>>>>> pr


# copy a block into the board
def copyboard(blockstr, cursor, board):
    block = [list(line) for line in blockstr.split('\n')]

<<<<<<< HEAD
    for i in range(len(block)):
        lsize = len(block[i])
        ksize = len(block[korsi])
        for j in range(lsize):
            # print(cursor - ksize)
            board[i][cursor - ksize + j] = block[i][j]
=======
    for widthChars in range(len(block)):
        lsize = len(block[widthChars])
        ksize = len(block[korsi])
        for j in range(lsize):
            # print(cursor - ksize)
            board[widthChars][cursor - ksize + j] = block[widthChars][j]
>>>>>>> pr


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
<<<<<<< HEAD
        z = text[i]
=======
        readText = text[i]
>>>>>>> pr
        if text[i] in fa:
            if text[i+1] not in before_n:
                if text[i] not in after_n:
                    readText = readText + 'ـ'
            if text[i-1] not in after_n:
<<<<<<< HEAD
                z = 'ـ' + z
=======
                readText = 'ـ' + readText
>>>>>>> pr

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
<<<<<<< HEAD
        if z in f1:
            board, lenc = copyboard(f1[z], cursor, board)
            cursor -= lenc


=======
        if readText in font_glyphs:
            board, lenc = copyboard(font_glyphs[readText], cursor, board)
            cursor -= lenc

>>>>>>> pr
    # print the remaining of the board
    for line in board:
        print(''.join(line[cursor:]))


<<<<<<< HEAD
text = argv[1]

board_width = os.get_terminal_size().columns

render(text, board_width, boardh, ' ')
=======
try:
  text = argv[1]
except:
  text = ""

board_width = os.get_terminal_size().columns

try:
  render(text, board_width, boardh, ' ')
except:
  render("", board_width, boardh, ' ')
>>>>>>> pr
