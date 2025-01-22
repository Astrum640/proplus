import os
import subprocess
import ctypes

def is_admin():
    """Check if the script is running with administrative privileges."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def check_disk():
    """Run the Windows CHKDSK utility to check disk for errors."""
    print("Checking disk for errors...")
    try:
        subprocess.run("chkdsk C: /f /r /x", check=True, shell=True)
        print("Disk check completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while checking the disk: {e}")

def repair_disk():
    """Repair disk errors using the Windows SFC utility."""
    print("Repairing disk errors...")
    try:
        subprocess.run("sfc /scannow", check=True, shell=True)
        print("Disk repair completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while repairing the disk: {e}")

def main():
    """Main function to diagnose and repair disk errors."""
    if not is_admin():
        print("This program requires administrative privileges to run.")
        print("Please run the program as an administrator.")
        return

    print("ProPlus - Disk Diagnostics and Repair Tool")
    print("1. Check Disk for Errors")
    print("2. Repair Disk")
    choice = input("Please select an option (1 or 2): ")

    if choice == '1':
        check_disk()
    elif choice == '2':
        repair_disk()
    else:
        print("Invalid selection. Please choose 1 or 2.")

if __name__ == "__main__":
    main()