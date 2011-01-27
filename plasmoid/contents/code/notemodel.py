#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2010-2011, Volkan Esgel
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 3 of the License, or (at your option)
# any later version.
#
# Please read the COPYING file.
#

# PyQt4 Section
from PyQt4.QtCore import *

# Application Section
from colors import *
from datamanager import DataManager

(DescriptionRole, ColorRole, RateRole) = range(Qt.UserRole, Qt.UserRole + 3)


class NoteItem:
    def __init__(self, title, description=None, color=None, rate=None):
        self.title = title
        self.description = description
        self.color = color
        self.rate = rate

class NoteModel(QAbstractListModel):
    def __init__(self, package_path, parent=None):
        super(NoteModel, self).__init__(parent)
        self.notes = []

        dm = DataManager(package_path)
        data = dm.getData()

        # load notes from data file
        for line in data:
            title, description, color, rate = line.split('|')
            self.notes.append(NoteItem(title, description, COLORS[color], rate))

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
