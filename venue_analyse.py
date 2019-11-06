#期刊涵盖了极大的信息，通过比对以进行判断
import json
with open("train_pub.json") as file1:
    pub = json.load(file1)
with open("train_author.json") as file2:
    author = json.load(file2)
dict_writer_venue = {}

def get_venue():
    for name in author:
        for writer in author[name]:
            for article in author[name][writer]:
                try:
                    if writer not in dict_writer_venue:
                        dict_writer_venue[writer]=[pub[article]["venue"],]
                    else:
                        dict_writer_venue[writer].append(pub[article]["venue"])
                except:
                    if "venue" not in pub[article]:
                        print("文章缺少venue字段")
                        pass
                    else:
                        print("其他错误")
get_venue()
for writer in dict_writer_venue:
    print(writer)
    for title in dict_writer_venue[writer]:
        print(title)
#以上只是获取了作者的论文标题信息，还没来得及去重
#而且论文标题的信息过多，包含了不必要的自然语言信息，要按照abstract的处理办法，量化并提取信息
