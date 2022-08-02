# filters for araste output are here
import re

def apply_filter(text: str, filter_name: str) -> str:

    filter_map = {
        'rainbow': rainbow,
        'vrainbow': rainbow_vertical,
        'hrainbow': rainbow_horizontal,
        'box': box,
        'vmirror': vertical_mirror,
        'hmirror': horizontal_mirror,
        'ritalic': italic_right,
        'litalic': italic_left,
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
    first_line_ansii_removed = re.sub(r'(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]', '', art_lines[0])
    width = len(first_line_ansii_removed)

    output = ''
    output += '╔' + '═' * width + '╗' + '\n'
    for line in art_lines:
        output += '║' + line + '║' + '\n'
    output += '╚' + '═' * width + '╝'

    return output

def vertical_mirror(art: str) -> str:
    art_lines = art.split('\n')
    art_lines.reverse()
    output = '\n'.join(art_lines)

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
