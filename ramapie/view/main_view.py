#!/usr/bin/python3
# -----------------------------------------------------------------------------
# Project: RamaPie
# File: main_view.py
# Author: Christofanis Skordas (skordasc@uchicago.edu)
# -----------------------------------------------------------------------------
# Purpose:
# This file contains the main view for the RamaPie application.
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

from pathlib import PurePosixPath
from qtpy.QtCore import QPoint, QSize, Qt, QEvent, Signal
from qtpy.QtGui import QCloseEvent, QIcon
from qtpy.QtWidgets import QMainWindow, QMessageBox

from ramapie.model import PathModel


class MainView(QMainWindow):
    """This class is responsible for displaying the main application for RamaPie."""

    close_event_changed: Signal = Signal()

    def __init__(self, directories: PathModel) -> None:
        super(MainView, self).__init__()

        # Directories
        self._directories = directories

        # Event helpers
        self._close_triggered: bool = False
        self.threads_finished: bool = False

    def display_window(self, version: str | None, size: QSize | None, position: QPoint | None, state: int) -> None:
        # Set the window title based on the version number
        self.setWindowTitle(f"RamaPie {version}") if version else self.setWindowTitle("RamaPie")
        # Set the window icon
        self.setWindowIcon(QIcon(PurePosixPath(self._directories.icon_path).joinpath("RamaPie.png").as_posix()))
        # Display the window
        self.showNormal()

        # Set the window size
        if size:
            self.resize(size)
        # Set the window position
        if position:
            self.move(position)

        # Set the window state
        if state == 4:
            self.setWindowState(Qt.WindowState.WindowMaximized)

    def changeEvent(self, event: QEvent, **kwargs) -> None:
        """Updates the state of the window on changes."""
        if event.type() == QEvent.WindowStateChange:
            # Center the window to screen after
            if event.oldState() & Qt.WindowState.WindowMaximized:
                center = self.screen().availableGeometry().center()

                # Position the window in the middle of the active screen
                x = int(center.x() - self.width() / 2)
                y = int(center.y() - self.height() / 2)
                self.setGeometry(x, y, 800, 600)

    def closeEvent(self, event: QCloseEvent) -> None:
        """Creates a message box for exit confirmation if closeEvent is triggered."""
        _msg_question = QMessageBox.question(
            self,
            "Exit confirmation",
            "Are you sure you want to close the application?",
            defaultButton=QMessageBox.No,
        )

        if _msg_question == QMessageBox.Yes:

            # Emit the application close event changed signal, to update the main window settings.
            self.close_event_changed.emit()

            # Make sure that all other threads are aborted before closing.
            self._close_triggered = True
            while not self.threads_finished:
                continue

            # Close application
            event.accept()
        else:
            event.ignore()

    @property
    def close_triggered(self) -> bool:
        return self._close_triggered
