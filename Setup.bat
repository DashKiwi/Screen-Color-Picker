@echo off
if not "%1"=="am_admin" (
    powershell -Command "Start-Process -Verb RunAs -FilePath '%0' -ArgumentList 'am_admin'"
    exit /b
)
@echo on
pip install keyboard
pip install pyscreenshot
pip install pyperclip
pip install screeninfo
pip install pynput