#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Jonny.Hong"

import os
import hashlib
import json
import zlib

md5Dic = {}
FILE_COUNT = 0


def record_md5():
    with open("md5.txt", "wb+") as f:
        md5Str = json.dumps(md5Dic).encode("utf-8")
        md5Str = zlib.compress(md5Str)
        f.write(md5Str)


def traverse_calc(fName):
    if os.path.isfile(fName):
        calc(fName)
    else:
        for root, dirs, files in os.walk(fName):
            for name in files:
                path = os.path.join(root, name)
                calc(path)


def calc(fName):
    global FILE_COUNT
    FILE_COUNT += 1
    eachF = open(fName, "rb")
    md5 = calc_md5(eachF.read())
    nameSplit = fName.split("assets")
    md5Dic["\\assets" + nameSplit[len(nameSplit)-1]] = md5
    print("\\assets" + nameSplit[len(nameSplit)-1] + " : " + md5)


def calc_md5(context):
    m2 = hashlib.md5()
    m2.update(context)
    return m2.hexdigest()


def run(path):
    print("开始解析 " + path)
    traverse_calc(path)
    record_md5()
    print("解析完成 文件个数:" + str(path))
