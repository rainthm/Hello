# code=utf-8
import sys
import xlwings as xw


#该文件主要用于将在网客户名单进行名称主体提炼,从第四列提取名字提炼后放到第6列
#表格名为：
#
#               现有客户锁定客户去重.xlsx
#
#该表格也可以手动维护
#
#
#
#
#
#
#
#取得需要提炼名字的表格
biaogemingzi = sys.argv[1]
#字典存放文件
zidianmingzi = sys.argv[2]

xlsx_sop_name = biaogemingzi
#xlsx_sop_name = "现有客户锁定客户去重.xlsx"
app = xw.App(visible=False, add_book=False)
sop_book = app.books.open(xlsx_sop_name)
sheet_sop_name = sop_book.sheets[0]
total_sop_rows = sheet_sop_name.used_range.last_cell.row
#获取SOP名单表中的客户名称
sop_customer_names = sheet_sop_name.range((2,4),(total_sop_rows,4)).value
#print(sheet_sop_name)

#将字典里面的词存到集合或者列表中
dict = {'(',')','（','）'}
fR = open(zidianmingzi, 'r', encoding='UTF-8')
with fR:
    for line in fR:
        line = line.strip('\n');
        #SaveList.append(line)
        dict.add(line)
#print(dict)

print("请稍等……")
#读取公司名文件，并查找其中是否含有字典中的词，如果有，则删除对应部分
#删除后写入到新文件中
#fW = open('newcompany.txt', 'w', encoding="utf-8")
sheet_sop_name.range("F1").value = "现网客户简称"      
for num in range(2,total_sop_rows+1):
    orgin_name = str(sheet_sop_name.range(num, 4).value) 
    #通过匹配进行名称缩写，提取主体名
    new_comp = orgin_name
    for stop in dict:
        if stop in new_comp:
            new_comp = new_comp.replace(stop, "")
    #将主体名写回到表格中F列        
    sheet_sop_name.range(num, 6).value = new_comp     
print("本次操作成功，一共有 " , num , " 个现网客户。现在可以打开原表格查看简称是否正确。")                     
#print(num)

fR.close()
sop_book.save()
sop_book.close()
app.quit()
