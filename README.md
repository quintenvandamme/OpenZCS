# OpenZCS
An open source version of the ZCS(ZeqOS Coding Structure) programming language in zeqOS Chabazite

## build

### windows

- Download and install Python from [here](https://www.python.org/downloads/).

- Install nuitka `python -m pip install nuitka`

```bash
python -m nuitka --onefile --include-package=tk-inter main.py
```

### linux

#### Arch linux

- Install nuitka `python -m pip install nuitka`

- Install tkinter `sudo pacman -S tk`

```bash
python -m nuitka --follow-imports --include-package=tkinter main.py
```

#### Ubuntu

- Install nuitka `python -m pip install nuitka`

- Install tkinter `sudo apt install tk`

```bash
python -m nuitka --follow-imports --include-package=tkinter main.py
```
