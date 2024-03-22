#!/usr/bin/python3
# -----------------------------------------------------------------------------
# Project: RamaPie
# File: main_model.py
# Author: Christofanis Skordas (skordasc@uchicago.edu)
# -----------------------------------------------------------------------------
# Purpose:
# This file contains the main model for the RamaPie application.
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

from ramapie.model.settings import SettingsModel


@dataclass
class MainModel:
    """This class is responsible for the main model for RamaPie."""

    _settings: SettingsModel = field(init=False, repr=False, compare=False)

    def __post_init__(self) -> None:
        self._settings = SettingsModel()

    @property
    def settings(self) -> SettingsModel:
        """This property returns the settings model instance of the main model."""
        return self._settings
