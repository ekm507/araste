# filters for araste output are here
from distutils.command.build_scripts import first_line_re
import re

def apply_filter(text: str, filter_name: str) -> str:

    filter_map = {
        'rainbow': rainbow,
        'box': box,
        'vmirror': vertical_mirror,
    }

    if filter_name not in filter_map.keys():
        return text

    return filter_map[filter_name](text)

def get_filters() -> map:
    filters_details = {
        'rainbow': 'rainbow colors',
        'box': 'text in a box',
        'vmirror': 'vertical mirror',
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
    output = ''
    art_lines.reverse()
    for line in art_lines:
        output += line + '\n'

    return output[:-1]