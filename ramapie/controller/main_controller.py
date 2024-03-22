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
import time
from typing import Optional

from qtpy.QtCore import Qt
from qtpy.QtWidgets import QApplication

from ramapie.model import MainModel, QtWorkerModel
from ramapie.view import MainView


class MainController:
    """This class is responsible for controlling the main application for RamaPie."""

    def __init__(self) -> None:
        """This method initializes the main application for RamaPie."""
        self._app = QApplication(sys.argv)
        self._model = MainModel()
        self._view = MainView(directories=self._model.directories)

        # Main application thread
        self._main_worker = QtWorkerModel(self._thread_methods, ())

        # Run main controller methods
        self._configure_main_controller()

    def run(self, version: Optional[str] = "") -> None:
        """This method is responsible for running the main application for RamaPie."""
        # Display the view
        self._view.display_window(
            version=version, size=self._model.settings.display.size, position=self._model.settings.display.position, state=self._model.settings.display.state
        )

        # Start the PyQt application's event loop and exit the Python script with the status code returned by the
        # application
        sys.exit(self._app.exec())

    def _thread_methods(self) -> None:
        """Run all thread methods"""
        while not self._view.close_triggered:
            time.sleep(0.05)

        # Set thread status to finished, so the GUI loop can end
        self._view.threads_finished = True

    def _close_event_triggered(self) -> None:
        """Saves the main application window size, position and state."""
        # Save the size
        self._model.settings.display.size = self._view.size()
        # Save the position
        self._model.settings.display.position = self._view.pos()
        # Save the state (maximized or not)
        if self._view.windowState() == Qt.WindowState.WindowMaximized:
            self._model.settings.display.state = 4
        else:
            self._model.settings.display.state = 2

    def _configure_main_controller(self) -> None:
        """Basic configuration for the main controller functionality."""
        # Connects the signal and slot for the main view settings.
        self._view.close_event_changed.connect(self._close_event_triggered)
        # Start the main application thread
        self._main_worker.start()
