# -*- coding: utf-8 -*-
"""
@author: 董广顺
"""
import re
import CreateDict
import Vsm
import numpy  as np

#KNN这里是给一个file，对其做分类。

#为每一个file建立一个向量，然后进行KNN计算，最后返回属于哪个文件夹
def knn(file):#此处的file是文件路径
    Vector=[]#文本的向量
    wordlist={}#文本的词典
    f=open(file,'rb')
    text = f.read().decode('utf-8','ignore')
    textlow = text.lower()
    preword = re.sub('[^a-zA-Z]',' ',textlow)  #去除非字母字符
    words= preword.split()  # 分词        
    for word in words:#构建文本的词典
        if word in wordlist:
            wordlist[word]+=1
        else:#如果这个词在本文本首次出现
            wordlist[word]=1#添加进文本的词典
    
    key4file=wordlist.keys()
    Dictkey=CreateDict.Dict4ALL.keys()
    for i in range(0,len(CreateDict.Dict4ALL)):#构建文本的向量
        for key in Dictkey:
            if key in key4file:
                Vector.append(wordlist[key])
            else:
                Vector.append(0)

    #向量构建完了，现在要计算KNN了。
    #公式是   cos=(A*B)/(|A|*|B|) 模：根号[(x1-Y1)^2+(x2-Y2)^2]
    #cos越大角度越小
    knnresult=[]#存结果
    knnpath=[]#存路径
    knnnum=30 #取多少个邻居
    a_pre=np.array(Vector)#将list转成向量数组 
    a=np.multiply(a_pre,Vsm.DictVector)
    lx=np.sqrt(a.dot(a))
    for i in range(0,len(Vsm.Vec4All)):
        key=Vsm.Vec4All[i].keys()
        value=Vsm.Vec4All[i].values()
        b_pre=np.array(value)
        b=np.multiply(b_pre,Vsm.DictVector)
        ly=np.sqrt(b.dot(b))
        cos_angle=a.dot(b)/(lx*ly)
        if abs(cos_angle)>min(knnresult):
           n=knnresult.index(min(knnresult))#knn结果中最小值所在位置，准备被替换
           del knnresult[n]
           del knnpath[n]#删除
           knnresult.append(abs(cos_angle))
           knnpath.append(key)            
        elif len(knnresult<knnnum):
            knnresult.append(abs(cos_angle))
            knnpath.append(key)
    #knn计算结束。result里数据不重要了。knnpath里存的是里的最近的knnnum个邻居的路径
    #现在由这个路径来计算送入knn的文本属于哪个文件夹
    for i in range(0,knnnum):
        k=knnpath[i].rindex('\\')#把路径最后的文件名去掉，就只剩文件夹名了
        knnpath[i]=knnpath[i][:k]
    
    #找到list中出现次数最多的那个元素，元素本身就是文件夹的路径，返回这个路径就好了
    max=0
    pathno=0
    for i in range(0,knnnum):
        temp=knnpath.count(knnpath[i])
        if temp>max:
            max=temp
            pathno=i
    return knnpath[pathno]#返回文件路径
 
