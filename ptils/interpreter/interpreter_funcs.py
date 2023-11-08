""" Interpreter utility functions """

import os


def cls():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


clear = cls
