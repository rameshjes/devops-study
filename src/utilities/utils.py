import string

import numpy as np


def add(x, y):

    return x + y


def subtract(x, y):

    return x - y


def return_string(data):

    return data


def remove_spaces(x):

    return str(x).replace(" ", "")


def remove_punctuations(text):

    text = str(text)
    table = text.maketrans("", "", string.punctuation)
    return text.translate(table)


def create_array(d):

    return np.array(d)
