#文章标题同样涵盖了极大的信息，通过比对以进行判断
import json
with open("train_pub.json") as file1:
    pub = json.load(file1)
with open("train_author.json") as file2:
    author = json.load(file2)
dict_writer_title = {}

def get_title():
    for name in author:
        for writer in author[name]:
            for article in author[name][writer]:
                try:
                    if writer not in dict_writer_title:
                        dict_writer_title[writer]=[pub[article]["title"],]
                    else:
                        dict_writer_title[writer].append(pub[article]["title"])
                except:
                    if "title" not in pub[article]:
                        print("文章缺少title字段")
                        pass
                    else:
                        print("其他错误")
get_title()
for writer in dict_writer_title:
    print(writer)
    for title in dict_writer_title[writer]:
        print(title)
#以上只是获取了作者的论文标题信息，还没来得及去重
#而且论文标题的信息过多，包含了不必要的自然语言信息，要按照abstract的处理办法，量化并提取信息
