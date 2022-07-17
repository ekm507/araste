<div align="center">
  <h1> Araste </h1>
  <h2> making ascii-art out of Persian/Arabic text </h2>
</div>

Similar to the figlet and toilet tools, but for Persian and Arabic texts.

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

## Install and Usage

for installing you only need to execute following command.

````bash
pip install araste
````

2. or to build it yourself:

```bash
git clone 'https://github.com/ekm507/araste/'
cd araste
python3 setup.py bdist_wheel
pip install ./dist/araste-1.1-py3-none-any.whl
```

## Instaling Fonts
For Installing Fonts You Can Use araste-get
````bash
araste-get FontName
````
## Unistall

to uninstall araste, simply use pip.

```bash
pip uninstall araste
```

## Create New Font
To get additional fonts or create custom fonts using ![araste-fonts](https://github.com/ekm507/araste-fonts) .

In that repository of fonts created and added by users, there are guides for designing and creating fonts and such tools for this purpose .

## Todos

Todos have been moved to a separate file. [TODOS](https://github.com/ekm507/araste/blob/main/TODOS_EN.md)

