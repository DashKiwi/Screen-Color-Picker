# Screen Color Picker

A python program to pick the specific color of a pixel on screen

## Installation

If you are running a windows machine, you can run the Setup.bat file (will ask for administrator) on the top folder or you can manually install the required library's below.

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the following library's.

```bash
pip install keyboard
pip install pyscreenshot
pip install pyperclip
pip install screeninfo
pip install pynput
```
For Linux or Mac OS you may have to run the 'pip install keyboard' command with sudo E.g. 'sudo pip install keyboard'
## Usage
If you are running on a windows machine, you can run the Start.bat file which will start the program automatically (runs the command lines below). It is pretty useless by itself so I recommend adding a shortcut.
```bash
cd yourdrive:\path\to\foler
python Main.py
```
alternatively you could run the python file in your own IDE whatever you do it is up too you!

## Settings
Keybinds: To change the hotkey which is what gets the color, change the "HOTKEY" variable as shown in the example below. HOTKEY is located on the 11th line as shown below.

```python
6.  import mss
7.  import pyperclip
8.  import os
9.
10. # Global Variables
11. HOTKEY = "ctrl+alt+c"
12.
13. # Functions
```
## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)