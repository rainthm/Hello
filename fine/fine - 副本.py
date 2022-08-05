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

############################################################################################################################
#将字典里面的词存到集合
dict = {'(',')','（','）'}
fR = open('..\dict.txt', 'r', encoding='UTF-8')
with fR:
    for line in fR:
        line = line.strip('\n');
        dict.add(line)
#print(dict)
############################################################################################################################



############################################################################################################################
#打开现有存量名称表
app = xw.App(visible=False, add_book=False)
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


############################################################################################################################
#打开市场收集客户名单表
xlsx_market_name = "2018 BJ AWS.xlsx"
#app = xw.App(visible=False, add_book=False)
market_book = app.books.open(xlsx_market_name)
sheet_market_name = market_book.sheets[1]
total_market_rows = sheet_market_name.used_range.last_cell.row
print('--------------------------------------------------')
print('\n本次收集客户联系条目总数：',total_market_rows,'\n')
print('--------------------------------------------------')
#获取市场收集名单表中的客户名称
#market_customer_names = sheet_market_name.range((2,6),(total_market_rows,6)).value


#fW = open('origin_company.txt', 'w', encoding="utf-8")
total_matched = 0

sheet_market_name.range("F1").value = "公司主体名提取"
sheet_market_name.range("H1").value = "和在网客户匹配度对比"

for num in range(2,total_market_rows+1):
    orgin_name = str(sheet_market_name.range(num, 4).value)
    #fW.write(orgin_name + '\n')   
    
    #通过匹配进行名称缩写，提取主体名
    new_comp = orgin_name
    for stop in dict:
        if stop in new_comp:
            new_comp = new_comp.replace(stop, "")
    #将主体名写回到表格中        
    sheet_market_name.range(num, 6).value = new_comp
    
    #计算和现网客户的关联度
    max_corr = 0
    most_likely_sop_name = ''
    for sop_name in sop_customer_names:
        corr = fuzz.ratio(new_comp, sop_name)
        #print(corr)
        if corr > max_corr:
            max_corr = corr
            most_likely_sop_name = sop_name
    #根据和现网客户的关联度，进行对应操作        
    if max_corr == 100:
        print("客户名称： " + str(orgin_name) + "\n")
        print("客户简称： " + str(new_comp) + '\n')
        total_matched = total_matched + 1
        print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<命 中 现 网 客 户>>>>>>>>>>>>>>>>>>>>>>>>>>>>：',most_likely_sop_name,'\n')
        sheet_market_name.range(num,8).value = "在网客户"
        sheet_market_name.range(num,8).color = (255,0,0)
    elif max_corr > 70:
        print('\n--------------------------------------------------------------------------------\n')
        print("客户名称简称： " + str(orgin_name) + "\n")
        print('             最佳匹配现网客户名称：',most_likely_sop_name)
        print('匹配度(百分制) = ', max_corr,'\n')
        print('--------------------------------------------------------------------------------\n')
        sheet_market_name.range(num,8).value = "建议人工比对客户"
        sheet_market_name.range(num,8).color = (0,0,250)
    else:
        #print('未找到相对匹配客户，可能是新客户\n')
        pass    
    
############################################################################################################################



print("总命中客户数：", total_matched)



fR.close()
market_book.save()
market_book.close()
sop_book.close()
app.quit()
