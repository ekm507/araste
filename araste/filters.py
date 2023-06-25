# filters for araste output are here
import re
from .char_maps import hmirror_character_alternatives, vmirror_character_alternatives, flip90_character_alternatives

def apply_filter(text: str, filter_name: str) -> str:

    filter_map = {
        'rainbow': rainbow,
        'vrainbow': rainbow_vertical,
        'hrainbow': rainbow_horizontal,
        'box': box,
        'vmirror': character_aware_vertical_mirror,
        'hmirror': character_aware_horizontal_mirror,
        'ritalic': italic_right,
        'litalic': italic_left,
        'flip90': character_aware_flip90,
        'hgrow': grow_horizontal,
        'vgrow': grow_vertical,
        'red': lambda x: color('red', x),
        'orange': lambda x: color('orange', x),
        'yellow': lambda x: color('yellow', x),
        'green': lambda x: color('green', x),
        'cyan': lambda x: color('cyan', x),
        'blue': lambda x: color('blue', x),
        'purple': lambda x: color('purple', x),
        'blinker': lambda x: color('blinker', x)
    }

    if filter_name not in filter_map.keys():
        return text

    return filter_map[filter_name](text)

def get_filters() -> map:
    filters_details = {
        'rainbow': 'rainbow colors',
        'vrainbow': 'rainbow colors vertical',
        'hrainbow': 'rainbow colors horizontal',
        'box': 'text in a box',
        'vmirror': 'vertical mirror',
        'hmirror': 'horizontal mirror',
        'ritalic': 'skew the output a bit to the right',
        'litalic': 'skew the output a bit to the left',
        'flip90': 'flip art by 90 degrees',
        'hgrow': 'grow art horizontally',
        'vgrow': 'grow art vertically',
        '[red, orange, yellow, green, cyan, blue, purple, blinker]': 'output in selected color',
    }
    return filters_details

def rainbow(art:str) -> str:

    # list of colors for rainbow. ansi escape codes.
    rainbow_colors = ['\33[31m', '\33[33m', '\33[93m', '\33[32m', '\33[36m', '\33[34m', '\33[35m']

    # ansi escape code for end of color
    end_color = '\33[0m'

    output = ''

    # process text line by line
    for offset, line in enumerate(art.split('\n')):

        # apply rainbow filter on each line
        for i in range(len(line)):
            if line[i] != ' ':
                output += rainbow_colors[(i + offset) % len(rainbow_colors)] + line[i]
            else:
                output += ' '
        output += end_color + '\n'

    return output[:-1]


def rainbow_vertical(art:str) -> str:

    # list of colors for rainbow. ansi escape codes.
    rainbow_colors = ['\33[31m', '\33[33m', '\33[93m', '\33[32m', '\33[36m', '\33[34m', '\33[35m']

    # ansi escape code for end of color
    end_color = '\33[0m'

    output = ''

    # process text line by line
    for offset, line in enumerate(art.split('\n')):

        # apply rainbow filter on each line
        for i in range(len(line)):
            if line[i] != ' ':
                output += rainbow_colors[(i) % len(rainbow_colors)] + line[i]
            else:
                output += ' '
        output += end_color + '\n'

    return output[:-1]



def rainbow_horizontal(art:str) -> str:

    # list of colors for rainbow. ansi escape codes.
    rainbow_colors = ['\33[31m', '\33[33m', '\33[93m', '\33[32m', '\33[36m', '\33[34m', '\33[35m']

    # ansi escape code for end of color
    end_color = '\33[0m'

    output = ''

    # process text line by line
    for i, line in enumerate(art.split('\n')):
        output += rainbow_colors[i % len(rainbow_colors)] + line + end_color + '\n'

    return output[:-1]


def box(art:str) -> str:
    art_lines = art.split('\n')
    ansi_removed_lines = [
        re.sub(r'(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]', '', line)
        for line in art_lines
    ]

    lines_lengths = list(map(lambda line: len(line), ansi_removed_lines))
    max_width = max(lines_lengths)

    output = ''

    # top of box
    output += '╔' + '═' * max_width + '╗' + '\n'

    # box body
    for line_length, line in zip(lines_lengths, art_lines):
        output += '║' + line + ' ' * (max_width - line_length) + '║' + '\n'
    
    # bottom of box
    output += '╚' + '═' * max_width + '╝'

    return output

def vertical_mirror(art: str) -> str:
    art_lines = art.split('\n')
    art_lines.reverse()
    output = '\n'.join(art_lines)

    return output


def character_aware_vertical_mirror(art: str) -> str:
    art_lines = art.split('\n')
    art_lines.reverse()
    output = ''
    for line in art_lines:
        output_line = ''.join([vmirror_character_alternatives[char] if char in vmirror_character_alternatives.keys() else char for char in line])
        output += output_line + '\n'
    output = output[:-1]

    return output


def horizontal_mirror(art: str) -> str:
    art_lines = art.split('\n')
    ansi_escape_regex = r'((\x9B|\x1B\[)[0-?]*[ -\/]*[@-~])'

    output = ''

    for line in art_lines:    
        chars_and_escape_codes = re.split(ansi_escape_regex, line)
        # chars_and_escape_codes.reverse()
        reversed_string = ''
        for code in chars_and_escape_codes[::-1]:
            if re.match(ansi_escape_regex, code):
                reversed_string += code
            else:
                reversed_string += code[::-1]
        output += reversed_string + '\n'

    return output[:-1]


def character_aware_horizontal_mirror(art:str) -> str:
    art_lines = art.split('\n')
    ansi_escape_regex = r'((\x9B|\x1B\[)[0-?]*[ -\/]*[@-~])'

    output = ''

    for line in art_lines:    
        chars_and_escape_codes = re.split(ansi_escape_regex, line)
        # chars_and_escape_codes.reverse()
        reversed_string = ''
        for code in chars_and_escape_codes[::-1]:
            if re.match(ansi_escape_regex, code):
                reversed_string += code
            else:
                line = ''
                for char in code[::-1]:
                    if char in hmirror_character_alternatives.keys():
                        reversed_string += hmirror_character_alternatives[char]
                    else:
                        reversed_string += char

                # reversed_string += code[::-1]
        output += reversed_string + '\n'

    return output[:-1]


def italic_right(art: str) -> str:
    art_lines = art.split('\n')
    output = ''
    numof_lines = len(art_lines)
    for i, line in enumerate(art_lines):
        output += ' ' * ((numof_lines - i)) + line + '\n'
    
    return output[:-1]


def italic_left(art: str) -> str:
    art_lines = art.split('\n')
    output = ''
    for i, line in enumerate(art_lines):
        output += ' ' *  i + line + '\n'
    
    return output[:-1]

def flip90(art: str) -> str:
    art_lines = art.split('\n')

    # make a 2d matrix of chars
    art_char_list = [
        list(line)
        for line in art_lines]

    # transpose char matrix
    char_list_flipped = list(map(list, zip(*art_char_list)))

    # start writing matrix content into output
    output = ''

    for line in char_list_flipped[::-1]:
        output += ''.join(line) + '\n'

    return output[:-1]


def character_aware_flip90(art: str) -> str:
    art_lines = art.split('\n')

    # make a 2d matrix of chars
    art_char_list = [
        [flip90_character_alternatives[char] if char in flip90_character_alternatives.keys() else char for char in list(line)]
        for line in art_lines]

    # transpose char matrix
    char_list_flipped = list(map(list, zip(*art_char_list)))

    # start writing matrix content into output
    output = ''

    for line in char_list_flipped[::-1]:
        output += ''.join(line) + '\n'

    return output[:-1]


def grow_horizontal(art: str) -> str:
    grow_ratio = 2

    art_lines = art.split('\n')

    output = ''

    for line in art_lines:
        for character in line:
            output += character * grow_ratio
        output += '\n'

    return output[:-1]


def grow_vertical(art: str) -> str:
    grow_ratio = 2

    art_lines = art.split('\n')

    output = ''

    for line in art_lines:
        output += (line + '\n') * grow_ratio

    return output[:-1]

def color(color: str, art: str) -> str:

    # list of colors for rainbow. ansi escape codes.
    rainbow_colors = {
    'red':'\33[31m',
    'orange': '\33[33m',
    'yellow': '\33[93m',
    'green': '\33[32m',
    'cyan': '\33[36m',
    'blue': '\33[34m',
    'purple': '\33[35m',
    'blinker': '\33[5m'
    }

    # ansi escape code for end of color
    end_color = '\33[0m'

    art_lines = art.split('\n')
    
    output = ''
    for line in art_lines:
        line = line.replace(end_color, end_color + rainbow_colors[color])
        output += rainbow_colors[color] + line + end_color + '\n'
    
    return output[:-1]
