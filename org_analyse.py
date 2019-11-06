#对作者的组织机构进行分析
#机构包含了作者的身份信息，同一机构的同一名字作者是同一个人的几率非常高
#先检查一下同一作者的机构是否发生了变化，变化应该是与时间相关
#检查一下同一机构是否有同名作者
#考虑到作者很有可能会变化机构，但机构之间的名字可能有极大关联（专业、大学）
#对机构的可信度设置变化的权重，当机构名字完全一样时，权重增大；不完全一样时，权重随相似度变化。
import json
import re
import name_compare
name_judge = name_compare.name_judge
with open("train_pub.json") as file1:
    pub = json.load(file1)
with open("train_author.json") as file2:
    author = json.load(file2)
#先观测一下作者的机构是否变化过
dict_writer_org = {}
#记录作者的机构信息
#key->list of org

lost_author = 0
def get_org(lost_author):#此函数用来填写dict_writer_org

    for name in author:
        for writer in author[name]:
            for article in author[name][writer]:
                for auth in pub[article]["authors"]:
                    if name_judge(name,auth["name"]):
                        #print(name + " <==> " + auth["name"])
                        try:
                            #print("name: " + name)
                            #print("writer_id" + writer)
                            if writer not in dict_writer_org:
                                #print("4")
                                dict_writer_org[writer] = [auth["org"], ]

                            else:
                                #print("5")
                                if(auth["org"] not in dict_writer_org[writer]):
                                    dict_writer_org[writer].append(auth["org"])
                                else:
                                    pass
                        except:
                            if "org" not in auth:
                                pass
                                #print("org信息缺失")
                            else:
                                pass
                                #print("其他错误")
                        #print("在"+article+"里找到了"+writer)
                        break
                    else:
                        pass
                else:
                    print("想在文章"+article+"找到：" + name)
                    print("以下为文章中的作者：")
                    for auth in pub[article]["authors"]:
                        pass
                        print(auth["name"].lower())
                    lost_author += 1

                    #print("从作者论文ID找到论文以后，在论文的author里没有找到该作者名字")
                    #高达56998人次
    return lost_author
lost_author = get_org(lost_author)
print(lost_author)#56998 改进之后 6137
#print(dict_writer_org.__len__())#表只有16429个作者，但是全部一共应该有22839人，人呢？ 改进之后 22593
#发现问题，表示缩写的.在author中没有存储
#print(dict_writer_org)
#for writer in dict_writer_org:
#    print(writer)
#    print(dict_writer_org[writer])

#到此为止，已经大致获取了作者的org信息，之后在进行比对时候，按照相似度，赋予该信息不同的权值