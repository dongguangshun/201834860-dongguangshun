# -*- coding: utf-8 -*-
"""
@author: 董广顺
"""
import re
import creatdict


#NBC这里是给一个file，对其做分类。
testDSpath=creatdict.TestDir

def NBC(file):
    pfolders=0 #属于某个文件夹的概率。取最大的一个
    belongfolder=''
    f=open(file,'rb')
    text = f.read().decode('utf-8','ignore')
    textlow = text.lower()
    preword = re.sub('[^a-zA-Z]',' ',textlow)  #去除非字母字符
    preword = [word for word in preword if len(word) >=3 ] #去掉长度小于三的词
    words= preword.split()  # 分词     
    for key in creatdict.foldersdict:
        dict=creatdict.foldersdict[key]
        wordkey=dict.keys()
        wordkey4ALL=creatdict.Dict4ALL.keys()
        pfolder=1
        for word in words:
            if word in wordkey:
                pword=dict[word]
            else:
                pword=1/creatdict.folderwordnum[key]
                
            if word in wordkey4ALL:
                pword4ALL=creatdict.Dict4ALL[word]
            else:
                pword4ALL=1/creatdict.wordnum4ALL
            
            pfolder*=pword
            pfolder=pfolder/pword4ALL
        
        pfolder=pfolder*creatdict.folderwordnum[key]/creatdict.wordnum4ALL
        #前面算好了测试样本属于某文件夹的概率，下面求最大的那个
        if pfolder>pfolders:
            global belongfolder
            belongfolder=key
    return belongfolder
