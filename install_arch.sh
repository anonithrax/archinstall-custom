#!/bin/bash

# Check if Python is installed
if command -v python3 &>/dev/null; then
    echo "Python 3 is installed, proceeding to the installation script."
else
    echo "Python 3 is not installed. Installing Python 3 now."
    pacman -Sy --noconfirm python
fi

# Run the Python Arch Linux installation script
python3 arch_auto_install.py
