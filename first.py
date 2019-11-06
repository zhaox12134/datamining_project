import json

##整个train_author.json文件可视作一个字典，关键字是姓名，每个被索引元素也是字典
##每个索引的字典是人(唯一)的ID与其著作的映射关系，一个人对应多个著作数据

##当遍历一个字典时候，只是在遍历关键字
#train_pub 作为一个字典，其关键字是论文的ID
#
with open( "train_pub.json") as file:
    a = json.load(file)
    for item in a["P9a1gcvg"]:
        print(a["P9a1gcvg"][item])
    print ("..................")





