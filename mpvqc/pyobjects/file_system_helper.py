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

from pathlib import Path

import inject
from PySide6.QtCore import QUrl, Slot, QObject
from PySide6.QtQml import QmlElement

from mpvqc.services import ApplicationPathsService

QML_IMPORT_NAME = "pyobjects"
QML_IMPORT_MAJOR_VERSION = 1


@QmlElement
class MpvqcFileSystemHelperPyObject(QObject):
    _paths = inject.attr(ApplicationPathsService)

    # noinspection PyTypeChecker
    @Slot(QUrl, result=str)
    def url_to_absolute_path(self, url: QUrl) -> str:
        path = Path(url.toLocalFile())
        return str(path.absolute())

    # noinspection PyTypeChecker
    # @Slot(QUrl, result=str)
    # def abs_path_of(self, url: QUrl) -> str:
    #     path = Path(url.toLocalFile())
    #     return str(path.absolute())
    #
    # # noinspection PyTypeChecker
    # @Slot(QUrl, result=str)
    # def stem_of(self, url: QUrl) -> str:
    #     path = Path(url.toLocalFile())
    #     return path.stem
    #
    # # noinspection PyTypeChecker
    # @Slot(QUrl, result=QUrl)
    # def parent_of(self, url: QUrl) -> QUrl:
    #     path = Path(url.toLocalFile()).absolute()
    #     return QUrl.fromLocalFile(path.parent)
    #
    # # noinspection PyTypeChecker
    # @Slot(str, result=QUrl)
    # def url_from_file(self, file: str):
    #     return QUrl.fromLocalFile(file)
    #
    # # noinspection PyTypeChecker
    # @Slot(QUrl, result=bool)
    # def is_existing_file(self, url: QUrl):
    #     path = Path(url.toLocalFile()).absolute()
    #     return path.is_file()

    # @Slot(QUrl, str)
    # def write(self, url: QUrl, content: str):
    #     path = Path(url.toLocalFile())
    #     path.write_text(content, encoding='utf-8')
    #
    # @Slot(str, str)
    # def write_backup(self, video_name: str, content: str):
    #     now = datetime.now()
    #
    #     zip_name = f'{now:%Y-%m}.zip'
    #     zip_path = self._paths.dir_backup / zip_name
    #     zip_mode = "a" if zip_path.exists() else "w"
    #
    #     file_name = f'{now:%Y-%m-%d_%H-%M-%S}_{video_name}.txt'
    #
    #     # noinspection PyTypeChecker
    #     with ZipFile(zip_path, mode=zip_mode, compression=ZIP_DEFLATED) as zip:
    #         zip.writestr(file_name, content)
