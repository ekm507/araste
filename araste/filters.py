# filters for araste output are here

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

    return output
