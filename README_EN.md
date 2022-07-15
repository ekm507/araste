<div align="center">
  <h1> Araste </h1>
  <h2> Transforming Persian writings into the art of skiing </h2>
</div>

Similar to the figlet tool, but for Persian and Arabic texts.

**Note: Araste tool is under Development**

Currently, you can write a command, sentence or several lines of text with the following command, using the default font.

```bash
$ araste your text
```

or for choose the font

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

or for helps

```bash
$ araste -h
```


the Program output with default font:

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

1. for installing you only need to exec this command.

````bash
bash <(curl -s https://raw.githubusercontent.com/ekm507/araste/main/installer/install.sh)
````

or in oter shells for example fish :

````bash
curl -s https://raw.githubusercontent.com/ekm507/araste/main/installer/install.sh | bash
````

2. you only need Python 3 to use the program. this program has no dependencies on oter packages .

## Todos

Todos have been moved to a separate file. ![TODOS](https://github.com/ekm507/araste/blob/main/TODOS_EN.md)

