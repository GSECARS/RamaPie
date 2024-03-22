#!/usr/bin/python3
# -----------------------------------------------------------------------------
# Project: RamaPie
# File: path_model.py
# Author: Christofanis Skordas (skordasc@uchicago.edu)
# -----------------------------------------------------------------------------
# Purpose:
# This file contains the PathModel class, which is responsible for the
# paths of the RamaPie icons and style files.
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

from dataclasses import dataclass, field
from pathlib import Path, PurePosixPath


@dataclass
class PathModel:
    """Model that holds the paths for the assets directories."""

    _assets_path: str = field(init=False, compare=False, repr=False)
    _icon_path: str = field(init=False, compare=False, repr=False)

    def __post_init__(self) -> None:
        self._assets_path = Path("ramapie/assets").absolute().as_posix()
        self._icon_path = PurePosixPath(self._assets_path).joinpath("icons").as_posix()

    @property
    def icon_path(self) -> str:
        """Return the path of the icons' directory."""
        return self._icon_path
