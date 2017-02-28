#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
import os


def run(source, target, quality, formation):
    subprocess.call(["png2atf.exe", "-i", source, "-o", target, "-q", quality, "-c", formation])


def traverse_run(fName, quality, formation):
    if os.path.isfile(fName):
        run(fName, fName, quality, formation)
    else:
        for root, dirs, files in os.walk(fName):
            for name in files:
                if os.path.splitext(name)[1] == ".jpg":
                    path = os.path.join(root, name)
                    run(path, path, quality, formation)


if __name__ == '__main__':
    traverse_run("bg", "0", "DXT5")
