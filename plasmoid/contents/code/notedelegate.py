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


# Module Variables
ITEM_PADDING = 6


class NoteDelegate(QtGui.QStyledItemDelegate):

    def __init__(self, parent=None):
        super(NoteDelegate, self).__init__(parent)

        # Font Definitions
        self.font = QtGui.qApp.font().toString().split(',')[0]

        self.titleFont = QtGui.QFont(self.font, 9, QtGui.QFont.Bold)
        self.descriptionFont = QtGui.QFont(self.font, 9, QtGui.QFont.Normal)
        self.rateFont = QtGui.QFont(self.font, 8, QtGui.QFont.Normal)

        # Font Metrics
        self.titleFontFM = QtGui.QFontMetrics(self.titleFont)
        self.descriptionFontFM = QtGui.QFontMetrics(self.descriptionFont)

    def sizeHint(self, option, index):
        if index.column() == 0:
            return QSize(0, 50)

    def paint(self, painter, option, index):
        if not index.isValid():
            return super(NoteDelegate, self).paint(painter, option, index)

        topLeft = option.rect.topLeft()
        topRight = option.rect.topRight()
        bottomRight = option.rect.bottomRight()
        bottomLeft = option.rect.bottomLeft()

        x = option.rect.x() + ITEM_PADDING
        y = option.rect.y() + ITEM_PADDING
        width = option.rect.width() - ITEM_PADDING
        height = option.rect.height() - ITEM_PADDING

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
        painter.drawLine(QPointF(bottomRight), QPointF(bottomLeft))

        # Draw Title
        painter.setPen(QtGui.QPen(Qt.black))
        value = index.data(Qt.DisplayRole)
        if value.isValid():
            text = value.toString()
            painter.setFont(self.titleFont)
            painter.drawText(x, y, width, height, Qt.AlignLeft, text)
            titleRect = self.titleFontFM.boundingRect(option.rect, Qt.TextWordWrap, text)

        # Draw Description
        value = index.data(DescriptionRole)
        if value.isValid():
            text = value.toString()
            painter.setFont(self.descriptionFont)
            top = titleRect.height()
            painter.drawText(x + 2, y + top, width, height - top, Qt.AlignLeft, text)

        # Draw Rate
        value = index.data(RateRole)
        if value.isValid():
            rate = value.toInt()[0]
            painter.setFont(self.rateFont)
            painter.setPen(QtGui.QColor("#edf5ff"))
            for i in range(1, 6):
                if i <= rate:
                    painter.setBrush(QtGui.QColor(Qt.red))
                else:
                    painter.setBrush(QtGui.QColor(Qt.gray))
                painter.drawRoundRect(bottomRight.x() - ITEM_PADDING - 12, y + 4 + (i-1)*6, 10, 3, 10, 10)

        painter.restore()
