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

from mpvqc.services import ResourceService, ApplicationEnvironmentService, ApplicationPathsService, BackupService, \
    FileStartupService, PlayerService, ResourceReaderService, ReverseTranslatorService


def bindings(binder: inject.Binder):
    binder.bind_to_constructor(ApplicationEnvironmentService, lambda: ApplicationEnvironmentService())
    binder.bind_to_constructor(ApplicationPathsService, lambda: ApplicationPathsService())
    binder.bind_to_constructor(BackupService, lambda: BackupService())
    binder.bind_to_constructor(FileStartupService, lambda: FileStartupService())
    binder.bind_to_constructor(PlayerService, lambda: PlayerService())
    binder.bind_to_constructor(ResourceService, lambda: ResourceService())
    binder.bind_to_constructor(ResourceReaderService, lambda: ResourceReaderService())
    binder.bind_to_constructor(ReverseTranslatorService, lambda: ReverseTranslatorService())


def configure_injections():
    inject.configure(bindings, bind_in_runtime=False)