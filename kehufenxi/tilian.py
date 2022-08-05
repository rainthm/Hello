# code=utf-8
import xlwings as xw


def fine(file_name, dic_set):
    """
    
    """
    xlsx_sop_name = file_name
    app = xw.App(visible=False, add_book=False)
    sop_book = app.books.open(xlsx_sop_name)
    sheet_sop_name = sop_book.sheets[1]




xlsx_sop_name = "East20220728.xlsx"
app = xw.App(visible=False, add_book=False)
sop_book = app.books.open(xlsx_sop_name)
sheet_sop_name = sop_book.sheets[1]


#将字典里面的词存到集合或者列表中
dict = {'(',')','（','）'}



#SaveList = []
fR = open('..\dict.txt', 'r', encoding='UTF-8')
with fR:
    for line in fR:
        line = line.strip('\n');
        #SaveList.append(line)
        dict.add(line)
#print(SaveList)
print(dict)
# line = fR.readline()
# line = line[:-1]
# dict.add(line)

#读取公司名文件，并查找其中是否含有字典中的词，如果有，则删除对应部分
#删除后写入到新文件中
fW = open('newcompany.txt', 'w', encoding="utf-8")
num = 0
fT = open('ceshigongsi.txt', 'r', encoding='UTF-8')
with fT:
    for company in fT:
        new_comp = company.strip('\n')
        num = num + 1
        for stop in dict:
            if stop in new_comp:
                new_comp = new_comp.replace(stop, "")
        #print(new_comp)
        fW.write(new_comp+'\n')
        sheet_sop_name.range(num, 6).value = new_comp
        
                

#line = fT.readline()
#print(line)


#
#for word in tags:
#    fW.write(word+'\n')

fR.close()
fT.close()
fW.close()
sop_book.save()
sop_book.close()
app.quit()
