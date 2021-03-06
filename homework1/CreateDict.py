# -*- coding: utf-8 -*-
"""
Spyder Editor
    董广顺
"""

#from textblob import TextBlob
#import nltk
import os
import re

Dict4ALL={}#大字典
#Array4Folder=[]#文件夹字典的list
trainDSpath = 'C:\\Users\\89304\\Desktop\\数据集\\20news-bydate\\20news-bydate-train'
#建立文档目录并建立文档的小词典，同时建立大词典？
#每个文件夹要有一个文件目录
def readfiles(catalog):#为每个文件夹建立文件目录，也就是还要有一个遍历，调用20次这个函数
    files=os.listdir(catalog)
    fileslist={}#文件目录，key是文件位置，value是每个文件的字典。（嵌套字典）
    for f in files:
        #dict4everyfile={}
        wordlist={}#每个文件的字典，value是TF值
        tmp_path = os.path.join(catalog,f)
        file=open(tmp_path,'rb')#打开文件
        text = file.read().decode('utf-8','ignore')
        textlow = text.lower()
        preword = re.sub('[^a-zA-Z]',' ',textlow)  #去除非字母字符
        words= preword.split()  # 分词            
        for word in words:
            if word in wordlist:
                wordlist[word]+=1
            else:#如果这个词在本文本首次出现
                wordlist[word]=1#添加进文本的词典
                if word in Dict4ALL:#如果大词典中已有，IDF值加1
                    Dict4ALL[word]+=1
                else:#如果大词典中没有。添加进大词典
                    Dict4ALL[word]=1
        fileslist[tmp_path]=wordlist#每个文件夹的字典，value是每个文件的字典。
    
        file.close()#在每个文件的字典建好后，给文件夹建一个字典。字典的value是每个文件的字典
    #Array4Folder.append(fileslist)#这个list的元素是文件夹的字典
    return fileslist#返回一个字典。
if __name__ == '__main__':
    readfiles(trainDSpath)
    
'''import sys
import imp
imp.reload(sys)
sys.setdefaultencoding('utf-8')'''




''' preword = [word for word in preword if len(word) >=3 ] #去掉长度小于三的词
preword = TextBlob.WordList(preword).singularize()  # 复数变单数
preword = [word.lemmatize('v') for word in preword ]  #过去式、进行时变一般形式
preword = [word for word in preword if word not in  stoplists] #删除stoplists当中的单词
'''


