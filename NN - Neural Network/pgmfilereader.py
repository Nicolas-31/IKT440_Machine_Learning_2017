#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 22:47:11 2017
pgmfilereader.py
pgm file
header:
P5

32 30

156
This means Width=32, Height=30, Depth=156? is two bytes (using uint16)
https://stackoverflow.com/questions/35723865/read-a-pgm-file-in-python
https://stackoverflow.com/questions/7368739/numpy-and-16-bit-pgm
@author: eivind
"""
import numpy as np


class PgmFileReader:
    pathname = ""

    def __init__(self, pathname):
        self.pathname = pathname

    def open(self, filename):
        file = self.pathname + filename
        data = open(file, "rb")
        fileformat = data.readline()
        # print("Fileformat:", fileformat)
        (width, height) = [int(i) for i in data.readline().split()]
        # print("Width Height:", width, height)
        depth = data.readline()
        # print("Depth", depth)
        # arrlen = width*height

        image = np.fromfile(data, dtype=np.uint8)
        # print("****************************")
        # print(image.shape)
        # We get an matrix 960X1 bytes
        return np.array(image)
