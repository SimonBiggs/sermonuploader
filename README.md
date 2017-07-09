# Set up development environement

## Install Wine-Staging

https://wiki.winehq.org/Ubuntu

    wget -nc https://dl.winehq.org/wine-builds/Release.key
    sudo apt-key add Release.key
    sudo apt-add-repository https://dl.winehq.org/wine-builds/ubuntu/

    sudo apt-get install --install-recommends winehq-staging wine-staging-compat

## WinPython

Download 32 bit winpython and save the release under `./windows_libs/python`:

    https://github.com/winpython/winpython/releases/download/1.7.20170401/WinPython-32bit-3.5.3.1Zero.exe
    
## Download Bat to EXE Converter

http://www.f2ko.de/en/b2e.php

Extract `Portable/Bat_To_Exe_Converter.exe` and rename it to be: `./windows_libs/bat2exe.exe`
