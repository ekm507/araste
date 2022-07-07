#!/usr/bin/python3
# from font3 import f1, korsi

# read from flf font file
a = open('f1.flf')
b = a.readline().split(' ')
boardh = int(b[1])
korsi = int(b[2])
comment_lines = int(b[5])
num_chars = int(b[8])
for _ in range(comment_lines):
    a.readline()

f1 = dict()
for i in range(num_chars):
    c = a.readline()[:-1]
    d = '\n'.join([a.readline()[:-2] for i in range(boardh)])[:-1]
    f1[c] = d


def copyboard(blockstr, cursor, board):
    block = [list(line) for line in blockstr.split('\n')]

    for i in range(len(block)):
        lsize = len(block[i])
        ksize = len(block[korsi])
        for j in range(lsize):
            # print(cursor - ksize)
            board[i][cursor - ksize + j] = block[i][j]


    return board, len(block[korsi])

after_n = list("رذزدژآاءوؤ!؟?\n. ‌،:؛")
before_n = list(" ‌،؛:.؟!?\n")
fa = list('ضصثقفغعهخحجچشسیبلاتنمکگظطزرذدپوؤءژ' + '\u200d')

def render(text, boardw, boardh, empty_char = ' '):
    board = [ [empty_char for i in range(boardw)] for j in range(boardh)]
    # text = '\n'.join(''.join(line) for line in board)
    cursor = boardw - 10
    text = ' ' + text + ' '
    for i in range(1, len(text) - 1):
        z = text[i]
        if text[i] in fa:
            if text[i+1] not in before_n:
                if text[i] not in after_n:
                    z = z + 'ـ'
            if text[i-1] not in after_n:
                z = 'ـ' + z
        

        board, lenc = copyboard(f1[z], cursor, board)
        # print(z, lenc)
        cursor -= lenc


    for line in board:
        print(''.join(line[cursor:]))

text = 'ببب پ بابا'
# text = 'ا'

from sys import argv
text = argv[1]
render(text, 200, 18, ' ')
# qa = f1['ا'].split('\n')
# qb = f1['ب'].split('\n')
# qr = f1['ر'].split('\n')
# for i in range(len(qa)):
#     print(qr[i], qb[i], qa[i], sep='')
