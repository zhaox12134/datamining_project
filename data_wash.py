#本模块用于淘洗数据，去除对结果没有帮助的噪声数据，用于后续分析
#貌似有重复的文章，是作者部分出现了两篇还是一篇文章有两个ID？抽样检查，发现应该是后者
import json

with open("train_pub.json") as file1:
    pub = json.load(file1)
with open("train_author.json") as file2:
    author = json.load(file2)

including = 0
not_including = 0
count = 0
#作者一共22839人
#文章总数为203184篇，其中:
#abstract
#有abstract字段的文章有157230篇，而其中有内容的有129000篇
#无abstract字段的文章有45954篇，再加上有字段无内容的一共74184篇
#title
#所有文章都有title
#keywords
#203127篇文章有keyword，57篇没有
#180086篇文章有字段，而内容为空，23098篇无字段或者内容为空
#128439篇文章有3个或以上关键字，74745篇3个以下
#authors
#185411篇文章作者在10人及以下
#17773篇10人以上
#111778篇文章作者在5人及以下
#91406篇5人以上
#如果我们将优质数据定义为：<1>abstract字段存在且非空<2>keywords在三个及以上<3>authors在10人以下<4><5>
#则优质数据文章有85929篇，非优质数据文章117255篇
#但是，有24547人次需要分类的作者出现在非优质数据中,只有820人次出现在优质数据中
def replace(word):
    a=""
    for i in range(word.__len__()):

        if word[i] == " ":
            a=a+"_"
        else:
            a=a+word[i]
    return a
writer_in_bad_data = 0
writer_in_good_data = 0
double_arti = 0
article_title = []
for article in pub:
    if pub[article]["title"] not in article_title:
        article_title.append(pub[article]["title"])
    else:
        double_arti += 1
'''for article in pub:
    count += 1
    if pub[article]["authors"].__len__()<=10 or ("abstract" in pub[article] and pub[article]["abstract"]!="") or ("keywords" in pub[article] and pub[article]["keywords"].__len__()>=3):
        for writer in pub[article]["authors"]:
            if  replace(writer["name"]) in author:
                writer_in_good_data += 1
        including +=1
    else:
        for writer in pub[article]["authors"]:
            if  replace(writer["name"]) in author:
                writer_in_bad_data += 1
        not_including +=1'''
#print(count)
#print(including)
#print(not_including)
#print(writer_in_good_data)
#print(writer_in_bad_data)
print(double_arti)#有3230篇的标题是相同的，应该考虑去除掉这部分数据

