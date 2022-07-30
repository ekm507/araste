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

araste [options] <your text>


# DESCRIPTION
Similar to the figlet and toilet tools, but for Persian and Arabic texts.

# COMMANDS

usage:

```bash
araste <your text>
```

use `-f` switch to choose font

```bash
araste 'your persian/arabic text' -f 'fontpath or fontname'
```

to get a list of installed fonts:

```bash
araste --list
```

for now, there are a few fonts that you can use:
```
aipara
aipara_mini
zivar
nima
```

it can also read text from stdin. so you can do something like this:

```bash
echo 'آراسته' | araste
```

to get help:

```bash
araste -h
```


an output with the default font (aipara):

```
                                      ██████
        ████                ██        ██
  ████                      ██          ██
  ████    ██    ██  ██  ██  ██    ██    ██
    ██████████████████████  ██    ██    ██
                                  ██
                                ██
```

# Instaling Fonts

For Installing Fonts You Can Use araste-get
````bash
araste-get install FontName
````

# Creating New Fonts!

To get additional fonts for araste or to create your own custom fonts, use tools and manuals in [araste-fonts](https://github.com/ekm507/araste-fonts) repo.

