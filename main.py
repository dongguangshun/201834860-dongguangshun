# -*- coding: utf-8 -*-
"""
dgs

@author: 89304
"""
import os
import knn

testDSpath='C:\\Users\\89304\\Desktop\\数据集\\20news-bydate\\20news-bydate-test'

def main(catalog):#遍历一遍test数据集，送入knn，并打印结果。
    folders=os.listdir(catalog)
    for folder in folders:
        tmp_path= os.path.join(catalog,folder)
        if (os.path.isdir(tmp_path)):
            main(tmp_path)
        else:
            result=knn.knn(tmp_path)
            print(result)
main(testDSpath)
        
      
