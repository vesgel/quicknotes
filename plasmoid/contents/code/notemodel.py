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

from PyQt4.QtCore import *
from colors import *

(DescriptionRole, ColorRole, RateRole) = range(Qt.UserRole, Qt.UserRole + 3)


class NoteItem:
    def __init__(self, title, description=None, color=None, rate=None):
        self.title = title
        self.description = description
        self.color = color
        self.rate = rate

class NoteModel(QAbstractListModel):
    def __init__(self, parent=None):
        super(NoteModel, self).__init__(parent)
        self.notes = []

        for i in range(0, 4):
            note = NoteItem("Note %s" % i, "Description")
            self.notes.append(note)
        self.notes[0].color = YELLOW
        self.notes[1].color = BLUE
        self.notes[2].color = GRAY
        self.notes[3].color = BROWN
        self.notes[0].rate = 1
        self.notes[1].rate = 2
        self.notes[2].rate = 3
        self.notes[3].rate = 4

    def rowCount(self, parent=QModelIndex()):
        return len(self.notes)

    def data(self, index, role):
        if not index.isValid():
            return QVariant()

        if role == Qt.DisplayRole:
            return QVariant(self.notes[index.row()].title)

        if role == ColorRole:
            return QVariant(self.notes[index.row()].color)
        elif role == DescriptionRole:
            return QVariant(self.notes[index.row()].description)
        elif role == RateRole:
            return QVariant(self.notes[index.row()].rate)
