import json
import sklearn

#testdata = {}
#testdata['key1'] = {"a":123, "b":456,"c":456,"d":456}
with open("train_pub.json") as file1:
    pub = json.load(file1)
with open("train_author.json") as file2:
    author = json.load(file2)
#print("juan_du" in author)
#print(pub["Ujdl9fhz"])
#for writer in pub["Ujdl9fhz"]["authors"]:
#    print( writer)
#count=0
#for name in author:
 #   for writer in author[name]:
#        count += 1

#print("11" in b)
#print(count)
#a = "aaa bbb"
#print("a bb"=="a bb")
'''for name in author:
    if "wNNsUQUZ" in author[name]:
        print(author[name]["wNNsUQUZ"])
        for arti in author[name]["wNNsUQUZ"]:
            print(pub[arti])'''

