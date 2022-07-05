from font3 import f1, korsi

def copyboard(blockstr, cursor, board):
    block = [list(line) for line in blockstr.split('\n')]

    for i in range(len(block)):
        lsize = len(block[i])
        for j in range(lsize):
            board[i][cursor - lsize + j] = block[i][j];

    return board, len(block[korsi])

after_n = list("رذزدژاءوؤ!؟?\n. ‌،:؛")
before_n = list(" ‌،؛:.؟!?\n")
fa = list('ضصثقفغعهخحجچشسیبلاتنمکگظطزرذدپوؤءژ')

def render(text, boardw, boardh, empty_char = ' '):
    board = [ [empty_char for i in range(boardw)] for j in range(boardh)]
    # text = '\n'.join(''.join(line) for line in board)
    cursor = boardw
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
render(text, 100, 10, '.')
# qa = f1['ا'].split('\n')
# qb = f1['ب'].split('\n')
# qr = f1['ر'].split('\n')
# for i in range(len(qa)):
#     print(qr[i], qb[i], qa[i], sep='')