# Imports
from screeninfo import get_monitors
from pynput.mouse import Controller
from PIL import Image
import keyboard
import mss
import pyperclip
import os

# Global Variables
HOTKEY = "ctrl+alt+c"

# Functions
def get_color(coordX, coordY):
    monitors = get_monitors()
    for monitor in monitors:
        if monitor.x <= coordX < monitor.x + monitor.width and monitor.y <= coordY < monitor.y + monitor.height:
            adjusted_x = coordX - monitor.x
            adjusted_y = coordY - monitor.y
            bbox = (monitor.x, monitor.y, monitor.x + monitor.width, monitor.y + monitor.height)
            with mss.mss() as sct:
                screenshot = sct.grab(bbox)
                image = Image.frombytes("RGB", (screenshot.width, screenshot.height), screenshot.rgb)
                pixel_color = image.getpixel((adjusted_x, adjusted_y))
                return pixel_color
    
    return (0, 0, 0)

def rgb_to_hex(rgb):
    clamp = lambda x: max(0, min(x, 255))
    return f"#{clamp(rgb[0]):02x}{clamp(rgb[1]):02x}{clamp(rgb[2]):02x}"

def get_position():
    mouse = Controller()
    return mouse.position

def on_hotkey_press():
    cursor_position = get_position()
    color = get_color(cursor_position[0], cursor_position[1])
    hex_color = rgb_to_hex(color)
    print("\nColor Grabbed")
    print(f"Coordinates: X = {cursor_position[0]}, Y = {cursor_position[1]}")
    print(f"HEX: {hex_color}")
    print(f"RGB: {', '.join(str(i) for i in color)}")
    pyperclip.copy(hex_color)

# Start
keyboard.add_hotkey(HOTKEY, on_hotkey_press)
os.system('cls||clear & title Screen Color Picker')
print(f"Point your mouse cursor at anywhere on the screen, hit {HOTKEY.upper()}")
print("The HEX color code will be available on your clipboard. (Also printed here)\n")
keyboard.wait()
