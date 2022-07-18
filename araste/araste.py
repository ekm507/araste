#!/usr/bin/python3
import os

# copy a block into the board

rainbow_colors = ['\33[31m', '\33[33m', '\33[93m', '\33[32m', '\33[36m', '\33[34m', '\33[35m']
end_color = '\33[0m'

def copyboard(blockstr, cursor, board, korsi):
    block = [list(line) for line in blockstr.split('\n')]

    for widthChars in range(len(block)):
        lsize = len(block[widthChars])
        ksize = len(block[korsi])
        for j in range(lsize):
            # print(cursor - ksize)
            board[widthChars][cursor - ksize + j] = block[widthChars][j]

    return board, len(block[korsi])

# convert text into ascii art and print

def print_rainbow(text, offset=0):
    for i in range(len(text)):
        if text[i] != ' ':
            print(rainbow_colors[(i + offset) % len(rainbow_colors)] + text[i], sep='', end='')
        else:
            print(text[i], end='', sep='')
    print(end_color)

def render(text, font, empty_char=' ', rainbow=False):

    fonts_dir = __file__.replace("araste.py", "") + "fonts"

    # if font is a directory:
    if '/' in font:
        font_filename = os.path.realpath(str(font))
    else:

        font_filename = fonts_dir.rstrip(
            '/') + '/' + font.replace(".flf", "") + ".flf"

    try:
        fontFile = open(font_filename)
        flf_headers = fontFile.readline().split(' ')
    except:
        raise FileNotFoundError

    boardw = os.get_terminal_size().columns
    boardh = int(flf_headers[1])
    korsi = int(flf_headers[2])
    max_block_width = int(flf_headers[3])
    comment_lines = int(flf_headers[5])
    num_chars = int(flf_headers[8])
    for _ in range(comment_lines):
        fontFile.readline()

    # characters which need character to be separated if it is after them
    after_n = list("()«»رذزدژآاءوؤ!؟?\n. ‌،:؛")
    # characters which need character to be separated if it is before them
    before_n = list("()«» ‌،؛:.؟!?\n")
    # list of characters in persian alphabet
    fa = list('ضصثقفغعهخحجچشسیبلاتنمکگظطزرذدپوؤءژ' + '\u200d')

    # font glyphs is character to block
    font_glyphs = dict()
    for i in range(num_chars):
        persianChars = fontFile.readline()[:-1]
        persionAsciiChars = '\n'.join(
            [fontFile.readline()[:-2] for _ in range(boardh)])[:-1]
        font_glyphs[persianChars] = persionAsciiChars

    # generate an empty board
    board = [[empty_char for _ in range(boardw)] for _ in range(boardh)]

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
            for i, line in enumerate(board):
                if rainbow:
                    print_rainbow(''.join(line[cursor:]), offset=0)
                else:
                    print(''.join(line[cursor:]))

            # reset the board and cursor
            cursor = boardw - max_block_width
            board = [[empty_char for _ in range(boardw)]
                     for _ in range(boardh)]

        # copy the block of the character into the board
        if readText in font_glyphs:
            board, lenc = copyboard(
                font_glyphs[readText], cursor, board, korsi)
            cursor -= lenc

    # print the remaining of the board
    for i, line in enumerate(board):
        if rainbow:
            print_rainbow(''.join(line[cursor:]), offset=0)
        else:
            print(''.join(line[cursor:]))
