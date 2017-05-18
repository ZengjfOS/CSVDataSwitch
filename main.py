# -*- coding: utf-8 -*-  

'''
Description：
    1. 所有的csv文件都在input目录下；
    2. 从csv文件读去Serial Number、Dark Bad Pixels、Dark Long Bad Pixels字段内容；
    3. 将读取去的相关内容写入ouput.csv文件中；
    4. output.csv文件中，每一行代表对应Serial Number、Dark Bad Pixels、Dark Long Bad Pixels对应的值。
    5. Serial Number、Dark Bad Pixels、Dark Long Bad Pixels字段放在config.ini文件内部，output输出行的顺序也是依照这个顺序

Author：曾剑锋
Date：2017-05-17
'''

import sys
import csv
import configparser
from os import walk

'''
获取所有需要处理csv文件
'''
def getCSVFiles() :

    f = []
    for (dirpath, dirnames, filenames) in walk("input") :
        f.extend(filenames)

    print(f)

    return f

'''
检查当前行里是否有需要的列值
'''
def getValueFromRow(row, header, columnWithVals, config) :

    for column in header :

        if column.strip() in row :
            valueColumn = config[column]["valueColumn"]
            columnIndex = 0

            if valueColumn == None or len(valueColumn) == 0 or int(valueColumn) < 2 :
                columnIndex = 0
            else :
                columnIndex = int(valueColumn) - 1

            if len(row[columnIndex].strip()) != 0 :
                columnWithVals[column.strip()] = row[columnIndex].strip()
                return row[columnIndex].strip()

    return None

'''
获取当前文件中所有的row，对每行数据进行对比，见最后输出的结果输出到output.csv文件中
'''
def dealCSVFile(inputFile, output, outputHeader, config) :

    outputRow = []
    columnWithVals = {}

    # remove header before deal data
    inputHeader = next(inputFile)

    for row in inputFile :
        if (len(row) >= 2) :

            # get values in dict
            getValueFromRow(row, outputHeader, columnWithVals, config)

    # order all vaule by outputHeader order
    for column in outputHeader :
        outputRow.append(columnWithVals[column])

    # write to output file
    output.writerow(outputRow)

'''
主线程处理函数
'''
def main(argv=None) :

    # get all csv file
    csvFiles = getCSVFiles()

    # create output.csv file and get a csv writer
    csv_output = open('output.csv','w')
    outputCSVWriter = csv.writer(csv_output, delimiter=',', lineterminator='\n')

    # get output csv header from config.ini file
    config = configparser.ConfigParser()
    config.read("config.ini")

    outputHeader = config.sections()
    if (outputHeader == None) :
        return
    outputCSVWriter.writerow(outputHeader)

    for inputFile in csvFiles:
        csv_input = open("input/" + inputFile)
        inputCSVReader = csv.reader(csv_input)

        dealCSVFile(inputCSVReader, outputCSVWriter, outputHeader, config)

        csv_input.flush()
        csv_input.close()

    csv_output.flush()
    csv_output.close()

if __name__ == "__main__" :
    sys.exit(main())
