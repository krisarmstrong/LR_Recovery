#!/usr/bin/env python3
"""
Project Title: LinkRunnerRecoveryTests

Pytest smoke tests for linkrunner_recovery.py functionality.

Author: Kris Armstrong
"""
__version__ = "1.0.0"

import pytest
import subprocess
from pathlib import Path
import linkrunner_recovery

@pytest.fixture
def temp_dir(tmp_path: Path) -> Path:
    """Create a temporary directory for testing.

    Args:
        tmp_path: Pytest-provided temporary path.

    Returns:
        Path to temporary directory.
    """
    return tmp_path

def test_parse_arguments_valid(temp_dir: Path) -> None:
    """Test parsing valid command-line arguments."""
    args = linkrunner_recovery.parse_arguments(['--mac_address', '00:11:22:33:44:55', '--serial_number', 'ABC123'])
    assert args.mac_address == '00:11:22:33:44:55'
    assert args.serial_number == 'ABC123'
    assert args.opt_8021x == 0
    assert args.opt_reports == 0
    assert args.opt_reflector == 0

def test_keyboard_interrupt(temp_dir: Path, caplog: pytest.LogCaptureFixture) -> None:
    """Test KeyboardInterrupt handling.

    Args:
        temp_dir: Temporary directory for testing.
        caplog: Pytest fixture to capture log output.
    """
    with pytest.raises(SystemExit) as exc:
        linkrunner_recovery.setup_logging(False)
        raise KeyboardInterrupt
    assert exc.value.code == 0
    assert "Cancelled by user" in caplog.text

def test_version_bumper_generation(temp_dir: Path) -> None:
    """Test version_bumper.py generation."""
    from git_setup import VERSION_BUMPER_TEMPLATE, create_file
    create_file(temp_dir / 'version_bumper.py', VERSION_BUMPER_TEMPLATE)
    assert (temp_dir / 'version_bumper.py').exists()
    result = subprocess.run(['python', 'version_bumper.py', '--help'], cwd=temp_dir, capture_output=True, text=True)
    assert result.returncode == 0