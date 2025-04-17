# LinkRunnerRecovery

A Python tool to recover and update MAC address, serial number, and option bits on a LinkRunner Pro/Duo device.

Designed for network technicians and administrators, it writes commands to `command.txt` and reads `results.txt` on the device's drive, with cross-platform detection for Windows, Linux, and macOS.

## Installation
```bash
chmod +x linkrunner_recovery.py
```

## Usage
### linkrunner_recovery.py
```bash
./linkrunner_recovery.py --mac_address 00:11:22:33:44:55 --serial_number ABC123 [--opt_8021x 1] [--opt_reports 1] [--opt_reflector 1] [--verbose] [--logfile path]
```

### version_bumper.py
```bash
python version_bumper.py --project_dir /path/to/project [--type minor] [--commit] [--git_tag] [--dry_run]
```

## Generated Files (via git_setup.py)
- **.gitignore**: Ignores Python, IDE, OS, and project-specific files (e.g., `__pycache__`, `.venv`, `tests/output/`).
- **README.md**: Project template with customizable title, installation, and usage.
- **CHANGELOG.md**: Initial changelog with a 0.1.0 entry, customizable author.
- **requirements.txt**: Placeholder for dependencies.
- **LICENSE**: Proprietary license for LinkRunner devices.
- **CONTRIBUTING.md**: Fork-branch-PR guidelines.
- **CODE_OF_CONDUCT.md**: Contributor Covenant with contact info.
- **tests/**: Directory with a placeholder test file.
- **version_bumper.py** (optional): Tool for bumping semantic versions.

## Notes
- **Proprietary License**: This software is intended for use with LinkRunner Pro/Duo devices. Unauthorized distribution or modification is prohibited.
- **Drive Detection**: Requires a mounted device with volume label “LR” or `linkrunner.id` file.

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com)
[![Coverage](https://img.shields.io/badge/coverage-90%25-brightgreen)](https://github.com)
[![License](https://img.shields.io/badge/license-Proprietary-red)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org)