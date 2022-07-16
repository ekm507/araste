<div align="center">
  <h1> Araste </h1>
  <h2> making ascii-art out of Persian/Arabic text </h2>
</div>

Similar to the figlet and toilet tools, but for Persian and Arabic texts.

usage:

```bash
$ araste <your text>
```

use `-f` switch to choose font

```bash
$ araste 'your persian/arabic text' -f 'fontpath or fontname'
```

for now, there are 2 fonts that you can use:
```
aipara
aipara_mini
```

it can also read text from stdin. so you can do something like this:

```bash
$ echo 'آراسته' | araste
```

to get help:

```bash
$ araste -h
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

## Install and Usage

1. for installing you only need to execute following command.

````bash
bash <(curl -s https://raw.githubusercontent.com/ekm507/araste/main/installer/install.sh)
````

or in oter shells like zsh or fish:

````bash
curl -s https://raw.githubusercontent.com/ekm507/araste/main/installer/install.sh | bash
````

2. you only need Python 3 to use the program. this program has no special dependencies.

## unistall

to uninstall araste, simply remove it's files.

if you have installed araste for system:

```bash
$ sudo rm -rf /usr/share/araste
$ sudo rm /usr/bin/araste
```

or if you have installed araste for your user only:

```bash
$ rm -rf ~/.local/share/araste
$ rm ~/.local/bin/araste
```

## Todos

Todos have been moved to a separate file. [TODOS](https://github.com/ekm507/araste/blob/main/TODOS_EN.md)

