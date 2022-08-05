# code=utf-8
import xlwings as xw
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

#用于根据字典表，将市场收集到的公司文件名，进行主体词提取，并存在源文件的第6列
#同时生成文件newcompany.txt，即简称的公司名字


def fine(file_name, dic_set):
    """
    
    """
    xlsx_market_name = file_name
    app = xw.App(visible=False, add_book=False)
    market_book = app.books.open(xlsx_market_name)
    sheet_market_name = market_book.sheets[1]




xlsx_market_name = "大华南测试1.xlsx"
app = xw.App(visible=False, add_book=False)
market_book = app.books.open(xlsx_market_name)
sheet_market_name = market_book.sheets[1]


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


############################################################################################################################
#打开现有存量名称表
#app = xw.App(visible=False, add_book=False)
xlsx_sop_name = "现有客户&锁定客户去重8.4.xlsx"
sop_book = app.books.open(xlsx_sop_name)
sheet_sop_name = sop_book.sheets[0]
total_sop_rows = sheet_sop_name.used_range.last_cell.row
print('--------------------------------------------------')
print('\n存量客户总数：',total_sop_rows,'\n')
print('--------------------------------------------------')
#获取SOP名单表中的客户名称
sop_customer_names = sheet_sop_name.range((2,6),(total_sop_rows,6)).value
############################################################################################################################


#读取公司名文件，并查找其中是否含有字典中的词，如果有，则删除对应部分
#删除后写入到新文件中
total_matched = 0
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
        sheet_market_name.range(num, 6).value = new_comp
        
        max_corr = 0
        most_likely_sop_name = ''
        for sop_name in sop_customer_names:
            corr = fuzz.ratio(new_comp, sop_name)
            #print(corr)
            if corr > max_corr:
                max_corr = corr
                most_likely_sop_name = sop_name
        if max_corr == 100:
            print("客户名称： " + str(company) + "\n")
            print("客户简称： " + str(new_comp) + '\n')
            total_matched = total_matched + 1
            print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<命 中 现 网 客 户>>>>>>>>>>>>>>>>>>>>>>>>>>>>：',most_likely_sop_name,'\n')
            sheet_market_name.range(num,8).value = "在网客户"
            sheet_market_name.range(num,8).color = (255,0,0)
        elif max_corr > 70:
            print('\n--------------------------------------------------------------------------------\n')
            print("客户名称简称： " + str(company) + "\n")
            print('             最佳匹配现网客户名称：',most_likely_sop_name)
            print('匹配度(百分制) = ', max_corr,'\n')
            print('--------------------------------------------------------------------------------\n')
            sheet_market_name.range(num,8).value = "建议人工比对客户"
            sheet_market_name.range(num,8).color = (0,0,250)
        else:
        #print('未找到相对匹配客户，可能是新客户\n')
            pass

print("总命中客户数：", total_matched)
fR.close()
fT.close()
fW.close()
market_book.save()
market_book.close()
sop_book.close()
app.quit()
