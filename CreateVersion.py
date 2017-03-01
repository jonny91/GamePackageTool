#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Jonny.Hong"

import zlib
import json
import os
import CreateMD5

md5Dic = {}
versionDic = {}

def __checkMD5__():
    global versionDic
    global md5Dic
    currentMD5Dic = CreateMD5.md5Dic
    for each in currentMD5Dic:
        if each in versionDic:
            if md5Dic[each] != currentMD5Dic[each]:
                versionDic[each] += 1
        else:
            versionDic[each] = 0

def __readMD5File__():
    global md5Dic
    if os.path.exists("md5.txt"):
        with open("md5.txt", "rb+") as f:
            ba = f.read()
            ba = zlib.decompress(ba)
            ba = bytes(ba).decode()
            md5Dic = json.loads(ba)


def __readVersionFile__():
    global versionDic
    if os.path.exists("version.dat"):
        with open("version.dat", "rb+") as f:
            ba = f.read()
            ba = zlib.decompress(ba)
            ba = bytes(ba).decode()
            versionDic = json.loads(ba)

def __createVersionFile__():
    global versionDic
    with open("version.dat", "wb+") as f:
        versionStr = json.dumps(versionDic).encode("utf-8")
        versionStr = zlib.compress(versionStr)
        f.write(versionStr)

def run(floderOrFileName):
    __readMD5File__()
    __readVersionFile__()

    CreateMD5.traverse_calc(floderOrFileName)
    CreateMD5.record_md5()

    __checkMD5__()
    __createVersionFile__()