#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import hashlib
import json
import struct

md5Dic = {}
FILE_COUNT = 0


def record_md5():
    with open("md5.txt", "w+") as f:
        json.dump(md5Dic, f)


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
    md5Dic[fName] = md5
    print(fName + " : " + md5)


def calc_md5(context):
    m2 = hashlib.md5()
    m2.update(context)
    return m2.hexdigest()


if __name__ == '__main__':
    floderOrFileName = r"E:\adventure\assets"
    print("开始解析 " + floderOrFileName)
    traverse_calc(floderOrFileName)
    record_md5()
    print("解析完成 文件个数:" + str(FILE_COUNT))
