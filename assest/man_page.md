---
title: araste
section: 1
header: User Manual
footer: araste 1.2.1
date: July 7, 2022
---

# NAME
Araste - making ascii-art out of Persian/Arabic text

# SYNOPSIS
**araste** [*OPTION*] [*TEXT*]

# DESCRIPTION
Similar to the figlet and toilet tools, but for Persian and Arabic texts.


# OPTIONS

**-h** 
: display help message

**-f**
: select font

**\--list**
: list available fonts

**-F**
: chose a filter. you can concatenate filters.

**\--filter-list**
: list available filters

**-a, \--alignment**
: chose text alignment can be one of (l, r, c)

**-w, \--width**
: set maximum width of rendered output


# EXAMPLES
araste -f zivar یک نوشته‌ی فارسی

araste نوشته‌ی رنگی داخل قاب -F rainbow box

# AUTHOR
maintained by Erfan Kheyrollahi (ekm507@gmail.com)

# REPORTING BUGS
[araste source code](https://github.com/ekm507/araste)

# SEE ALSO
araste-get(1)
