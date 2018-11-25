# -*- coding: utf-8 -*-
"""
dgs

@author: 89304
"""
import os
import NBC

testDSpath='C:\\Users\\89304\\Desktop\\testSample'

def main(catalog):#遍历一遍test数据集，送入NBC，并打印结果。
    folders=os.listdir(catalog)
    for folder in folders:
        tmp_path= os.path.join(catalog,folder)
        files=os.listdir(folder)
        for file in files:
            filepath=os.path.join(tmp_path,file)
            belongfolder=NBC.NBC(filepath)
            print(belongfolder)
main(testDSpath)
        