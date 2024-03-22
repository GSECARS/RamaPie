#!/usr/bin/python3
# -----------------------------------------------------------------------------
# Project: RamaPie
# File: settings_model.py
# Author: Christofanis Skordas (skordasc@uchicago.edu)
# -----------------------------------------------------------------------------
# Purpose:
# This file main file of the setting model package.
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
from qtpy.QtCore import QSettings

from ramapie.model.settings.display_model import DisplayModel


@dataclass
class SettingsModel:
    """This class is responsible for the settings model for RamaPie."""

    _settings: QSettings = field(init=False, repr=False, compare=False)
    _display: DisplayModel = field(init=False, repr=False, compare=False)

    def __post_init__(self) -> None:
        self._settings = QSettings("GSECARS", "RamaPie")
        self._display = DisplayModel(settings=self._settings)

    @property
    def display(self) -> DisplayModel:
        """This property returns the display model instance of the settings model."""
        return self._display
