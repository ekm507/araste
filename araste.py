#!/usr/bin/python3
import os
import argparse

# message handling
# levels ( Error, Warning, Info, Text )
# note: levels and text with string types
def message(level, text):
  print( f"{level}:\n{text}" )

# read from flf font file

parser = argparse.ArgumentParser()
default_font_name = 'aipara'

parser.add_argument("-f", "--font", help="add your custom font path or choose font from [ aipara - aipara-mini ]", dest="font", default=default_font_name)
parser.add_argument("--list", help="list available fonts", dest="get_font_list", action="store_true")
parser.add_argument("text", help="Text", nargs='*')

args = parser.parse_args()


# default dir where fonts are stored
# there are 2 possible options. root directory or home directory
root_font_dir = '/usr/share/araste/fonts/'
usr_font_dir = os.path.expanduser('~') + '/.local/share/araste/fonts/'

font_dir = ''
if os.path.exists(root_font_dir):
  font_dir = root_font_dir
elif os.path.exists(usr_font_dir):
  font_dir = os.path.realpath(usr_font_dir)

if args.get_font_list == True:
  fonts_list = os.listdir(font_dir)
  for font_name in fonts_list:
    print(font_name.rstrip('.flf'))
  exit(0)

# if font is a directory:
if '/' in args.font:
  font_filename = str(args.font)

else:

  if os.path.exists(font_dir):
    font_filename = font_dir.rstrip('/') + '/' + args.font.rstrip('.flf') + '.flf'

  else:
    message('Error', f'font not found!\nis araste installed?')
    exit(1)

try:
  fontFile = open(font_filename)
  flf_headers = fontFile.readline().split(' ')
except:
  message("Error", f"{font_filename} is not found")
  exit(1)

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
        if readText in font_glyphs:
            board, lenc = copyboard(font_glyphs[readText], cursor, board)
            cursor -= lenc

    # print the remaining of the board
    for line in board:
        print(''.join(line[cursor:]))


board_width = os.get_terminal_size().columns

if len(args.text) > 0:
  text = ' '.join(args.text)
  render(text, board_width, boardh, ' ')
else:
  while True:
    try:
      text = input()
      render(text, board_width, boardh, ' ')
    except EOFError:
      break
