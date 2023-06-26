#!/usr/bin/python3
__version__ = "3.2.1"

import os
import sys
from araste.filters import apply_filter

# copy a block into the board
def copyboard_glyph(blockstr: str, cursor: int, board: list, korsi: int) -> tuple:
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

def copyboard_string(substring_data: tuple, glyph_data: dict, cursor: int, board: list, korsi: int, direction: int) -> tuple:
    # if substring_data[1] == 1:
    #     sub_direction = 'rtl'
    # else:
    #     sub_direction = 'ltr'

    substring = substring_data[0]
    sub_direction = substring_data[1]    

    if sub_direction == direction:
        for character in substring:
            glyph = glyph_data[character][1]
            board, cursor = copyboard_glyph(
                glyph, cursor, board, korsi)




def print_line(line: str) -> None:
    return line + '\n'

def read_font(font:str) -> dict:

    # get directory where fonts are stored
    fonts_dir = __file__.replace("__init__.py", "") + "fonts"

    # get font file name
    # if font is a directory:
    if '/' in font:
        font_filename = os.path.realpath(str(font))
    else:
        font_filename = fonts_dir.rstrip(
            '/') + '/' + font.replace(".aff", "") + ".aff"

    file_line = 0
    # read the font
    try:
        fontfile = open(font_filename)
        aff_headers = fontfile.readline().split(' ')
        file_line += 1
    except:
        raise FileNotFoundError

    if aff_headers[0] != 'aff3':
        print('this is not an aff3 font. or there is an Error in header.', file=sys.stderr)
        sys.exit(1)


    # get font headers
    block_height = int(aff_headers[1])
    korsi = int(aff_headers[2])
    comment_lines = int(aff_headers[3])
    num_chars = int(aff_headers[5])
    default_direction = int(aff_headers[6])
    for _ in range(comment_lines):
        fontfile.readline()
        file_line += 1

    # get font characters
    # font glyphs is character to block
    font_glyphs = dict()
    for i in range(num_chars):

        persianchars = fontfile.readline().rstrip('\n')
        file_line += 1
        if len(persianchars) == 0:
            print(f'there is an Error in Line {file_line}', file=sys.stderr)
            print(f'character for this glyph is empty.', file=sys.stderr)

        

        try:
            line = fontfile.readline()
            if len(line) < 1:
                print(f'file seems to be broken. trying to read a glyph that does not exist!', file=sys.stderr)
                print(f'ignoring from line {file_line}', file=sys.stderr)
                break

            char_variation, char_direction = list(map(int,line.rstrip('\n').split(' ')))
            file_line += 1
        except ValueError:
            print(f'there is an Error in font file. somewhere near Line {file_line}', file=sys.stderr)
            sys.exit(1)
        
        persianasciichars = '\n'.join(
            [fontfile.readline()[:-1] for _ in range(block_height)])
        
        file_line += block_height

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
        matchings = filter(lambda character: text.startswith(character[0]), glyph_headers)
        try:
            longest = max(matchings, key=lambda x:len(x[0]))
        except ValueError:
            longest = ('', 0)

    return longest

def split_into_directioned_substrings(text:str, glyph_data: dict) -> list:
    substrings = []
    substring = []
    direction = 1
    i = 0
    while i < len(text):
        glyph = find_longest_substring(text[i:], glyph_data, 0)
        # print(glyph)
        try:
            glyph_direction = glyph_data[glyph][0]
        except:
            i += 1
            continue
        # print(glyph_direction, direction)
        if glyph_direction in [direction, 0]:
            substring.append(glyph[0])
        else:
            # print(substring, direction)
            substrings.append( (substring, direction) )
            direction = glyph_direction
            substring = [glyph[0]]
        
        if len(glyph[0]) > 0:
            i += len(glyph[0])
        else:
            i += 1

    substrings.append( (substring, direction) )


    return substrings

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

    substrings = split_into_directioned_substrings(text, glyph_data)
    directioned_chars = []
    for substring in substrings:
        # if text is right to left
        if substring[1] == 1:
            directioned_chars += substring[0]
        else:
            directioned_chars += substring[0][::-1]
    
    directioned_text = ''.join(directioned_chars)

    text = directioned_text


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

        try:
            max_line_width = len(glyph_data[character][1].split('\n')[korsi])
        except IndexError:
            print(f'there is an Error in font file. is the Korsi set correctly?', file=sys.stderr)
            sys.exit(1)

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
    while i < len(text) - 1:

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
            board, lenc = copyboard_glyph(
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
