#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2010, Volkan Esgel
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 3 of the License, or (at your option)
# any later version.
#
# Please read the COPYING file.
#

# PyQt4 Section
from PyQt4 import QtGui
from PyQt4.QtCore import *

# Application Section
from notemodel import *


class NoteDelegate(QtGui.QStyledItemDelegate):

    def __init__(self, parent=None):
        super(NoteDelegate, self).__init__(parent)

    def sizeHint(self, option, index):
        return QSize(0, 40)

    def paint(self, painter, option, index):
        if not index.isValid():
            return super(NoteDelegate, self).paint(painter, option, index)

        topLeft = option.rect.topLeft()
        bottomLeft = option.rect.bottomLeft()

        painter.save()

        painter.setRenderHint(QtGui.QPainter.Antialiasing, True)

        # Fill Row with Note Color
        value = index.data(ColorRole)
        if value.isValid():
            color = value.toList()
            lightHue = QtGui.QColor(color[0].toString())
            darkHue = QtGui.QColor(color[1].toString())

            gradient = QtGui.QLinearGradient(QPointF(topLeft), QPointF(bottomLeft))
            gradient.setColorAt(0, lightHue)
            gradient.setColorAt(1, darkHue)

            painter.fillRect(option.rect, gradient)

        # Draw Line to Seperate Rows
        pen = QtGui.QPen(Qt.black, 1, Qt.SolidLine)
        painter.setPen(pen)
        painter.drawLine(QPointF(option.rect.bottomRight()), QPointF(bottomLeft))

        # Draw Title
        painter.setPen(QtGui.QPen(Qt.black))
        value = index.data(Qt.DisplayRole)
        if value.isValid():
            text = value.toString()
            painter.drawText(option.rect, Qt.AlignLeft, text)

        painter.restore()
