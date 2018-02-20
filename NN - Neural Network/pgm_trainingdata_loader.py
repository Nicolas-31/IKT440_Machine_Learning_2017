#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 09:51:09 2017

@author: eivind
"""
from os import listdir
from os.path import isfile, join
from pgmfilereader import PgmFileReader
import numpy as np


def load_verification_bamboo(path):
    path = path + "/"
    fr = PgmFileReader(path)
    files = [f for f in listdir(path) if isfile(join(path, f))]

    verification_data = []

    for file in files:
        image = fr.open(file)
        reshaped = np.reshape(image, (960, 1))

        verification_data.append((reshaped, file))

    return verification_data


def load_data():
    path = "training_data/"
    fr = PgmFileReader(path)
    files = [f for f in listdir(path) if isfile(join(path, f))]
    trainingfiles = files  # [0:450]
    validationfiles = files[-50:]
    verificationfiles = files[-50:]
    training_data = []
    validation_data = []
    verification_data = []
    for file in trainingfiles:
        # print(file)
        image = fr.open(file)
        reshaped = np.reshape(image, (960, 1))
        t = (reshaped, vectorized_result(file))
        training_data.append(t)

    for file in validationfiles:
        print(file)
        image = fr.open(file)
        reshaped = np.reshape(image, (960, 1))
        t = (reshaped, get_directionindex(get_direction(file)))
        validation_data.append(t)

    for file in verificationfiles:
        # print(file)
        image = fr.open(file)
        reshaped = np.reshape(image, (960, 1))

        verification_data.append((reshaped, file))

    return (training_data, validation_data, verification_data)


def vectorized_result(filename):
    # e = np.zeros((4, 1))
    e = np.full((4, 1), 0)
    index = get_directionindex(get_direction(filename))

    e[index] = 1
    return e


# takes a filename as input
# returns the direction indicated by the filename
# Example: "kawamura_left_angry_sunglasses_4" will return "left"
def get_direction(filename):
    i = filename.index("_") + 1
    filename = filename[i:]
    j = filename.index("_")
    f = filename[:j]
    return f


def get_directionindex(direction):
    if direction == "left":
        return 0
    elif direction == "right":
        return 1
    elif direction == "up":
        return 2
    else:  # "straight" in file:
        return 3
