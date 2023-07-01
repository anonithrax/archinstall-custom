import archinstall

# Ask the user for the hard drive
selected_drive = archinstall.select_disk(archinstall.all_disks())

# Set the partition sizes
boot_partition_size = selected_drive.size // 100  # 1% of total size
root_partition_size = selected_drive.size // 2  # 50% of total size
home_partition_size = selected_drive.size - boot_partition_size - root_partition_size  # remaining size

# Define the filesystem layout
filesystem_layout = {
    "mountpoints": {
        "/": {"size": root_partition_size, "filesystem": "ext4"},
        "/home": {"size": home_partition_size, "filesystem": "ext4"},
        "/boot": {"size": boot_partition_size, "filesystem": "vfat"},
    }
}

# Start the installation process
with archinstall.Installer(selected_drive, archinstall.Layout(filesystem_layout)) as installation:
    # Set hostname
    installation.set_hostname('anondeskvm')

    # Set the root password
    installation.set_root_password('AnonDesk#1234')

    # Add a new user
    installation.add_new_user('anon', 'Anon#1234', is_sudo=True)

    # Select the profiles (xorg, audio, pipewire, etc.)
    installation.select_profile('xorg')
    installation.select_profile('audio')
    installation.add_additional_packages(['pipewire', 'pipewire-pulse', 'pipewire-jack', 'pipewire-alsa', 'pipewire-media-session', 'gst-plugin-pipewire'])
    installation.enable_service('pipewire')

    # Set up the bootloader
    installation.add_bootloader()

    installation.install()

# All done!
print("Installation complete!")
