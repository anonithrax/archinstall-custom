import archinstall

# List available hard drives and let the user select one
available_drives = archinstall.list_drives()
print("Available drives:")
for i, drive in enumerate(available_drives, start=1):
    print(f"{i}. {drive}")
selected_drive_index = int(input("Select the drive for installation: ")) - 1
selected_drive = available_drives[selected_drive_index]
print(f"You selected {selected_drive}.")

# Ask the user to specify the partition sizes
efi_partition_size = int(input("Enter the size for the EFI partition in MiB (for example, '512' for 512MiB): "))
root_partition_size = int(input("Enter the size for the root partition in GiB (for example, '30' for 30GB): "))
# Ensure the drive is not mounted and has no partitions
archinstall.sys_command(f'umount -R /mnt', hide_output=False)
archinstall.sys_command(f'parted -s {selected_drive} mklabel gpt', hide_output=False)

# Partition the drive
# User-specified sizes for the EFI and root partitions, and the rest for home
archinstall.sys_command(f'parted -s {selected_drive} mkpart ESP fat32 1MiB {efi_partition_size}MiB', hide_output=False)
archinstall.sys_command(f'parted -s {selected_drive} set 1 esp on', hide_output=False)
archinstall.sys_command(f'parted -s {selected_drive} mkpart primary ext4 {efi_partition_size}MiB {root_partition_size}GiB', hide_output=False)
archinstall.sys_command(f'parted -s {selected_drive} mkpart primary ext4 {root_partition_size}GiB 100%', hide_output=False)

# Format the partitions
archinstall.sys_command(f'mkfs.fat -F32 {selected_drive}1', hide_output=False)
archinstall.sys_command(f'mkfs.ext4 {selected_drive}2', hide_output=False)
archinstall.sys_command(f'mkfs.ext4 {selected_drive}3', hide_output=False)

# Mount the partitions
archinstall.sys_command(f'mount {selected_drive}2 /mnt', hide_output=False)
archinstall.sys_command(f'mkdir -p /mnt/boot', hide_output=False)
archinstall.sys_command(f'mount {selected_drive}1 /mnt/boot', hide_output=False)
archinstall.sys_command(f'mkdir -p /mnt/home', hide_output=False)
archinstall.sys_command(f'mount {selected_drive}3 /mnt/home', hide_output=False)

# The rest of your script here...
