#  mpvQC
#
#  Copyright (C) 2022 mpvQC developers
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.


import inject
from PySide6.QtCore import Slot, Signal
from PySide6.QtQml import QmlElement
from PySide6.QtQuick import QQuickFramebufferObject

from mpvqc.impl.player_renderer import PlayerRenderer

QML_IMPORT_NAME = "pyobjects"
QML_IMPORT_MAJOR_VERSION = 1


@QmlElement
class MpvPlayerPyObject(QQuickFramebufferObject):
    """ Adapted from https://gitlab.com/robozman/python-mpv-qml-example """

    sig_on_update = Signal()

    def __init__(self):
        super().__init__()
        from mpvqc.services.player import PlayerService
        self._player = inject.instance(PlayerService)
        self.sig_on_update.connect(self.do_update)

    @Slot()
    def do_update(self):
        self.update()

    def createRenderer(self) -> QQuickFramebufferObject.Renderer:
        # todo: Workaround https://bugreports.qt.io/browse/PYSIDE-1868
        # Need to hold a reference in the Python object for now
        # Once the fix is rolled out, this should be inlined
        self._renderer = PlayerRenderer(self)
        return self._renderer

    @Slot()
    def pause(self):
        self._player.pause()

    @Slot(int)
    def jump_to(self, seconds: int):
        self._player.jump_to(seconds)

    @Slot(int, int)
    def move_mouse(self, x, y):
        self._player.move_mouse(x, y)

    @Slot()
    def scroll_up(self):
        self._player.scroll_up()

    @Slot()
    def scroll_down(self):
        self._player.scroll_down()

    @Slot()
    def press_mouse_left(self):
        self._player.press_mouse_left()

    @Slot()
    def press_mouse_middle(self):
        self._player.press_mouse_middle()

    @Slot()
    def release_mouse_left(self):
        self._player.release_mouse_left()