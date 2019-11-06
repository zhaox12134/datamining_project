#关键字是一篇文章内容的精髓，涵盖了比abstract更简洁有效的信息，通过关键字比对，可以较好地进行归类
import json
with open("train_pub.json") as file1:
    pub = json.load(file1)
with open("train_author.json") as file2:
    author = json.load(file2)
dict_writer_key = {}
def get_keywords():
    for name in author:
        for writer in author[name]:
            for article in author[name][writer]:
                try:
                    if writer not in dict_writer_key:
                        dict_writer_key[writer]=pub[article]["keywords"]
                    else:
                        dict_writer_key[writer].extend(pub[article]["keywords"])
                except:
                    if "keywords" not in pub[article]:
                        print("文章缺少keywords字段")
                        pass
                    else:
                        print("其他错误")
get_keywords()
for writer in dict_writer_key:
    print(writer)
    print(dict_writer_key[writer])
#获取以后，应该是采用最近邻算法，比对论文相似度最高的