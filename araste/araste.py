#!/usr/bin/python3
from math import floor
import os
import sys
from araste.filters import apply_filter

# copy a block into the board
def copyboard(blockstr: str, cursor: int, board: list, korsi: int) -> tuple:
    block = [list(line) for line in blockstr.split('\n')]

    for widthChars in range(len(block)):
        lsize = len(block[widthChars])
        ksize = len(block[korsi])
        if cursor - ksize + lsize > len(board[0]):
            lsize = - cursor + ksize + len(board[0])

        for j in range(lsize):
            # print(cursor - ksize)
            board[widthChars][cursor - ksize + j] = block[widthChars][j]

    return board, len(block[korsi])


def print_line(line: str, offset: int = 0) -> None:
    return line + '\n'


def print_board(
    board: list,
    cursor: int, 
    alignment: str = 'l',
) -> None:

    output = ''

    for i, line in enumerate(board):

        # add spaces to the line to align it
        if alignment == 'l':
            aligned_line = ''.join(line[cursor:])
        elif alignment == 'r':
            aligned_line = ' ' * cursor + ''.join(line[cursor:])
        elif alignment == 'c':
            num_spaces_left = cursor // 2
            num_spaces_right = cursor - num_spaces_left
            aligned_line = ' ' * num_spaces_left + ''.join(line[cursor:]) + ' ' * num_spaces_right

        output += print_line(''.join(aligned_line), offset=i)

    return output[:-1]


# convert text into ascii art and print
def render(
    text: str, 
    font: str, 
    empty_char: str = ' ', 
    filters: list = [], 
    alignment: str = 'l',
    width: int = None
) -> str:

    # get directory where fonts are stored
    fonts_dir = __file__.replace("araste.py", "") + "fonts"

    # get font file name
    # if font is a directory:
    if '/' in font:
        font_filename = os.path.realpath(str(font))
    else:
        font_filename = fonts_dir.rstrip(
            '/') + '/' + font.replace(".flf", "") + ".flf"

    # read the font
    try:
        fontfile = open(font_filename)
        flf_headers = fontfile.readline().split(' ')
    except:
        raise FileNotFoundError

    # get board width
    # if board width is not provided in args:
    if width == None:
        # try to get terminal width
        if sys.stdout and sys.stdout.isatty():
            boardw = os.get_terminal_size().columns
        # if terminal is not available (e.g: output is being piped or redirected)
        else:
            # set the width to 80 as default
            boardw = 80
    # if board width is provided in args, just use it
    else:
        boardw = width

    # get font headers
    boardh = int(flf_headers[1])
    korsi = int(flf_headers[2])
    max_block_width = int(flf_headers[3])
    comment_lines = int(flf_headers[5])
    num_chars = int(flf_headers[8])
    for _ in range(comment_lines):
        fontfile.readline()

    # characters which need character to be separated if it is after them
    after_n = list("()«»رذزدژآاءوؤ!؟?\n. ‌،:؛")
    # characters which need character to be separated if it is before them
    before_n = list("()«» ‌،؛:.؟!?\n")
    # list of characters in persian alphabet
    fa = list('ضصثقفغعهخحجچشسیبلاتنمکگظطزرذدپوؤءژ' + '\u200d')

    # get font characters
    # font glyphs is character to block
    font_glyphs = dict()
    for i in range(num_chars):
        persianchars = fontfile.readline()[:-1]
        persianasciichars = '\n'.join(
            [fontfile.readline()[:-2] for _ in range(boardh)])[:-1]
        font_glyphs[persianchars] = persianasciichars
    
    # get width of each character
    glyphs_width = {}
    for character in font_glyphs.keys():
        # max_line_width = max([len(line) for line in font_glyphs[character].split('\n')])
        max_line_width = len(font_glyphs[character].split('\n')[korsi])
        glyphs_width[character] = max_line_width

    # generate an empty board
    board = [[empty_char for _ in range(boardw)] for _ in range(boardh)]

    # rtl cursor
    cursor = boardw

    # add space to beginning and end of text to make it easier to handle
    text = ' ' + text + ' '

    rendered_ascii_art = ''

    # read characters from text and render them and print the result
    for i in range(1, len(text) - 1):

        # find appropriate variation of character
        readtext = text[i]
        if text[i] in fa:
            if text[i+1] not in before_n:
                if text[i] not in after_n:
                    readtext = readtext + 'ـ'
            if text[i-1] not in after_n:
                readtext = 'ـ' + readtext

        # get distance cursor should move
        if readtext in glyphs_width:
            next_width = glyphs_width[readtext]
        else:
            next_width = 0
        
        # check if you need a newline
        # if cursor has reached the end of the board or if character is a newline character
        if cursor <= next_width or text[i] in ['\n', '\r']:

            rendered_ascii_art += print_board(board, cursor, alignment=alignment)
            rendered_ascii_art += '\n'
            # print(rendered_ascii_art)

            # reset the board and cursor
            cursor = boardw
            board = [[empty_char for _ in range(boardw)]
                     for _ in range(boardh)]

        # copy the block of the character into the board
        if readtext in font_glyphs:
            
            board, lenc = copyboard(
                font_glyphs[readtext], cursor, board, korsi)
                
            # move the cursor by the width of the character to the left
            cursor -= next_width

    # print the remaining of the board
    rendered_ascii_art += print_board(board, cursor, alignment=alignment)

    # apply filter

    if filters is not None:
        for filter in filters:
            rendered_ascii_art = apply_filter(rendered_ascii_art, filter)

    return rendered_ascii_art
