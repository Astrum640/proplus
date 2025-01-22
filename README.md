# ProPlus

ProPlus is a Python-based utility designed to diagnose and repair common disk errors on Windows systems. Its primary goal is to prevent system crashes and data loss by utilizing Windows built-in tools like CHKDSK and SFC.

## Features

- **Disk Error Checking**: Uses CHKDSK to scan and fix disk errors.
- **Disk Repair**: Leverages SFC to repair corrupted system files.

## Requirements

- Windows operating system
- Python 3.x installed
- Administrative privileges to run the script

## Installation

1. Clone this repository to your local machine.
   ```bash
   git clone https://github.com/yourusername/proplus.git
   ```
2. Navigate to the project directory.
   ```bash
   cd proplus
   ```

## Usage

1. Open a command prompt with administrative privileges.
2. Run the Python script using:
   ```bash
   python proplus.py
   ```
3. Follow the on-screen instructions to either check for disk errors or repair disk issues.

## Important Notes

- **Administrative Privileges**: The script requires administrative rights to execute the necessary system commands. Ensure you run it as an administrator.
- **Data Backup**: It's always advisable to back up your data before running disk repair tools.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.