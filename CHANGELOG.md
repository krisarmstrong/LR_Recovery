# Changelog

## [2.0.1] - 2025-04-17

### Patch
- Added type annotations, rotating log handler, sensitive data checks.
- Added tests for drive detection and command writing.

## [2.0.0] - 2025-04-16

### Added
- Refactored for Python 3 compatibility, removing Python 2-specific code.
- Replaced os.path with pathlib for cross-platform path handling.
- Replaced input() with argparse for command-line argument parsing.
- Added logging to linkrunner_recovery.log with verbose console option.
- Implemented sequential file I/O for command.txt and results.txt.
- Added Config class for global constants.
- Improved drive/mount point detection for Windows, Linux, macOS.
- Added MAC address validation using regex.
- Ensured PEP 8 compliance with Google-style docstrings.
- Added error handling for file operations and inputs.
- Set up Git repository with .gitignore, version_bumper.py, requirements.txt.
- Added README.md and CHANGELOG.md.
- Archived original script in archive/v1.0.0/.

## [1.0.0] - 2015-03-26

### Added
- Initial release for Python 2.
- Basic functionality for MAC address and option bits recovery.
- Supported Windows, Linux, macOS with placeholder drive detection.
- Used interactive input for MAC address and serial number.