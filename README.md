# datamining
#homework for data mining
#dgs

最开始读文件的时候，被编码格式卡住，python2.7的转变编码格式的语句在3.7里不能用

为了只遍历一遍文本，需要在为每个文本建立词典的同时建立总的词典。并且降低循环层数，可以大幅提高运算速度。

为了将文本的词典与文本对应起来，采用了嵌套词典的数据结构。外层词典的key是文档路径，value是文档的字典。

然后现在对建立词典这一步而言，有一个缺陷是每次运行程序都要算一次词典和向量，这使得程序可以对不同的数据集复用，但这其实没有什么意义，对不同的数据集其实总要做一些改变的，因此程序的设计应该更倾向于针对特定数据集，可以有一次计算把词典和VSM都算好存到硬盘上，然后之后的每次运行都可以直接去硬盘取这些数据而不用再算一遍。

选用的数据集是20news-bydate，这个数据集的train和test数据集是分开的，与18828那个不同，所以没有做把数据集按80%和20%分开那一步。

数据集的筛选做的不够。

程序的复用做的不够好。因为想只遍历一次train数据集就同时建好每个文本的词典和总词典，因此在createDict的时候要同时往总词典里添词。而对于test数据集而言，也需要createDict然后计算VSM，但是不能调用之前写的createDict函数，因为那个函数里还有对总词典的操作是不该运行的。这个其实完全是可以复用的。

VSM的tf值在遍历文本建立词典的时候就做好，IDF存在大词典的value里。

