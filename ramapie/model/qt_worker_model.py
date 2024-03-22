#!/usr/bin/python3
# -----------------------------------------------------------------------------
# Project: RamaPie
# File: qt_worker_model.py
# Author: Christofanis Skordas (skordasc@uchicago.edu)
# -----------------------------------------------------------------------------
# Purpose:
# This file contains the main worker model for the RamaPie application.
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

from qtpy.QtCore import QThread
from typing import Any, Callable


class QtWorkerModel(QThread):
    """The main worker class that's been used for threading."""

    def __init__(self, method: Callable[[], None], args: Any) -> None:
        super(QtWorkerModel, self).__init__()

        self._method = method
        self._args = args

    def run(self) -> None:
        self._method(*self._args)
