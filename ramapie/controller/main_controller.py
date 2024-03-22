#!/usr/bin/python3
# -----------------------------------------------------------------------------
# Project: RamaPie
# File: main_controller.py
# Author: Christofanis Skordas (skordasc@uchicago.edu)
# -----------------------------------------------------------------------------
# Purpose:
# This file contains the main controller for the RamaPie application.
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

import sys
from typing import Optional

from qtpy.QtWidgets import QApplication

from ramapie.view import MainView


class MainController:
    """This class is responsible for controlling the main application for RamaPie."""

    def __init__(self) -> None:
        """This method initializes the main application for RamaPie."""
        self._app = QApplication(sys.argv)
        self._view = MainView()

    def run(self, version: Optional[str] = "") -> None:
        """This method is responsible for running the main application for RamaPie."""
        # Display the view
        self._view.display_window(version=version)

        # Start the PyQt application's event loop and exit the Python script with the status code returned by the
        # application
        sys.exit(self._app.exec())
