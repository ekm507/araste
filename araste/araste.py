#!/usr/bin/python3
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


def print_line(line: str) -> None:
    return line + '\n'

def read_font(font:str) -> dict:

    # get directory where fonts are stored
    fonts_dir = __file__.replace("araste.py", "") + "fonts"

    # get font file name
    # if font is a directory:
    if '/' in font:
        font_filename = os.path.realpath(str(font))
    else:
        font_filename = fonts_dir.rstrip(
            '/') + '/' + font.replace(".aff", "") + ".aff"

    # read the font
    try:
        fontfile = open(font_filename)
        aff_headers = fontfile.readline().split(' ')
    except:
        raise FileNotFoundError

    if aff_headers[0] != 'aff2':
        sys.exit(1)


    # get font headers
    block_height = int(aff_headers[1])
    korsi = int(aff_headers[2])
    comment_lines = int(aff_headers[3])
    num_chars = int(aff_headers[5])
    for _ in range(comment_lines):
        fontfile.readline()

    # get font characters
    # font glyphs is character to block
    font_glyphs = dict()
    for i in range(num_chars):
        persianchars = fontfile.readline().rstrip('\n')
        char_variation, char_direction = list(map(int,fontfile.readline().rstrip('\n').split(' ')))
        persianasciichars = '\n'.join(
            [fontfile.readline()[:-1] for _ in range(block_height)])

        glyph_key = (persianchars, char_variation)
        glyph_data = (char_direction, persianasciichars)
        font_glyphs[glyph_key] = glyph_data
    
    font_data = {
        'height': block_height,
        'korsi': korsi,
        'glyphs': font_glyphs,
    }

    return font_data



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

        output += print_line(''.join(aligned_line))

    return output[:-1]


def find_longest_substring(text:str, glyph_headers:list, variation:int) -> tuple:

    accepting_variations = [0, variation]

    matchings = filter(lambda character: character[1] in accepting_variations and text.startswith(
        character[0]), glyph_headers)

    try:
        longest = max(matchings, key=lambda x:len(x[0]))
    except ValueError:
        longest = ('', 0)

    return longest

# convert text into ascii art and print
def render(
    text: str, 
    font: str, 
    empty_char: str = ' ', 
    filters: list = [], 
    alignment: str = 'l',
    width: int = None
) -> str:

    font_data = read_font(font)

    boardh = font_data['height']
    korsi = font_data['korsi'] - 1
    glyph_data = font_data['glyphs']


    # characters which need character to be separated if it is after them
    after_n = list("()«»رذزدژآاءٔوؤ!؟?\n. ‌،:؛")
    # characters which need character to be separated if it is before them
    before_n = list("()«» ‌،؛:ٔ.؟!?\n")
    # list of characters in persian alphabet
    fa = list('ضصثقفغعهخحجچشسیبلاتنمکگظطزآرذدپوؤءژ' + '\u200d')


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

    # get width of each character
    glyphs_width = {}
    for character in glyph_data.keys():
        # max_line_width = max([len(line) for line in font_glyphs[character].split('\n')])
        max_line_width = len(glyph_data[character][1].split('\n')[korsi])
        glyphs_width[character] = max_line_width

    # generate an empty board
    board = [[empty_char for _ in range(boardw)] for _ in range(boardh)]

    # rtl cursor
    cursor = boardw

    # add space to beginning and end of text to make it easier to handle
    text = ' ' + text + ' '

    rendered_ascii_art = ''

    # read characters from text and render them and print the result
    i = 1
    while i < len(text):

        # find appropriate variation of character
        substring = text[i]

        variation = 0

        if text[i] in fa:
            if text[i+1] not in before_n and text[i] not in after_n:
                if text[i-1] not in after_n:
                    variation = 2
                else:
                    variation = 1
            elif text[i-1] not in after_n:
                variation = 3
            else:
                variation = 4

        substring, variation = find_longest_substring(text[i:], glyph_data.keys(), variation)

        # get distance cursor should move
        if (substring, variation) in glyphs_width:
            next_width = glyphs_width[(substring, variation)]
        else:
            if (substring, 0) in glyphs_width:
                next_width = glyphs_width[(substring, 0)]
        
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
        # print(variation)
        # print(glyph_data[(substring, variation)][1])
        if (substring, variation) in glyph_data:
            board, lenc = copyboard(
                glyph_data[(substring, variation)][1], cursor, board, korsi)
                
            # move the cursor by the width of the character to the left
            cursor -= next_width
        i += len(substring) if len(substring) > 0 else 1


    # print the remaining of the board
    rendered_ascii_art += print_board(board, cursor, alignment=alignment)

    # apply filter

    if filters is not None:
        for filter in filters:
            rendered_ascii_art = apply_filter(rendered_ascii_art, filter)

    return rendered_ascii_art
