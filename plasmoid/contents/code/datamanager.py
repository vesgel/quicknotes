#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2011, Volkan Esgel
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 3 of the License, or (at your option)
# any later version.
#
# Please read the COPYING file.
#

import os

class DataManager:
    def __init__(self, package_path):
        self.datafile = "%scontents/data/data.txt" % (package_path)
        self.data = {}
        self.items = []

        self.__checkDataFile()

    def __checkDataFile(self):
        if not os.path.exists(self.datafile):
            # data file does not exist, create an empty data file
            file = open(self.datafile, 'w')
            file.close()
            print "Data file does not exist. An empty data file is created!"
        else:
            print "Data file is found and ready for usage."

    def getData(self):
        try:
            f = open(self.datafile, 'r')
            data = f.readlines()
            f.close()

            for i in range(len(data)):
                data[i] = data[i].strip('\n')

            return data

        except:
            print "Error on reading data file!"
