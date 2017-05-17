# -*- coding: utf-8 -*-  

'''
Description：
    1. 所有的csv文件都在input目录下；
    2. 从csv文件读去Serial Number、Dark Bad Pixels、Dark Long Bad Pixels字段内容；
    3. 将读取去的相关内容写入ouput.csv文件中；
    4. output.csv文件中，没一行代表对应Serial Number、Dark Bad Pixels、Dark Long Bad Pixels对应的值。

Author：曾剑锋
Date：2017-05-17
'''

import sys
import getopt
import csv
from os import walk


def getCSVFiles():

    f = []
    for (dirpath, dirnames, filenames) in walk("input"):
        f.extend(filenames)

    print(f)

    return f

def dealCSVFile(inputFile, output):

    outputRow = []

    # data row number was: 11
    for i in range(10):
        row = next(inputFile)

    # get serial number
    row = next(inputFile)
    outputRow.append(row[1])

    # data row number was: 39
    for i in range(38 - 11):
        row = next(inputFile)

    row = next(inputFile)
    outputRow.append(row[1])

    row = next(inputFile)
    outputRow.append(row[1])

    output.writerow(outputRow)

def main(argv=None):

    csvFiles = getCSVFiles()

    csv_output = open('output.csv','w')
    outputCSVWriter = csv.writer(csv_output, delimiter=',', lineterminator='\n')
    outputCSVWriter.writerow(["Serial Number", "Dark Bad Pixels", "Dark Long Bad Pixels"])

    for inputFile in csvFiles:
        csv_input = open("input/" + inputFile)
        inputCSVReader = csv.reader(csv_input)
        dealCSVFile(inputCSVReader, outputCSVWriter)

if __name__ == "__main__":
    sys.exit(main())
