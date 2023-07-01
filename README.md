# Arch Linux Automated Installation Script

This project consists of two scripts that automate the installation of Arch Linux. This can be particularly useful if you frequently install Arch Linux and would like to reduce the amount of manual work involved.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- A system with Arch Linux ISO booted (you can use a Virtual Machine for testing)
- Internet access

### Installing

1. Clone the repository

    ```
    git clone https://github.com/yourusername/archlinux-autoinstall.git
    ```

2. Navigate to the cloned directory

    ```
    cd archlinux-autoinstall
    ```

3. Make the scripts executable

    ```
    chmod +x install_arch.sh
    chmod +x arch_auto_install.py
    ```

4. Run the `install_arch.sh` script

    ```
    ./install_arch.sh
    ```

After executing the `install_arch.sh` script, it will check for Python, install it if necessary, and then run the `arch_auto_install.py` script. During the execution of `arch_auto_install.py`, you will be prompted to select a hard drive and partition sizes.

### Important Warning

Running these scripts will make significant changes to the selected hard drive, including deleting all data on it. Make sure you understand what each script does before you run them, and only run them on a system or virtual machine that you are prepared to have wiped and configured for a new Arch Linux installation. Always ensure you have a backup of your data.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

Remember to replace the URL in the `git clone` command with the URL of your actual repository.

The above README provides a simple introduction to what your project does, the steps to install it, how to use it, and a warning about the implications of using the scripts. It also includes a mention of the license under which the project is released.
