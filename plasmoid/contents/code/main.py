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
from PyQt4.QtCore import *
from PyQt4.QtGui import *

# PyKDE4 Section
from PyKDE4.plasma import Plasma
from PyKDE4 import plasmascript

# Application Section
from notemodel import NoteModel
from notedelegate import NoteDelegate


class QuickNotes(plasmascript.Applet):

    def __init__(self, parent, args=None):
        plasmascript.Applet.__init__(self, parent)

    def init(self):
        self.setHasConfigurationInterface(True)
        self.setAspectRatioMode(Plasma.IgnoreAspectRatio)

        """
        self.theme = Plasma.Svg(self)
        self.theme.setImagePath("widgets/background")
        self.setBackgroundHints(Plasma.Applet.DefaultBackground)
        """

        self.setBackgroundHints(Plasma.Applet.NoBackground)

        self.__createMainLayout()

        width = self.viewerSize.width() + 20
        height = self.viewerSize.height() - 20
        self.resize(width, height)

    def __createMainLayout(self):
        self.mainLayout = QGraphicsLinearLayout(Qt.Vertical, self.applet)

        noteview = Plasma.TreeView(self.applet)
        noteview.setStyleSheet("QTreeView { background: Transparent }")
        nmodel = NoteModel(noteview)
        noteview.setModel(nmodel)
        noteview.nativeWidget().setItemDelegate(NoteDelegate(self))
        noteview.nativeWidget().setHeaderHidden(True)
        noteview.nativeWidget().setIndentation(0)
        self.mainLayout.addItem(noteview)

        self.viewerSize = noteview.size()

        self.applet.setLayout(self.mainLayout)

def CreateApplet(parent):
    return QuickNotes(parent)
