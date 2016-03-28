#!/usr/bin/env python
# -*- coding: <encoding name> -*-

"""Insert module docstring here."""

import os
from PySide import QtGui

__author__ = "Sebastian Roll"

class FileDialogCellWidget(QtGui.QWidget):
    def __init__(self):
        super(FileDialogCellWidget, self).__init__()
        layout = QtGui.QHBoxLayout()

        filebutton = QtGui.QPushButton()
        docOpen = QtGui.QIcon.fromTheme("document-open")
        filebutton.setIcon(docOpen)
        filebutton.setFixedWidth(50)
        self.label = QtGui.QLabel("<- File path")
        layout.addWidget(filebutton)
        layout.addWidget(self.label)
        filebutton.clicked.connect(self.fileDialog)

        self.setLayout(layout)

    def fileDialog(self):
        filePath = QtGui.QFileDialog.getOpenFileName(self, ("Open File"), ".", ("Files (*.csv *.xml)"))
        basepath, filename = os.path.split(filePath[0])

        self.label.setText(filename)

