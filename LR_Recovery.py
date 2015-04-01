"""
Author: Kris Armstrong
Date: March 26 2015
Version: 1.0
Purpose: Recover LinkRunner Pro / Duo MAC Address and Option Bits
    Option Bit 0 802.1x
    Option Bit 1 Reports
    Option Bit 2 Reflector
"""
import sys
import os


def get_linux_os_drive(lr_drive):
    """
    Function: Gets the mount point for volume label LR
    :param lr_drive:
    :return mount_point:
    """
    mount_point = "\mnt\lr"
    print("DEBUG: Getting Linux LR Drive", lr_drive)
    mount_point = os.path.abspath(mount_point)
    while mount_point != os.path.sep:
        if os.path.ismount(mount_point):
            mount_point = os.path.abspath(os.path.join(mount_point, os.pardir))
    return mount_point


def get_win32_os_drive(lr_drive):
    """
    Function: Gets the letter for volume Label LR
    :param lr_drive:
    :return drive_letter:
    """
    drive_letter = "G:"
    print("DEBUG: Getting Windows LR Drive", lr_drive)

    return drive_letter


def get_darwin_os_drive(lr_drive):
    """
    Function: Gets the mount point for volume Label LR
    :param lr_drive:
    :return mount_point:
    """
    mount_point = "\mnt\lr"
    print("DEBUG: Getting OSX LR Drive", lr_drive)

    return mount_point


def read_write_command_txt(mac_address, opt_code_0, opt_code_1, opt_code_2):
    """
    Function:
    :param mac_address:
    :param opt_code_0:
    :param opt_code_1:
    :param opt_code_2:
    :return:
    """
    # with open("command.txt", rw):

    print("DEBUG: Opening Command.txt")

    print("DEBUG: Writing Command.txt")

    print("DEBUG: Reading Results.txt")


def main():

    """
    Function: Main
    Purpose: Take User Input
        MAC Address
        Serial Number
        Get Option Codes 0, 1, 2
        Determine OS and call appropriate Function
        Once Mounts Point or Drive Letter is Determined
        Call the Read_Write Function to update the unit.
    """
    mac_address = input("Please Enter MAC Address:")
    serial_number = input("Please Enter Serial Number:")

    print("You Entered MAC Address:", mac_address, "Serial Number:", serial_number)

    system_os = sys.platform

    lr_drive = "LR"
    opt_code_0 = 0
    opt_code_1 = 1
    opt_code_2 = 2

    if sys.platform.startswith('win32'):
        # Win32-specific code here...
        print("Windows Version", system_os)
        get_win32_os_drive(lr_drive)
    elif sys.platform.startswith('linux'):
        # Linux-specific code here...
        print("Linux Version", system_os)
        get_linux_os_drive(lr_drive)
    elif sys.platform.startswith("darwin"):
        # OSX-specific code here...
        print("Mac OSX Version", system_os)
        get_linux_os_drive(lr_drive)

    read_write_command_txt(mac_address, opt_code_0, opt_code_1, opt_code_2)

if __name__ == "__main__":
    main()