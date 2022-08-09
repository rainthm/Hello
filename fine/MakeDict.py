# code=utf-8
import jieba.analyse
import sys
import xlwings as xw
####################################################################################
#
# MakeDict
#       从一个excel表格中提取所有的客户名称，生成常见词的字典
#   参数：
#           string: Customers_Name_Excel 存放客户名称的文件
#           string: Dict                 字典文件名
#           integer:freq                  整数型文字，表示提炼多少个字词作为字典
#   用法：
#           python MakeDict  Customers_Name_Excel.exlx  dict.txt    freq
#
#
####################################################################################

#出现频次topK个最多的词汇
#通常该值小于30，建议在生成的字典文件中进行词语调整，同时改动该值
#topK = 20


#表格文件名
biaogemingzi = sys.argv[1]
#字典文件名
zidian = sys.argv[2]
#出现频次topK个最多的词汇
topN = int(sys.argv[3])

xlsx_sop_name = biaogemingzi
app = xw.App(visible=False, add_book=False)
sop_book = app.books.open(xlsx_sop_name)
sheet_sop_name = sop_book.sheets[0]
total_sop_rows = sheet_sop_name.used_range.last_cell.row
#获取SOP名单表中的客户名称
sop_customer_names = sheet_sop_name.range((2,4),(total_sop_rows,4)).value
#print(sheet_sop_name)

data = str(sop_customer_names)

tags = jieba.analyse.extract_tags(data, topK=topN)


fW = open(zidian, 'w', encoding="utf-8")
for word in tags:
    fW.write(word+'\n')


fW.close()
sop_book.close()
app.quit()