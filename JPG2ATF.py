#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Jonny.Hong"

import subprocess
import os


def __run__(source, target, quality, formation):
    subprocess.call(["png2atf.exe", "-i", source, "-o", target, "-q", str(quality), "-c", formation])


def traverse_run(fName, quality=0, formation="DXT5"):
    if os.path.isfile(fName):
        __run__(fName, fName, quality, formation)
    else:
        for root, dirs, files in os.walk(fName):
            for name in files:
                if os.path.splitext(name)[1] == ".jpg":
                    path = os.path.join(root, name)
                    __run__(path, path, quality, formation)


if __name__ == '__main__':
    traverse_run("bg")
