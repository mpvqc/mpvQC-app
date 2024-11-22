/*
mpvQC

Copyright (C) 2022 mpvQC developers

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
*/

import QtQuick
import QtTest

import settings

TestCase {
    id: testCase

    width: 400
    height: 400
    visible: true
    when: windowShown
    name: "MpvqcSubMenuWindowTitle"

    Component {
        id: objectUnderTest

        MpvqcSubMenuWindowTitle {
            mpvqcApplication: QtObject {
                property var mpvqcSettings: QtObject {
                    property var windowTitleFormat: MpvqcSettings.WindowTitleFormat.DEFAULT
                }
            }
        }
    }

    function test_selection() {
        const control = createTemporaryObject(objectUnderTest, testCase);
        verify(control);

        control.defaultFormat.triggered();
        compare(control.mpvqcApplication.mpvqcSettings.windowTitleFormat, MpvqcSettings.WindowTitleFormat.DEFAULT);
        verify(!control.fileNameFormat.checked);
        verify(!control.filePathFormat.checked);

        control.fileNameFormat.triggered();
        compare(control.mpvqcApplication.mpvqcSettings.windowTitleFormat, MpvqcSettings.WindowTitleFormat.FILE_NAME);
        verify(!control.defaultFormat.checked);
        verify(!control.filePathFormat.checked);

        control.filePathFormat.triggered();
        compare(control.mpvqcApplication.mpvqcSettings.windowTitleFormat, MpvqcSettings.WindowTitleFormat.FILE_PATH);
        verify(!control.defaultFormat.checked);
        verify(!control.fileNameFormat.checked);
    }
}
