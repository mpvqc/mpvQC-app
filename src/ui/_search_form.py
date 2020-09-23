# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/search_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SearchForm(object):
    def setupUi(self, SearchForm):
        SearchForm.setObjectName("SearchForm")
        SearchForm.setWindowModality(QtCore.Qt.NonModal)
        SearchForm.resize(890, 34)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SearchForm.sizePolicy().hasHeightForWidth())
        SearchForm.setSizePolicy(sizePolicy)
        SearchForm.setWindowTitle("")
        self.horizontalLayout = QtWidgets.QHBoxLayout(SearchForm)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.searchLineEdit = QtWidgets.QLineEdit(SearchForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchLineEdit.sizePolicy().hasHeightForWidth())
        self.searchLineEdit.setSizePolicy(sizePolicy)
        self.searchLineEdit.setMinimumSize(QtCore.QSize(250, 0))
        self.searchLineEdit.setObjectName("searchLineEdit")
        self.horizontalLayout.addWidget(self.searchLineEdit)
        self.previousButton = QtWidgets.QPushButton(SearchForm)
        self.previousButton.setEnabled(True)
        self.previousButton.setFocusPolicy(QtCore.Qt.NoFocus)
        icon = QtGui.QIcon.fromTheme("go-up")
        self.previousButton.setIcon(icon)
        self.previousButton.setFlat(False)
        self.previousButton.setObjectName("previousButton")
        self.horizontalLayout.addWidget(self.previousButton)
        self.nextButton = QtWidgets.QPushButton(SearchForm)
        self.nextButton.setEnabled(True)
        self.nextButton.setFocusPolicy(QtCore.Qt.NoFocus)
        icon = QtGui.QIcon.fromTheme("go-down")
        self.nextButton.setIcon(icon)
        self.nextButton.setFlat(False)
        self.nextButton.setObjectName("nextButton")
        self.horizontalLayout.addWidget(self.nextButton)
        spacerItem = QtWidgets.QSpacerItem(30, 0, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.searchResultLabel = QtWidgets.QLabel(SearchForm)
        self.searchResultLabel.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchResultLabel.sizePolicy().hasHeightForWidth())
        self.searchResultLabel.setSizePolicy(sizePolicy)
        self.searchResultLabel.setText("")
        self.searchResultLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.searchResultLabel.setObjectName("searchResultLabel")
        self.horizontalLayout.addWidget(self.searchResultLabel)
        self.searchCloseButton = QtWidgets.QPushButton(SearchForm)
        self.searchCloseButton.setFocusPolicy(QtCore.Qt.NoFocus)
        icon = QtGui.QIcon.fromTheme("window-close")
        self.searchCloseButton.setIcon(icon)
        self.searchCloseButton.setFlat(False)
        self.searchCloseButton.setObjectName("searchCloseButton")
        self.horizontalLayout.addWidget(self.searchCloseButton)

        self.retranslateUi(SearchForm)
        QtCore.QMetaObject.connectSlotsByName(SearchForm)

    def retranslateUi(self, SearchForm):
        _translate = QtCore.QCoreApplication.translate
        self.searchLineEdit.setPlaceholderText(_translate("SearchForm", "Find in comments"))
        self.previousButton.setText(_translate("SearchForm", "Previous"))
        self.nextButton.setText(_translate("SearchForm", "Next"))
        self.searchCloseButton.setText(_translate("SearchForm", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SearchForm = QtWidgets.QWidget()
    ui = Ui_SearchForm()
    ui.setupUi(SearchForm)
    SearchForm.show()
    sys.exit(app.exec_())
