# code=utf-8
import sys
import xlwings as xw
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

#用于根据字典表，将市场收集到的公司文件名，进行主体词提取，并存在源文件的第6列

#取得需要提炼名字的表格
biaogemingzi = sys.argv[1]
#字典存放文件
zidianmingzi = sys.argv[2]
#存放存量客户的文件名字
cunliangbiaoge = sys.argv[3]

xlsx_sop_name = cunliangbiaoge
xlsx_market_name = biaogemingzi

############################################################################################################################
#关联度匹配参数
wanquanpipei = 100  #完全匹配
bachengpipei = 80   #八成匹配
############################################################################################################################


def fine(file_name, dic_set):
    """
    这个函数暂时不用，后面再优化
    """
    xlsx_market_name = file_name
    app = xw.App(visible=False, add_book=False)
    market_book = app.books.open(xlsx_market_name)
    sheet_market_name = market_book.sheets[1]

############################################################################################################################
#将字典里面的词存到集合
dict = {'(',')','（','）'}
fR = open(zidianmingzi, 'r', encoding='UTF-8')
with fR:
    for line in fR:
        line = line.strip('\n');
        dict.add(line)
#print(dict)
############################################################################################################################



############################################################################################################################
#打开现有存量名称表
app = xw.App(visible=False, add_book=False)
#xlsx_sop_name = "现有客户&锁定客户去重8.4.xlsx"
sop_book = app.books.open(xlsx_sop_name)
sheet_sop_name = sop_book.sheets[0]
total_sop_rows = sheet_sop_name.used_range.last_cell.row
print('--------------------------------------------------')
print('\n存量客户总数：',total_sop_rows,'\n')
print('--------------------------------------------------')
#获取SOP名单表中的客户名称
sop_customer_names = sheet_sop_name.range((2,6),(total_sop_rows,6)).value
sop_customer_state = sheet_sop_name.range((2,5),(total_sop_rows,5)).value
#for i in range(1, total_sop_rows):
#    print(sop_customer_names[i])
############################################################################################################################


############################################################################################################################
#打开市场收集客户名单表
#xlsx_market_name = "2018 BJ AWS.xlsx"
#app = xw.App(visible=False, add_book=False)
market_book = app.books.open(xlsx_market_name)
sheet_market_name = market_book.sheets[1]
total_market_rows = sheet_market_name.used_range.last_cell.row
print('--------------------------------------------------')
print('\n本次收集客户联系条目总数：',total_market_rows,'\n')
print('--------------------------------------------------')


total_matched = 0

sheet_market_name.range("F1").value = "公司主体名提取"
sheet_market_name.range("H1").value = "和在网客户匹配度对比结果"
sheet_market_name.range("I1").value = "客户状态"
#对市场收集名单表中的客户名称，逐个进行
#1、主体词提炼，并写入到原来表格的第H列
#2、关联度匹配，
# 2.1 如果100%匹配，则标注为在网客户
# 2.2 如果75%匹配，则标注为关注客户
for num in range(2,total_market_rows+1):
    orgin_name = str(sheet_market_name.range(num, 4).value) 
    #通过匹配进行名称缩写，提取主体名
    new_comp = orgin_name
    for stop in dict:
        if stop in new_comp:
            new_comp = new_comp.replace(stop, "")
            
    #将主体名写回到表格中F列        
    sheet_market_name.range(num, 6).value = new_comp
    
    #计算和现网客户的关联度
    max_corr = 0
    most_likely_sop_name = ''
    position = 0
    for i in range(0, total_sop_rows-1):
        #print(sop_customer_names[i])
        sop_name = sop_customer_names[i]
    #for sop_name in sop_customer_names:
        corr = fuzz.ratio(new_comp, sop_name)
        #print(corr)
        if corr > max_corr:
            max_corr = corr
            most_likely_sop_name = sop_name
            position = i
    #根据和现网客户的关联度，在网或者高度关联客户，则写入到H列，并用颜色区分
    #在网客户则        
    if max_corr == wanquanpipei:
        print("客户名称： " + str(orgin_name) + "\n")
        print("客户简称： " + str(new_comp) + '\n')
        total_matched = total_matched + 1
        print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<命 中 现 网 客 户>>>>>>>>>>>>>>>>>>>>>>>>>>>>：',most_likely_sop_name,'\n')
        sheet_market_name.range(num,8).value = "在网客户"
        sheet_market_name.range(num,8).color = (255,0,0)
        sheet_market_name.range(num,9).value = sop_customer_state[position]
        sheet_market_name.range(num,9).color = (255,0,0)
    elif max_corr > bachengpipei:
        print('\n--------------------------------------------------------------------------------\n')
        print("客户名称简称： " + str(orgin_name) + "\n")
        print('             最佳匹配现网客户名称：',most_likely_sop_name)
        print('             匹配度(百分制) = ', max_corr,'\n')
        print('--------------------------------------------------------------------------------\n')
        sheet_market_name.range(num,8).value = "建议人工比对客户"
        sheet_market_name.range(num,8).color = (0,0,250)
        #sheet_market_name.range(num,9).value = sop_customer_state[position]
        sheet_market_name.range(num,9).color = (0,250,255)
    else:
        #print('未找到相对匹配客户，可能是新客户\n')
        pass    
    
############################################################################################################################



print("总命中条目数：", total_matched)



fR.close()
market_book.save()
market_book.close()
sop_book.close()
app.quit()
