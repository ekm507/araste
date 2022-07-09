<div align="center">
  <h1> Araste </h1>
  <h2> Transforming Persian writings into the art of skiing </h2>
</div>

Similar to the figlet tool, but for Persian and Arabic texts.

**Note: Araste tool is under Development**

Currently, you can write a command, sentence or several lines of text with the following command, using the default font.

```bash
$ araste 'آراسته'
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

- [x] Designing a Persian ascii font.
- [x] Support flf format similar to figlet.
- [x] Another font design.
- [ ] Having 3 font.
- [x] converting fonts to flf format.
- [ ] debuging the flf format fonts.
- [x] development a tool on commandline with installer.
- [ ] release the version one
- [x] write an english readme
- [ ] Adding the possibility of selecting fonts and listing available fonts
