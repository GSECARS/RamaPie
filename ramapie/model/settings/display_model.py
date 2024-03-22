#!/usr/bin/python3
# -----------------------------------------------------------------------------
# Project: RamaPie
# File: display_model.py
# Author: Christofanis Skordas (skordasc@uchicago.edu)
# -----------------------------------------------------------------------------
# Purpose:
# This file contains the display model settings for the RamaPie application.
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
from qtpy.QtCore import QSettings, QSize, QPoint


@dataclass
class DisplayModel:
    """The main display settings model for the RamaPie application."""

    settings: QSettings = field(repr=False, compare=False)

    _size: QSize = field(init=False, repr=False, compare=False, default=None)
    _position: QPoint = field(init=False, repr=False, compare=False, default=None)
    _state: int = field(init=False, repr=False, compare=False, default=2)

    def __post_init__(self) -> None:
        self._size = self.settings.value("window_size", type=QSize)
        self._position = self.settings.value("window_position", type=QPoint)
        self._state = self.settings.value("window_state", type=int)

    @property
    def size(self) -> QSize | None:
        """This property returns the size of the window."""
        return self._size

    @size.setter
    def size(self, value: QSize) -> None:
        """This property sets the size of the window."""
        self._size = value
        self.settings.setValue("window_size", value)

    @property
    def position(self) -> QPoint | None:
        """This property returns the position of the window."""
        return self._position

    @position.setter
    def position(self, value: QPoint) -> None:
        """This property sets the position of the window."""
        self._position = value
        self.settings.setValue("window_position", value)

    @property
    def state(self) -> int:
        """This property returns the state of the window."""
        return self._state

    @state.setter
    def state(self, value: int) -> None:
        """This property sets the state of the window."""
        self._state = value
        self.settings.setValue("window_state", value)
