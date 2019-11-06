#有三分之一的文章没有摘要，难办
#作为分析起来比较复杂的数据，其可信度却并不是很高，亏了
import json
import re
writer_words_dict = {}
#一个存储在内存中的字典，一级字典的关键字是writer_ID,值也是一个字典，关键字是作者文章中出现过的词汇，对应的值是词汇的出现频率
with open("train_author.json") as file1:
    author = json.load(file1)
with open("train_pub.json") as file2:
    pub = json.load(file2)

for name in author:#遍历所有人名
    for writer_ID in author[name]:#对同名的作者进行遍历
        if writer_ID not in writer_words_dict:
            writer_words_dict[writer_ID] = {}
        for article_ID in author[name][writer_ID]:#遍历某一作者的全部著作
            try:
                print("获取到了abstract")
                abstract = pub[article_ID]['abstract']   #获取著作摘要，摘要是信息量最大部分
                abstract_words = re.split('\W+',abstract)#分词
            except:
                abstract_words = []
                print("文章ID:"+article_ID + "缺失abstract")
            for word in abstract_words:#统计，得到作者与词汇频率的字典
                if word not in writer_words_dict[writer_ID]:
                    writer_words_dict[writer_ID][word] = 1
                else:
                    writer_words_dict[writer_ID][word] += 1
def get_n11(this_writer_ID,word):
    if word in writer_words_dict[writer_ID]:
        n11 = writer_words_dict[writer_ID][word]
    else:
        n11 = 0
    return n11
def get_n12(this_writer_ID,name,word):
    n12 = 0
    for writer_ID in author[name]:
        if writer_ID != this_writer_ID:
            if word in writer_words_dict[writer_ID]:
                n12 += writer_words_dict[writer_ID][word]
            else:
                pass
    return n12
def get_n21(this_writer_ID,word):
    n21 = 0
    for other_word in writer_words_dict[this_writer_ID]:
        if other_word != word:
           n21 += writer_words_dict[this_writer_ID][other_word]
    return n21
def get_n22(this_writer_ID,name,word):
    n22 = 0
    for writer_ID in author[name]:
        if writer_ID != this_writer_ID:
            for other_word in writer_words_dict[writer_ID]:
                if other_word != word:
                    n22 += writer_words_dict[writer_ID][other_word]
    return n22
#需要对作者的词汇进行特征分析，使用X^2统计方法为佳，其特征维度与同名作者数量相同
#此处所求的是词汇在同名的不同作者之间的偏向
#数据形式为（V1，V2，V3.....Vn）n为作者数量
def get_n(name): ##计算的是同名作者的词汇出现频率总和
    n = 0
    for writer in author[name]:
        for word in writer_words_dict[writer]:
            n += writer_words_dict[writer][word]
    return n
word_vector_dict = {}
#word_vector_dict--+--name1--+--word1--vector(V1,..,Vn)
#                  |         +--word2--vector(V1,..,Vn)
#                  |
#                  +--name1--+--word1--vector(V1,..,Vn)
#                  |         +--word2--vector(V1,..,Vn)

def get_vector(n,word,name):#对于某一词汇，获取其在不同作者中的偏向，并存入word_vector_dict中
    word_vector = []
    for writer_ID in author[name]:
        n11 = get_n11(writer_ID, word)
        n12 = get_n12(writer_ID, name, word)
        n21 = get_n21(writer_ID, word)
        n22 = get_n22(writer_ID, name, word)
        x2 = (n * (n11 * n22 - n12 * n21) * (n11 * n22 - n12 * n21)) / ((n11 + n12) * (n21 + n22) * (n11 + n21) * (n12 + n22))
        word_vector.append(x2)

for name in author:#开始遍历author字典
    #每次name循环结束以后，得到一个字典，关键字是词汇，值是词汇在同名作者中的偏向
    #不同人名的字典不可混用
    n = get_n(name)
    for writer_ID in name:#对同名作者的词汇情况进行统计
        for word in writer_words_dict[writer_ID]:#对于某一作者拥有的词汇进行分析
            word_vector_dict[name][word] = get_vector(n,word,name)


