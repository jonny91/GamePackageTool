#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Jonny.Hong"

import CreateMD5
import JPG2ATF
import CreateVersion

if __name__ == '__main__':
    path = r"E:\adventure\assets"
    JPG2ATF.traverse_run("bg")
    CreateMD5.run(path)
    CreateVersion.run()
