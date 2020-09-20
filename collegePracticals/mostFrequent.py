import collections

file = open('data.txt', encoding="utf8")
content = file.read()

wordcount = {}
# To eliminate duplicates, remember to split by punctuation, and use case demiliters.
for word in content.lower().split():
    word = word.replace(".","")
    word = word.replace(",","")
    word = word.replace(":","")
    word = word.replace("\"","")
    word = word.replace("!","")
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1


for keys,value in wordcount.items():
    print(keys , " : ", value)

file.close()