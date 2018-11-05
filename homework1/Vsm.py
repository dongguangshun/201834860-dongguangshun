# -*- coding: utf-8 -*-
"""
@author: dgs
"""
import CreateDict
import os
import math
import numpy  as np
#大字典在CreateDict里
#文件夹list在VSM里
#VSM调用了20次 CreateDict
Array4Folder=[]#文件夹字典的list
folderpath='C:\\Users\\89304\\Desktop\\数据集\\20news-bydate\\20news-bydate-train'
#folderpath='C:\\Users\\89304\\Desktop\\数据集\\20news-bydate\\aaa'
folders=os.listdir(folderpath)
for folder in folders:
    Array4Folder.append(CreateDict.readfiles(os.path.join(folderpath,folder)))
    #调用了20次CreateDict

#计算总文件数量。
filesnum=0
for i in range (0,len(Array4Folder)):    
    filesnum+=len(Array4Folder[i])
#把大词典的value改成IDF
print(filesnum)
print(len(CreateDict.Dict4ALL))

keys=CreateDict.Dict4ALL.keys()
for key in keys:
    dft=CreateDict.Dict4ALL[key]
    CreateDict.Dict4ALL[key]=(math.log(filesnum/dft))

DictV=CreateDict.Dict4ALL.values()
DictVector=np.array(DictV)
#大词典构造结束
#再给每个文件建立向量
Vec4All=[]#全部向量的list.元素是文件夹的字典，字典内容是 文件路径：向量
def Vec4Files():
    for folder in Array4Folder:
        Vec4Folder={}
        key4files=folder.keys()#此处key是文件路径
        value4files=folder.values()#此处value是文件的字典，小字典
        for i in range(0,len(folder)):
             Vec4file=[]
             Dictkey=CreateDict.Dict4ALL.keys()
             for j in range(0,len(CreateDict.Dict4ALL)):
                 for key in Dictkey:
                     if key in value4files:
                         Vec4file.append(value4files[key])
                     else:
                         Vec4file.append(0)
             Vec4Folder[key4files]=Vec4file
        Vec4All.append(Vec4Folder)
#Vec4Files()


#输出大词典
def outputDict4ALL():
    writepath='C:\\Users\\89304\\Desktop\\数据集\\20news-bydate\\aaa\\Dict.txt'
    #itemDict=CreateDict.Dict4ALL.items()
    with open(writepath,'w',encoding='utf8') as output:
        output.write(str(CreateDict.Dict4ALL))

#outputDict4ALL()
        
#输出Array4Folder
def outputArray4Folder():
    writepath2='C:\\Users\\89304\\Desktop\\数据集\\20news-bydate\\aaa\\Dict2.txt'
    with open(writepath2,'w',encoding='utf8') as output:
        for i in range(0,20):
            output.write("".join(Array4Folder[i])+'\n')

#outputArray4ALL()

            
            
