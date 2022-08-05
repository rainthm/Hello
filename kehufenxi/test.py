# code=utf-8
import xlwings as xw
import time
import jieba
from fuzzywuzzy import fuzz
from fuzzywuzzy import process





xlsx_market_name = "North2022725test.xlsx"
xlsx_sop_name = "现有客户&锁定客户去重8.4.xlsx"

#打开市场收集回来的潜客名称表
app = xw.App(visible=False, add_book=False)
market_book = app.books.open(xlsx_market_name)
sheet_market_name = market_book.sheets[1]
total_rows = sheet_market_name.used_range.last_cell.row
print('--------------------------------------------------')
print('本次收集客户总数：',total_rows)
#获取市场部名单表中的客户名称
market_customer_names = sheet_market_name.range((3,4),(total_rows,4)).value

#xlsx_market = xlrd.open_workbook_xls(xlsx_market_name)
#sheet_market_name = xlsx_market.sheet_by_index(1)
#print(sheet_market_name)
#print(market_customer_names)


#对存量客户名称进行关键字拆分，并建立字典

name_list = jieba.cut(market_customer_names,cut_all=True)
print(list(name_list))

'''



#打开现有存量名称表
#app = xw.App(visible=False, add_book=False)
sop_book = app.books.open(xlsx_sop_name)
sheet_sop_name = sop_book.sheets[0]
#print(sheet_sop_name)
total_sop_rows = sheet_sop_name.used_range.last_cell.row
print('--------------------------------------------------')
print('存量客户总数：',total_sop_rows)
#获取存量客户名单表中的客户名称
sop_customer_names = sheet_sop_name.range((2,4),(total_sop_rows,4)).value
#print(sop_customer_names)





#计算模糊关联度
for i in range(len(market_customer_names)):
    mkt_name = market_customer_names[i]
    print(mkt_name)
    
    max_corr = 0
    most_likely_sop_name = ''
    for sop_name in sop_customer_names:
        corr = fuzz.ratio(mkt_name, sop_name)
        #print(corr)
        if corr > max_corr:
            max_corr = corr
            most_likely_sop_name = sop_name
            
    if max_corr == 100:
        print('命中>>>>>>>>>>>>：',most_likely_sop_name)
    elif max_corr > 60:
        #print('市场收集客户名称：',mkt_name)
        print('最佳匹配现网客户名称：',most_likely_sop_name)
        print('匹配度(百分制) = ', max_corr)
    else:
        print('未找到相对匹配客户，可能是新客户')



market_book.close()
sop_book.close()
app.quit()

'''


market_book.close()
app.quit()