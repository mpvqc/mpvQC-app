#  mpvQC
#
#  Copyright (C) 2022 mpvQC developers
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.

import inject
from PySide6.QtCore import QObject, Signal, Property
from PySide6.QtQml import QmlElement

from mpvqc.services.player import PlayerService

QML_IMPORT_NAME = "pyobjects"
QML_IMPORT_MAJOR_VERSION = 1


@QmlElement
class MpvqcMpvPlayerPropertiesPyObject(QObject):
    #

    mpv_version_changed = Signal(str)
    mpv_version = Property(str, lambda self: self.mpv.mpv_version, notify=mpv_version_changed)

    #

    ffmpeg_version_changed = Signal(str)
    ffmpeg_version = Property(str, lambda self: self.mpv.ffmpeg_version, notify=ffmpeg_version_changed)

    #

    video_loaded_changed = Signal(bool)
    video_loaded = Property(bool, lambda self: bool(self.mpv.path), notify=video_loaded_changed)

    #

    path_changed = Signal(str)
    path = Property(str, lambda self: str(self.mpv.path), notify=path_changed)

    #

    filename_changed = Signal(str)
    filename = Property(str, lambda self: str(self.mpv.filename), notify=filename_changed)

    #

    def get_duration(self):
        return self._duration

    duration_changed = Signal(float)
    duration = Property(float, get_duration, notify=duration_changed)

    #

    def get_percent_pos(self):
        return self._percent_pos

    percent_pos_changed = Signal(int)
    percent_pos = Property(int, get_percent_pos, notify=percent_pos_changed)

    #

    def get_time_pos(self):
        return self._time_pos

    time_pos_changed = Signal(int)
    time_pos = Property(int, get_time_pos, notify=time_pos_changed)

    #

    def get_time_remaining(self):
        return self._time_remaining

    time_remaining_changed = Signal(int)
    time_remaining = Property(int, get_time_remaining, notify=time_remaining_changed)

    #

    def get_height(self):
        return self._height

    heightChanged = Signal(int)
    height = Property(int, get_height, notify=heightChanged)

    #

    def get_width(self):
        return self._width

    widthChanged = Signal(int)
    width = Property(int, get_width, notify=widthChanged)

    def __init__(self):
        super().__init__()
        self.mpv = inject.instance(PlayerService).mpv

        self._subscribe_to_path()
        self._subscribe_to_filename()
        self._subscribe_to_duration()
        self._subscribe_to_percent_pos()
        self._subscribe_to_time_pos()
        self._subscribe_to_time_remaining()
        self._subscribe_to_height()
        self._subscribe_to_width()

    def _subscribe_to_path(self):
        self._path = ''

        @self.mpv.property_observer('path')
        def observer(_, value: str):
            if value and value != self._path:
                self._path = value
                self.path_changed.emit(value)
            self.video_loaded_changed.emit(bool(value))

    def _subscribe_to_filename(self):
        self._filename = ''

        @self.mpv.property_observer('filename')
        def observer(_, value: str):
            if value and value != self._filename:
                self._filename = value
                self.filename_changed.emit(value)

    def _subscribe_to_duration(self):
        self._duration = None

        @self.mpv.property_observer('duration')
        def observer(_, value: float):
            if value:
                self._duration = value
                self.duration_changed.emit(value)

    def _subscribe_to_percent_pos(self):
        self._percent_pos = None

        @self.mpv.property_observer('percent-pos')
        def observer(_, value: float):
            if value:
                value = round(value)
                if value != self._percent_pos:
                    self._percent_pos = value
                    self.percent_pos_changed.emit(value)

    def _subscribe_to_time_pos(self):
        self._time_pos = None

        @self.mpv.property_observer('time-pos')
        def observer(_, value: float):
            if value:
                value = round(value)
                if value != self._time_pos:
                    self._time_pos = value
                    self.time_pos_changed.emit(value)

    def _subscribe_to_time_remaining(self):
        self._time_remaining = None

        @self.mpv.property_observer('time-remaining')
        def observer(_, value: float):
            if value:
                value = round(value)
                if value != self._time_remaining:
                    self._time_remaining = value
                    self.time_remaining_changed.emit(value)

    def _subscribe_to_height(self):
        self._height = None

        @self.mpv.property_observer('height')
        def observer(_, value: float):
            if value:
                value = round(value)
                if value != self._height:
                    self._height = value
                    self.heightChanged.emit(value)

    def _subscribe_to_width(self):
        self._width = None

        @self.mpv.property_observer('width')
        def observer(_, value: float):
            if value:
                value = round(value)
                if value != self._width:
                    self._width = value
                    self.widthChanged.emit(value)