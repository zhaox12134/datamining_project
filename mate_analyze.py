#作者曾经的合作者也是重要的信息，如果他们曾经合作过，则他们很有可能会再次合作，凭借合作过的人，也有利于提高辨识度
#问题是合作者的存储，有两种思路：
#1.按照文章去存储，但查找时候麻烦，但保留了文章信息的框架
#2.按照人名去存储，然后存储其出现次数，问题是可能会出现重名，或者同名的不同写法
#要不然两个都实现算了
import json
from name_compare import name_judge as name_judge
with open("train_pub.json") as file1:
    pub = json.load(file1)
with open("train_author.json") as file2:
    author = json.load(file2)
dict_writer_mate = {} #存储作者的合作者名字列表
for name in author:
    for writer in author[name]:
        for article in author[name][writer]:
            for mate in pub[article]["authors"]:
                if name_judge(name,mate["name"]):
                    pass
                else:
                    if writer not in dict_writer_mate:
                        dict_writer_mate[writer]=[mate["name"],]
                    else:
                        dict_writer_mate[writer].append(mate["name"])
for writer in dict_writer_mate:
    print(writer)
    for mate in dict_writer_mate[writer]:
        print(mate)


