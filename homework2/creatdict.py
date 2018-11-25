# -*- coding: utf-8 -*-
"""
Spyder Editor
dgs
This is a temporary script file.
"""

#from textblob import TextBlob
#import nltk
import os
import random
import shutil
import re

TrainDir='C:\\Users\\89304\\Desktop\\trainSample'
TestDir='C:\\Users\\89304\\Desktop\\testSample'

def TrainAndTest(path):#区分训练集与测试集
    allfiles=os.listdir(path)
    for folder in allfiles:
        folderpath=path+'\\'+folder #文件夹路径
        files=os.listdir(folderpath) #文件列表
        num=len(files)
        num=int(num*0.8)  #取整
        trainSample = random.sample(files, num)
        for file in files:
            filepath=path+'\\'+folder+'\\'+file
            if file in trainSample:
                #放入
                copypath=TrainDir+'\\'+folder
            else:
                copypath=TestDir+'\\'+folder
            
            if os.path.exists(copypath) == False:
                os.makedirs(copypath)
            
            #print(filepath)
            shutil.copy(filepath,copypath)
            
path = "C:\\Users\\89304\\Desktop\\20news-18828"
#TrainAndTest(path) 

Dict4ALL={}#大字典
wordnum4ALL=0

#每个文件夹要有一个文件目录
def readfiles(catalog):#为每个文件夹建立词典。不用再为每个文件建立词典，但同样是每个文件夹调用一次。
    global wordnum4ALL
    files=os.listdir(catalog)        
    wordlist={}#每个文件夹的字典，value是单词出现的概率
    wordnum=0 #每个文件夹里的单词数
    #fileslist={}#文件目录，key是文件位置，value是每个文件的字典。（嵌套字典）
    for f in files:
        tmp_path = os.path.join(catalog,f)
        file=open(tmp_path,'rb')#打开文件
        text = file.read().decode('utf-8','ignore')
        textlow = text.lower()
        preword = re.sub('[^a-zA-Z]',' ',textlow)  #去除非字母字符
        preword = [word for word in preword if len(word) >=3 ] #去掉长度小于三的词
        words= preword.split()  # 分词            
        for word in words:
            wordnum+=1
            if word in wordlist:
                wordlist[word]+=1
            else:#如果这个词在本文本首次出现
                wordlist[word]=1#添加进文本的词典
            
            if word in Dict4ALL:#如果大词典中已有，总的出现次数加1
                    Dict4ALL[word]+=1
            else:#如果大词典中没有。添加进大词典
                    Dict4ALL[word]=1
       # fileslist[tmp_path]=wordlist#每个文件夹的字典，value是每个文件的字典。
    
        file.close()#在每个文件的字典建好后，给文件夹建一个字典。字典的value是每个文件的字典
    wordnum4ALL=wordnum4ALL+wordnum
    for key in wordlist:
        wordlist[key]=wordlist[key]/wordnum #字典的value是单词在类中出现的概率       
    return wordlist,wordnum#返回文件夹字典和wordnum。


#建立三个字典，一个是文件夹字典的字典。key是文件夹路径，value是文件夹字典。文件夹字典的key是word，value是word在这个文件夹里出现的概率。
#另一个是文件夹单词数字典。key是文件夹路径，value是文件夹单词数。
#最后一个是大字典。key是单词，value是单词出现的概率。
#总单词数存在前面的 wordnum4ALL里面。
foldersdict={}#文件夹字典
folderwordnum={}#文件夹单词数字典
folderpath='C:\\Users\\89304\\Desktop\\trainSample'
folders=os.listdir(folderpath)
for folder in folders:
    foldersdict[os.path.join(folderpath,folder)],folderwordnum[os.path.join(folderpath,folder)]=readfiles(os.path.join(folderpath,folder))
    #调用了20次CreateDict


#去除低频词和高频词

#把大词典的value改成每个单词出现的概率
keys=Dict4ALL.keys()
for key in keys:
    Dict4ALL[key]=Dict4ALL[key]/wordnum4ALL
    


#输出大词典
def outputDict4ALL():
    writepath='C:\\Users\\89304\\Desktop\\20news-18828\\aaa\\Dict.txt'
    #itemDict=CreateDict.Dict4ALL.items()
    with open(writepath,'w',encoding='utf8') as output:
        output.write(str(Dict4ALL))

#outputDict4ALL()
        
            
            




