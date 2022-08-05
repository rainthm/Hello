
import jieba.analyse

fR = open('chai_quchong.txt', 'r', encoding='UTF-8')
data = fR.read()

topK = 30
tags = jieba.analyse.extract_tags(data, topK=topK)


print(tags)

fW = open('dict.txt', 'w', encoding="utf-8")
for word in tags:
    fW.write(word+'\n')

fR.close()
fW.close()