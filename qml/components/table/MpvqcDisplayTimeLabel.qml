/*
mpvQC

Copyright (C) 2022 mpvQC developers

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
*/


import QtQuick
import QtQuick.Controls
import helpers


Label {
    id: control
    text: MpvqcTimeFormatUtils.formatTimeToString(control.time)
    horizontalAlignment: Text.AlignHCenter
    verticalAlignment: Text.AlignVCenter

    property int time
    property bool itemSelected

    signal clicked()
    signal edited(int time)

    MouseArea {
        anchors.fill: parent

        onClicked: {
            if (itemSelected) {
                startEditing()
            } else {
                triggerClicked()
            }
        }
    }

    function startEditing() {
        requestVideoPause()
        jumpToVideoPosition(control.time)
        openTimeEditPopup()
    }

    function requestVideoPause() {
        eventRegistry.produce(eventRegistry.EventRequestVideoPause)
    }

    function jumpToVideoPosition(time) {
        eventRegistry.produce(eventRegistry.EventJumpToVideoPosition, time)
    }

    function openTimeEditPopup(event) {
        const component = Qt.createComponent("MpvqcEditTimePopup.qml")
        const popup = component.createObject(control)
        popup.currentTime = control.time
        popup.edited.connect(control.triggerTimeEdited)
        popup.editingAborted.connect(control.resetVideoPosition)
        popup.valueChanged.connect(control.jumpToVideoPosition)
        popup.closed.connect(popup.destroy)
        if (LayoutMirroring.enabled) {
            // fixme? workaround popup opening to the right
            popup.x = -(control.width / 2)
        }
        popup.open()
    }

    function resetVideoPosition() {
        control.jumpToVideoPosition(control.time)
    }

    function triggerTimeEdited(time) {
        control.edited(time)
    }

    function triggerClicked() {
        control.clicked()
    }

}