# -*- coding: utf-8 -*-
"""
dgs

@author: 89304
"""
import os
import knn

testDSpath='C:\\Users\\89304\\Desktop\\数据集\\20news-bydate\\20news-bydate-test'

def main(catalog):
    files=os.listdir(catalog)
    for file in files:
        tmp_path = os.path.join(catalog,file)
        result=knn.knn(tmp_path)
        print(result)
       
main(testDSpath)
        
      
