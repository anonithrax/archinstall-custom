import archinstall

# Define the hard drive (in this case we're assuming it's /dev/sda)
hard_drive = '/dev/sda'

# Ensure the drive is not mounted and has no partitions
archinstall.sys_command(f'umount -R /mnt', hide_output=False)
archinstall.sys_command(f'parted -s {hard_drive} mklabel gpt', hide_output=False)

# Partition the drive
# 512MB for the EFI partition, 30GB for the root partition, and the rest for home
archinstall.sys_command(f'parted -s {hard_drive} mkpart ESP fat32 1MiB 513MiB', hide_output=False)
archinstall.sys_command(f'parted -s {hard_drive} set 1 esp on', hide_output=False)
archinstall.sys_command(f'parted -s {hard_drive} mkpart primary ext4 513MiB 30.5GiB', hide_output=False)
archinstall.sys_command(f'parted -s {hard_drive} mkpart primary ext4 30.5GiB 100%', hide_output=False)

# Format the partitions
archinstall.sys_command(f'mkfs.fat -F32 {hard_drive}1', hide_output=False)
archinstall.sys_command(f'mkfs.ext4 {hard_drive}2', hide_output=False)
archinstall.sys_command(f'mkfs.ext4 {hard_drive}3', hide_output=False)

# Mount the partitions
archinstall.sys_command(f'mount {hard_drive}2 /mnt', hide_output=False)
archinstall.sys_command(f'mkdir -p /mnt/boot', hide_output=False)
archinstall.sys_command(f'mount {hard_drive}1 /mnt/boot', hide_output=False)
archinstall.sys_command(f'mkdir -p /mnt/home', hide_output=False)
archinstall.sys_command(f'mount {hard_drive}3 /mnt/home', hide_output=False)

# Select the mirror servers for the installation
with archinstall.Filesystem(hard_drive, '/mnt') as fs:
    fs.load_os_profiles()
    installation = archinstall.Installer(fs)

# Select the profile (xorg, audio, pipewire, etc.)
installation.select_profile('xorg')
installation.select_profile('audio')
installation.add_additional_packages(['pipewire', 'pipewire-pulse', 'pipewire-jack', 'pipewire-alsa', 'pipewire-media-session', 'gst-plugin-pipewire'])
installation.enable_service('pipewire')

# Set hostname
installation.set_hostname('anondeskvm')

# Set the root password
installation.set_root_password('AnonDesk#1234')

# Add a new user
installation.add_new_user('anon', 'Anon#1234', is_sudo=True)

# Set up the bootloader
installation.add_bootloader()

installation.install()

# All done!
print("Installation complete!")
