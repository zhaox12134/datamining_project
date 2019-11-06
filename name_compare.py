#把名字处理的一些功能函数放到这里，供调用
import re

def replace(word):#去除"_"
    a=""
    for i in range(word.__len__()):

        if word[i] == "_":
            a=a+" "
        else:
            a=a+word[i]
    return a
def delet_dot(word):#去除 "."
    a=""
    for char in word:
        if(char!="."):
            a+=char
        else:
            a+=" "
    return a
def name_judge(word1,word2):#将pub中的名字与author中的名字归一化,并进行判断
    '''word1 是author中的名字，带有“_”,word2 是pub中的名字'''
    #word1_orgin = word1
    #word2_orgin = word2
    word1 = replace(word1).lower()
    word2 = delet_dot(word2).lower()
    flag1 = True
    flag2 = True
    if(word1==word2): ##第一种情况，二者完全相等
        return True
    else:
        word2_s = re.split('\W+',word2)
        word1_s = re.split('\W+',word1)
        for word in word2_s:  #或者名字是子集，比如 张三zhangsan————zhangsan  或者 姓和名次序被打乱 zhang san———— san zhang
            if word in word1_s:
                pass
            else:
                flag1 = False
        for word in word1_s:
            if word in word2_s:
                pass
            else:
                flag2 = False
        return (flag1 or flag2)
