#!/usr/bin/python3
# -----------------------------------------------------------------------------
# Project: RamaPie
# File: version.py
# Author: Christofanis Skordas (skordasc@uchicago.edu)
# -----------------------------------------------------------------------------
# Purpose:
# This file is used to update the version of the package based on the git tag.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# ----------------------------------------------------------------------

import subprocess
from pathlib import Path

# Paths
__static_version_path__ = Path(__file__).resolve().parent / ".static-version"
__pyproject_toml_path__ = Path(__file__).resolve().parent.parent / "pyproject.toml"


def get_static_version() -> str:
    """Reads the static version from the file and returns it."""
    try:
        # Read the static version from the file
        with open(__static_version_path__, "r") as static_version_file:
            static_version = static_version_file.read().strip()
    except FileNotFoundError:
        # If the file does not exist, set the version to None
        static_version = None
    return static_version if static_version else "0.0.1"


def update_static_version_file(git_tag: str) -> None:
    """Updates the static version file with the current tag."""
    with open(__static_version_path__, "w") as static_version_file:
        static_version_file.write(f"{git_tag}\n")


def check_for_tags() -> str:
    """Check if the current git commit has a tag and return it if it does."""
    try:
        # Get the latest tag
        git_tag = subprocess.check_output(["git", "describe", "--tags"]).decode("utf-8").strip()
        # Update the static version file
        update_static_version_file(git_tag)
    except subprocess.CalledProcessError:
        # If there is no tag, get the static version
        git_tag = get_static_version()
    return git_tag


def update_pyproject_toml_file() -> None:
    """Updates the version on the pyproject.toml file."""
    # Read the file
    with open(__pyproject_toml_path__, "r") as pyproject_toml_file:
        pyproject_toml = pyproject_toml_file.readlines()

    # Flag to check if we are in the [project] section
    in_project_section = False

    # Find the line with the version under [project] and update it
    for i, line in enumerate(pyproject_toml):
        stripped_line = line.strip()
        if stripped_line.startswith("[") and stripped_line.endswith("]"):
            # We are starting a new section
            in_project_section = stripped_line == "[project]"
        elif "version" in line and in_project_section:
            # We are in the [project] section and found the version line
            pyproject_toml[i] = f'version = "{get_static_version()}"\n'
            break

    # Write the updated file
    with open(__pyproject_toml_path__, "w") as pyproject_toml_file:
        pyproject_toml_file.writelines(pyproject_toml)


# Check if the current commit has a git tag
tag = check_for_tags()
# Update the static version file
update_static_version_file(git_tag=tag)
# Update the pyproject.toml file
update_pyproject_toml_file()
